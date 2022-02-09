# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/accesslog/v3/als.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class StreamAccessLogsResponse(betterproto.Message):
    """
    Empty response for the StreamAccessLogs API. Will never be sent. See below.
    """

    pass


@dataclass(eq=False, repr=False)
class StreamAccessLogsMessage(betterproto.Message):
    """
    Stream message for the StreamAccessLogs API. Envoy will open a stream to
    the server and stream access logs without ever expecting a response.
    """

    # Identifier data that will only be sent in the first message on the stream.
    # This is effectively structured metadata and is a performance optimization.
    identifier: "StreamAccessLogsMessageIdentifier" = betterproto.message_field(1)
    http_logs: "StreamAccessLogsMessageHttpAccessLogEntries" = (
        betterproto.message_field(2, group="log_entries")
    )
    tcp_logs: "StreamAccessLogsMessageTcpAccessLogEntries" = betterproto.message_field(
        3, group="log_entries"
    )


@dataclass(eq=False, repr=False)
class StreamAccessLogsMessageIdentifier(betterproto.Message):
    # The node sending the access log messages over the stream.
    node: "___config_core_v3__.Node" = betterproto.message_field(1)
    # The friendly name of the log configured in :ref:`CommonGrpcAccessLogConfig
    # <envoy_v3_api_msg_extensions.access_loggers.grpc.v3.CommonGrpcAccessLogConf
    # ig>`.
    log_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class StreamAccessLogsMessageHttpAccessLogEntries(betterproto.Message):
    """Wrapper for batches of HTTP access log entries."""

    log_entry: List[
        "___data_accesslog_v3__.HttpAccessLogEntry"
    ] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class StreamAccessLogsMessageTcpAccessLogEntries(betterproto.Message):
    """Wrapper for batches of TCP access log entries."""

    log_entry: List[
        "___data_accesslog_v3__.TcpAccessLogEntry"
    ] = betterproto.message_field(1)


class AccessLogServiceStub(betterproto.ServiceStub):
    async def stream_access_logs(
        self,
        request_iterator: Union[
            AsyncIterable["StreamAccessLogsMessage"],
            Iterable["StreamAccessLogsMessage"],
        ],
    ) -> "StreamAccessLogsResponse":

        return await self._stream_unary(
            "/envoy.service.accesslog.v3.AccessLogService/StreamAccessLogs",
            request_iterator,
            StreamAccessLogsMessage,
            StreamAccessLogsResponse,
        )


class AccessLogServiceBase(ServiceBase):
    async def stream_access_logs(
        self, request_iterator: AsyncIterator["StreamAccessLogsMessage"]
    ) -> "StreamAccessLogsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_stream_access_logs(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        response = await self.stream_access_logs(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.accesslog.v3.AccessLogService/StreamAccessLogs": grpclib.const.Handler(
                self.__rpc_stream_access_logs,
                grpclib.const.Cardinality.STREAM_UNARY,
                StreamAccessLogsMessage,
                StreamAccessLogsResponse,
            ),
        }


from ....config.core import v3 as ___config_core_v3__
from ....data.accesslog import v3 as ___data_accesslog_v3__
