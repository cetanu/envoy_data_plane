import envoy_data_plane.envoy.api.v2 as envoy
from datetime import timedelta


def test_a_cluster_can_be_created():
    envoy.Cluster(
        name='TestCluster',
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
            thresholds=[envoy.cluster.CircuitBreakersThresholds(
                priority=envoy.core.RoutingPriority.DEFAULT,
                max_connections=32768
            )]
        )
    )


def test_a_listener_can_be_created():
    envoy.Listener(
        name='TestListener',
        address=envoy.core.Address(
            socket_address=envoy.core.SocketAddress(
                protocol=envoy.core.SocketAddressProtocol.TCP,
                address='0.0.0.0',
                port_value=8080
            )
        ),
        filter_chains=[
            envoy.listener.FilterChain(
                name='TestFilterChain',
                filters=[
                    envoy.listener.Filter(
                        name='envoy.http_connection_manager'
                    )
                ]
            )
        ]
    )


def test_a_route_configuration_can_be_created():
    envoy.RouteConfiguration(
        name='TestRoutes',
        virtual_hosts=[
            envoy.route.VirtualHost(
                name='TestVirtualHost',
                domains=[
                    'test.com'
                ],
                routes=[
                    envoy.route.Route(
                        match=envoy.route.RouteMatch(prefix='/'),
                        route=envoy.route.RouteAction(cluster='SomeCluster')
                    )
                ]
            )
        ]
    )
