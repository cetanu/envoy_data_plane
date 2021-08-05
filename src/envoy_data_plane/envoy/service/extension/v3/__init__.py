# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/extension/v3/config_discovery.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Optional, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class EcdsDummy(betterproto.Message):
    """
    [#not-implemented-hide:] Not configuration. Workaround c++ protobuf issue
    with importing services: https://github.com/google/protobuf/issues/4221 and
    protoxform to upgrade the file.
    """

    pass


class ExtensionConfigDiscoveryServiceStub(betterproto.ServiceStub):
    async def stream_extension_configs(
        self,
        request_iterator: Union[
            AsyncIterable["__discovery_v3__.DiscoveryRequest"],
            Iterable["__discovery_v3__.DiscoveryRequest"],
        ],
    ) -> AsyncIterator["__discovery_v3__.DiscoveryResponse"]:

        async for response in self._stream_stream(
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/StreamExtensionConfigs",
            request_iterator,
            __discovery_v3__.DiscoveryRequest,
            __discovery_v3__.DiscoveryResponse,
        ):
            yield response

    async def delta_extension_configs(
        self,
        request_iterator: Union[
            AsyncIterable["__discovery_v3__.DeltaDiscoveryRequest"],
            Iterable["__discovery_v3__.DeltaDiscoveryRequest"],
        ],
    ) -> AsyncIterator["__discovery_v3__.DeltaDiscoveryResponse"]:

        async for response in self._stream_stream(
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/DeltaExtensionConfigs",
            request_iterator,
            __discovery_v3__.DeltaDiscoveryRequest,
            __discovery_v3__.DeltaDiscoveryResponse,
        ):
            yield response

    async def fetch_extension_configs(
        self,
        *,
        version_info: str = "",
        node: "___config_core_v3__.Node" = None,
        resource_names: Optional[List[str]] = None,
        type_url: str = "",
        response_nonce: str = "",
        error_detail: "____google_rpc__.Status" = None,
    ) -> "__discovery_v3__.DiscoveryResponse":
        resource_names = resource_names or []

        request = __discovery_v3__.DiscoveryRequest()
        request.version_info = version_info
        if node is not None:
            request.node = node
        request.resource_names = resource_names
        request.type_url = type_url
        request.response_nonce = response_nonce
        if error_detail is not None:
            request.error_detail = error_detail

        return await self._unary_unary(
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/FetchExtensionConfigs",
            request,
            __discovery_v3__.DiscoveryResponse,
        )


class ExtensionConfigDiscoveryServiceBase(ServiceBase):
    async def stream_extension_configs(
        self, request_iterator: AsyncIterator["__discovery_v3__.DiscoveryRequest"]
    ) -> AsyncIterator["__discovery_v3__.DiscoveryResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delta_extension_configs(
        self, request_iterator: AsyncIterator["__discovery_v3__.DeltaDiscoveryRequest"]
    ) -> AsyncIterator["__discovery_v3__.DeltaDiscoveryResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fetch_extension_configs(
        self,
        version_info: str,
        node: "___config_core_v3__.Node",
        resource_names: Optional[List[str]],
        type_url: str,
        response_nonce: str,
        error_detail: "____google_rpc__.Status",
    ) -> "__discovery_v3__.DiscoveryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_stream_extension_configs(
        self, stream: grpclib.server.Stream
    ) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        await self._call_rpc_handler_server_stream(
            self.stream_extension_configs,
            stream,
            request_kwargs,
        )

    async def __rpc_delta_extension_configs(
        self, stream: grpclib.server.Stream
    ) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        await self._call_rpc_handler_server_stream(
            self.delta_extension_configs,
            stream,
            request_kwargs,
        )

    async def __rpc_fetch_extension_configs(
        self, stream: grpclib.server.Stream
    ) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "version_info": request.version_info,
            "node": request.node,
            "resource_names": request.resource_names,
            "type_url": request.type_url,
            "response_nonce": request.response_nonce,
            "error_detail": request.error_detail,
        }

        response = await self.fetch_extension_configs(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/StreamExtensionConfigs": grpclib.const.Handler(
                self.__rpc_stream_extension_configs,
                grpclib.const.Cardinality.STREAM_STREAM,
                __discovery_v3__.DiscoveryRequest,
                __discovery_v3__.DiscoveryResponse,
            ),
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/DeltaExtensionConfigs": grpclib.const.Handler(
                self.__rpc_delta_extension_configs,
                grpclib.const.Cardinality.STREAM_STREAM,
                __discovery_v3__.DeltaDiscoveryRequest,
                __discovery_v3__.DeltaDiscoveryResponse,
            ),
            "/envoy.service.extension.v3.ExtensionConfigDiscoveryService/FetchExtensionConfigs": grpclib.const.Handler(
                self.__rpc_fetch_extension_configs,
                grpclib.const.Cardinality.UNARY_UNARY,
                __discovery_v3__.DiscoveryRequest,
                __discovery_v3__.DiscoveryResponse,
            ),
        }


from ...discovery import v3 as __discovery_v3__