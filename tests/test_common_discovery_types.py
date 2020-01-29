import envoy_data_plane.envoy.api.v2 as envoy


def test_a_cluster_can_be_created():
    envoy.Cluster(
        name='TestCluster'
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


def test_a_routeconfiguration_can_be_created():
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
