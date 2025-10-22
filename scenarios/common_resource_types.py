from datetime import timedelta

from vedro import scenario
import envoy_data_plane.envoy.api.v2 as envoy
from envoy_data_plane.google.protobuf import Any, StringValue


@scenario()
def cluster_can_be_created():
    actual = envoy.Cluster(
        name="TestCluster",
        type=envoy.ClusterDiscoveryType.STRICT_DNS,
        connect_timeout=timedelta(seconds=5),
        per_connection_buffer_limit_bytes=16777216,
        common_http_protocol_options=envoy.core.HttpProtocolOptions(
            idle_timeout=timedelta(seconds=55)
        ),
        dns_lookup_family=envoy.ClusterDnsLookupFamily.V4_ONLY,
        respect_dns_ttl=False,
        http_protocol_options=envoy.core.Http1ProtocolOptions(
            header_key_format=envoy.core.Http1ProtocolOptionsHeaderKeyFormat(
                proper_case_words=envoy.core.Http1ProtocolOptionsHeaderKeyFormatProperCaseWords()
            )
        ),
        outlier_detection=envoy.cluster.OutlierDetection(),
        circuit_breakers=envoy.cluster.CircuitBreakers(
            thresholds=[
                envoy.cluster.CircuitBreakersThresholds(
                    priority=envoy.core.RoutingPriority.DEFAULT, max_connections=32768
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
    actual = envoy.Listener(
        name="TestListener",
        address=envoy.core.Address(
            socket_address=envoy.core.SocketAddress(
                protocol=envoy.core.SocketAddressProtocol.TCP,
                address="0.0.0.0",
                port_value=8080,
            )
        ),
        filter_chains=[
            envoy.listener.FilterChain(
                name="TestFilterChain",
                filters=[envoy.listener.Filter(name="envoy.http_connection_manager")],
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
    actual = envoy.RouteConfiguration(
        name="TestRoutes",
        virtual_hosts=[
            envoy.route.VirtualHost(
                name="TestVirtualHost",
                domains=["test.com"],
                routes=[
                    envoy.route.Route(
                        match=envoy.route.RouteMatch(prefix="/"),
                        route=envoy.route.RouteAction(cluster="SomeCluster"),
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
    assert envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
    ).to_dict()


@scenario()
def route_rule_with_typed_per_filter_config_can_be_converted_to_dict():
    actual = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    )
    expected = {
        "match": {"prefix": "/"},
        "route": {"cluster": "SomeCluster"},
        "typedPerFilterConfig": {
            "foo": {
                "@type": "type.googleapis.com/google.protobuf.StringValue",
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
    expected = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    )
    assert envoy.route.Route().from_dict(_input) == expected


@scenario()
def route_rule_with_typed_per_filter_config_can_be_serialized_and_deserialized():
    _input = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    ).SerializeToString()
    expected = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={
            "foo": Any(
                value=StringValue(value="bar").SerializeToString(),
                type_url="type.googleapis.com/google.protobuf.StringValue",
            )
        },
    )
    assert envoy.route.Route().FromString(_input) == expected


@scenario()
def old_example_from_readme_works():
    route_config = envoy.RouteConfiguration(
        name="MyRouteConfig",
        virtual_hosts=[
            envoy.route.VirtualHost(
                name="SomeWebsite",
                domains=["foobar.com"],
                routes=[
                    envoy.route.Route(
                        name="catchall",
                        match=envoy.route.RouteMatch(prefix="/"),
                        direct_response=envoy.route.DirectResponseAction(
                            status=200,
                            body=envoy.core.DataSource(inline_string="Hello there"),
                        ),
                    )
                ],
            )
        ],
    )
    response = envoy.DiscoveryResponse(
        version_info="0",
        resources=[route_config],
    )
    actual = response.to_dict()
    expected = {
        "versionInfo": "0",
        "resources": [
            {
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
