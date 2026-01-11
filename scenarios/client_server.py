import vedro
import random
from typing import override
from collections.abc import AsyncIterator
from grpclib.server import Server
from grpclib.client import Channel
from envoy_data_plane.envoy.config.cluster.v3 import Cluster
from envoy_data_plane.envoy.service.cluster.v3 import (
    ClusterDiscoveryServiceBase,
    ClusterDiscoveryServiceAsyncStub,
)
from envoy_data_plane.envoy.service.discovery.v3 import (
    DiscoveryRequest,
    DiscoveryResponse,
)
from envoy_data_plane.google.protobuf import Any

HOST = "127.0.0.1"
PORT = random.randint(10000, 65535)


class ClusterDiscoveryService(ClusterDiscoveryServiceBase):
    @override
    async def stream_clusters(
        self, messages: AsyncIterator[DiscoveryRequest]
    ) -> AsyncIterator[DiscoveryResponse]:
        yield DiscoveryResponse(
            resources=[
                Any.pack(
                    Cluster(
                        name="foobar",
                    )
                )
            ]
        )


class Scenario(vedro.Scenario):
    subject: str = "CDS server can be created & serve requests"

    async def given_server(self):
        self.server = Server([ClusterDiscoveryService()])
        await self.server.start(HOST, PORT)

    async def when_request_is_sent(self):
        channel = Channel(host=HOST, port=PORT)
        service = ClusterDiscoveryServiceAsyncStub(channel)
        requests = [DiscoveryRequest()]
        self.responses = [
            response async for response in service.stream_clusters(messages=requests)
        ]

    async def then_it_should_produce_a_discovery_response(self):
        assert self.responses == [
            DiscoveryResponse(
                resources=[
                    Any(
                        type_url="type.googleapis.com/envoy.config.cluster.v3.Cluster",
                        value=b"\n\x06foobar",
                    )
                ]
            )
        ]
