from datetime import timedelta

from vedro import scenario

from envoy_data_plane.envoy.config.core.v3 import Metadata
from envoy_data_plane.envoy.service.discovery.v3 import DiscoveryResponse
from envoy_data_plane.envoy.config.core.v3 import (
    Address,
    DataSource,
    Http1ProtocolOptions,
    Http1ProtocolOptionsHeaderKeyFormat,
    Http1ProtocolOptionsHeaderKeyFormatProperCaseWords,
    HttpProtocolOptions,
    RoutingPriority,
    SocketAddress,
    SocketAddressProtocol,
)
from envoy_data_plane.envoy.config.listener.v3 import (
    Listener,
    Filter,
    FilterChain,
)
from envoy_data_plane.envoy.config.cluster.v3 import (
    Cluster,
    ClusterDiscoveryType,
    ClusterDnsLookupFamily,
    OutlierDetection,
    CircuitBreakers,
    CircuitBreakersThresholds,
)
from envoy_data_plane.envoy.config.route.v3 import (
    RouteAction,
    RouteConfiguration,
    VirtualHost,
    Route,
    RouteMatch,
    DirectResponseAction,
)
from envoy_data_plane.google.protobuf import Any, StringValue
from envoy_data_plane.envoy.extensions.access_loggers.stream.v3 import StdoutAccessLog
from envoy_data_plane.envoy.config.core.v3 import SubstitutionFormatString

from envoy_data_plane.helpers import to_struct, to_value


@scenario()
def cluster_can_be_created():
    actual = Cluster(
        name="TestCluster",
        type=ClusterDiscoveryType.STRICT_DNS,
        connect_timeout=timedelta(seconds=5),
        per_connection_buffer_limit_bytes=16777216,
        common_http_protocol_options=HttpProtocolOptions(
            idle_timeout=timedelta(seconds=55)
        ),
        dns_lookup_family=ClusterDnsLookupFamily.V4_ONLY,
        respect_dns_ttl=False,
        http_protocol_options=Http1ProtocolOptions(
            header_key_format=Http1ProtocolOptionsHeaderKeyFormat(
                proper_case_words=Http1ProtocolOptionsHeaderKeyFormatProperCaseWords()
            )
        ),
        outlier_detection=OutlierDetection(),
        circuit_breakers=CircuitBreakers(
            thresholds=[
                CircuitBreakersThresholds(
                    priority=RoutingPriority.DEFAULT, max_connections=32768
                )
            ]
        ),
    )

    expected = {  # pyright: ignore[reportUnknownVariableType]
        "name": "TestCluster",
        "type": "STRICT_DNS",
        "connectTimeout": "5s",
        "dnsLookupFamily": "V4_ONLY",
        "outlierDetection": {},
        "perConnectionBufferLimitBytes": 16777216,
        "commonHttpProtocolOptions": {"idleTimeout": "55s"},
        "httpProtocolOptions": {"headerKeyFormat": {"properCaseWords": {}}},
        "circuitBreakers": {"thresholds": [{"maxConnections": 32768}]},
    }

    assert actual.to_dict() == expected


@scenario()
def listener_can_be_created():
    actual = Listener(
        name="TestListener",
        address=Address(
            socket_address=SocketAddress(
                protocol=SocketAddressProtocol.TCP,
                address="0.0.0.0",
                port_value=8080,
            )
        ),
        filter_chains=[
            FilterChain(
                name="TestFilterChain",
                filters=[Filter(name="envoy.http_connection_manager")],
            )
        ],
    )

    expected = {
        "name": "TestListener",
        "address": {"socketAddress": {"address": "0.0.0.0", "portValue": 8080}},
        "filterChains": [
            {
                "name": "TestFilterChain",
                "filters": [{"name": "envoy.http_connection_manager"}],
            }
        ],
    }

    assert actual.to_dict() == expected


@scenario()
def route_configuration_can_be_created():
    actual = RouteConfiguration(
        name="TestRoutes",
        virtual_hosts=[
            VirtualHost(
                name="TestVirtualHost",
                domains=["test.com"],
                routes=[
                    Route(
                        match=RouteMatch(prefix="/"),
                        route=RouteAction(cluster="SomeCluster"),
                    )
                ],
            )
        ],
    )

    expected = {
        "name": "TestRoutes",
        "virtualHosts": [
            {
                "domains": ["test.com"],
                "name": "TestVirtualHost",
                "routes": [
                    {"match": {"prefix": "/"}, "route": {"cluster": "SomeCluster"}}
                ],
            }
        ],
    }

    assert actual.to_dict() == expected


