# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/trace/v3/trace_service.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class StreamTracesResponse(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class StreamTracesMessage(betterproto.Message):
    # Identifier data effectively is a structured metadata. As a performance
    # optimization this will only be sent in the first message on the stream.
    identifier: "StreamTracesMessageIdentifier" = betterproto.message_field(1)
    # A list of Span entries
    spans: List["____opencensus_proto_trace_v1__.Span"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class StreamTracesMessageIdentifier(betterproto.Message):
    # The node sending the access log messages over the stream.
    node: "___config_core_v3__.Node" = betterproto.message_field(1)


class TraceServiceStub(betterproto.ServiceStub):
    async def stream_traces(
        self,
        request_iterator: Union[
            AsyncIterable["StreamTracesMessage"], Iterable["StreamTracesMessage"]
        ],
    ) -> "StreamTracesResponse":

        return await self._stream_unary(
            "/envoy.service.trace.v3.TraceService/StreamTraces",
            request_iterator,
            StreamTracesMessage,
            StreamTracesResponse,
        )


class TraceServiceBase(ServiceBase):
    async def stream_traces(
        self, request_iterator: AsyncIterator["StreamTracesMessage"]
    ) -> "StreamTracesResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_stream_traces(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        response = await self.stream_traces(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.trace.v3.TraceService/StreamTraces": grpclib.const.Handler(
                self.__rpc_stream_traces,
                grpclib.const.Cardinality.STREAM_UNARY,
                StreamTracesMessage,
                StreamTracesResponse,
            ),
        }


from .....opencensus.proto.trace import v1 as ____opencensus_proto_trace_v1__
from ....config.core import v3 as ___config_core_v3__
