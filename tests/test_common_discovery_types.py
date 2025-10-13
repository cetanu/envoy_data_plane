from vedro import scenario
from datetime import timedelta

import envoy_data_plane.envoy.api.v2 as envoy
from betterproto2_compiler.known_types.any import Any
from betterproto2_compiler.known_types.google_values import StringValue


@scenario()
def test_a_cluster_can_be_created():
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

    expected = {
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
def test_a_listener_can_be_created():
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
def test_a_route_configuration_can_be_created():
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
def test_a_basic_route_can_convert_to_dict():
    envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
    ).to_dict()


@scenario()
def test_a_route_with_typed_per_filter_config_can_convert_to_dict():
    route = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={"foo": StringValue(value="bar")},
    )
    obj = route.to_dict()
    assert obj["typedPerFilterConfig"]["foo"] == "bar"


@scenario()
def test_route_rules_with_typed_per_filter_config_can_be_encoded_and_decoded():
    actual = envoy.route.Route(
        match=envoy.route.RouteMatch(prefix="/"),
        route=envoy.route.RouteAction(cluster="SomeCluster"),
        typed_per_filter_config={"foo": StringValue(value="bar")},
    )

    expected = {
        "match": {"prefix": "/"},
        "route": {"cluster": "SomeCluster"},
        "typedPerFilterConfig": {"foo": "bar"},
    }

    assert actual.to_dict() == expected
    # FIXME: can't convert back from dict
    # assert envoy.route.Route().from_dict(expected) == actual