@scenario()
def basic_route_can_convert_to_dict():
    assert Route(
        match=RouteMatch(prefix="/"),
        route=RouteAction(cluster="SomeCluster"),
    ).to_dict()


@scenario()
def route_rule_with_typed_per_filter_config_can_be_converted_to_dict():
    actual = Route(
        match=RouteMatch(prefix="/"),
        route=RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={"foo": Any.pack(to_value("bar"))},
    )
    expected = {
        "match": {"prefix": "/"},
        "route": {"cluster": "SomeCluster"},
        "typedPerFilterConfig": {
            "foo": {
                "@type": "type.googleapis.com/google.protobuf.Value",
                "value": "bar",
            }
        },
    }
    assert actual.to_dict() == expected


@scenario()
def route_rule_with_typed_per_filter_config_can_be_converted_from_dict():
    _input = {
        "match": {"prefix": "/"},
        "route": {"cluster": "SomeCluster"},
        "typedPerFilterConfig": {
            "foo": {
                "@type": "type.googleapis.com/google.protobuf.StringValue",
                "value": "bar",
            }
        },
    }
    expected = Route(
        match=RouteMatch(prefix="/"),
        route=RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={"foo": Any.pack(StringValue(value="bar"))},
    )
    assert Route().from_dict(_input) == expected


@scenario()
def route_rule_with_typed_per_filter_config_can_be_serialized_and_deserialized():
    _input = Route(
        match=RouteMatch(prefix="/"),
        route=RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    ).SerializeToString()
    expected = Route(
        match=RouteMatch(prefix="/"),
        route=RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    )
    assert Route().FromString(_input) == expected


@scenario()
def old_example_from_readme_works():
    route_config = RouteConfiguration(
        name="MyRouteConfig",
        virtual_hosts=[
            VirtualHost(
                name="SomeWebsite",
                domains=["foobar.com"],
                routes=[
                    Route(
                        name="catchall",
                        match=RouteMatch(prefix="/"),
                        direct_response=DirectResponseAction(
                            status=200,
                            body=DataSource(inline_string="Hello there"),
                        ),
                    )
                ],
            )
        ],
    )
    response = DiscoveryResponse(
        version_info="0",
        resources=[Any.pack(route_config)],
    )
    actual = response.to_dict()
    expected = {
        "versionInfo": "0",
        "resources": [
            {
                "@type": "type.googleapis.com/envoy.config.route.v3.RouteConfiguration",
                "name": "MyRouteConfig",
                "virtualHosts": [
                    {
                        "name": "SomeWebsite",
                        "domains": ["foobar.com"],
                        "routes": [
                            {
                                "name": "catchall",
                                "match": {
                                    "prefix": "/",
                                },
                                "directResponse": {
                                    "status": 200,
                                    "body": {"inlineString": "Hello there"},
                                },
                            }
                        ],
                    }
                ],
            }
        ],
    }
    assert expected == actual


@scenario()
def access_logger_example_with_nested_typed_config():
    actual = Any.pack(
        StdoutAccessLog(
            log_format=SubstitutionFormatString(
                json_format=to_struct(
                    {
                        **{
                            "cluster": "%UPSTREAM_CLUSTER%",
                            "host": "%UPSTREAM_HOST_NAME%",
                        },
                        **{  # overwrite
                            "cluster": "%UPSTREAM_CLUSTER_RAW%",
                            "route": "%ROUTE_NAME%",
                        },
                    }
                )
            ),
        )
    )
    expected = {
        "@type": "type.googleapis.com/envoy.extensions.access_loggers.stream.v3.StdoutAccessLog",
        "logFormat": {
            "jsonFormat": {
                "cluster": "%UPSTREAM_CLUSTER_RAW%",
                "host": "%UPSTREAM_HOST_NAME%",
                "route": "%ROUTE_NAME%",
            }
        },
    }

    assert actual.to_dict() == expected


@scenario()
def metadata_example_with_struct_untyped():
    actual = Any.pack(
        Metadata(
            filter_metadata={
                "foo": to_struct(
                    {
                        "string": "baz",
                        "bool": True,
                        "num": 123.0,
                        "nested_struct": {"nest": "value"},
                    }
                )
            }
        )
    )
    expected = {
        "filterMetadata": {
            "foo": {
                "string": "baz",
                "bool": True,
                "num": 123.0,
                "nested_struct": {"nest": "value"},
            }
        },
        "@type": "type.googleapis.com/envoy.config.core.v3.Metadata",
    }
    assert actual.to_dict() == expected
