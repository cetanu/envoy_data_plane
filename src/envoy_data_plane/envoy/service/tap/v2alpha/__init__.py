# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/tap/v2alpha/common.proto, envoy/service/tap/v2alpha/tap.proto, envoy/service/tap/v2alpha/tapds.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Optional, Union

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class OutputSinkFormat(betterproto.Enum):
    JSON_BODY_AS_BYTES = 0
    JSON_BODY_AS_STRING = 1
    PROTO_BINARY = 2
    PROTO_BINARY_LENGTH_DELIMITED = 3
    PROTO_TEXT = 4


@dataclass(eq=False, repr=False)
class TapConfig(betterproto.Message):
    """Tap configuration."""

    # The match configuration. If the configuration matches the data source being
    # tapped, a tap will occur, with the result written to the configured output.
    match_config: "MatchPredicate" = betterproto.message_field(1)
    # The tap output configuration. If a match configuration matches a data
    # source being tapped, a tap will occur and the data will be written to the
    # configured output.
    output_config: "OutputConfig" = betterproto.message_field(2)
    # [#not-implemented-hide:] Specify if Tap matching is enabled. The % of
    # requests\connections for which the tap matching is enabled. When not
    # enabled, the request\connection will not be recorded. .. note::   This
    # field defaults to 100/:ref:`HUNDRED
    # <envoy_api_enum_type.FractionalPercent.DenominatorType>`.
    tap_enabled: "___api_v2_core__.RuntimeFractionalPercent" = (
        betterproto.message_field(3)
    )


@dataclass(eq=False, repr=False)
class MatchPredicate(betterproto.Message):
    """
    Tap match configuration. This is a recursive structure which allows complex
    nested match configurations to be built using various logical operators.
    [#next-free-field: 9]
    """

    # A set that describes a logical OR. If any member of the set matches, the
    # match configuration matches.
    or_match: "MatchPredicateMatchSet" = betterproto.message_field(1, group="rule")
    # A set that describes a logical AND. If all members of the set match, the
    # match configuration matches.
    and_match: "MatchPredicateMatchSet" = betterproto.message_field(2, group="rule")
    # A negation match. The match configuration will match if the negated match
    # condition matches.
    not_match: "MatchPredicate" = betterproto.message_field(3, group="rule")
    # The match configuration will always match.
    any_match: bool = betterproto.bool_field(4, group="rule")
    # HTTP request headers match configuration.
    http_request_headers_match: "HttpHeadersMatch" = betterproto.message_field(
        5, group="rule"
    )
    # HTTP request trailers match configuration.
    http_request_trailers_match: "HttpHeadersMatch" = betterproto.message_field(
        6, group="rule"
    )
    # HTTP response headers match configuration.
    http_response_headers_match: "HttpHeadersMatch" = betterproto.message_field(
        7, group="rule"
    )
    # HTTP response trailers match configuration.
    http_response_trailers_match: "HttpHeadersMatch" = betterproto.message_field(
        8, group="rule"
    )


@dataclass(eq=False, repr=False)
class MatchPredicateMatchSet(betterproto.Message):
    """A set of match configurations used for logical operations."""

    # The list of rules that make up the set.
    rules: List["MatchPredicate"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class HttpHeadersMatch(betterproto.Message):
    """HTTP headers match configuration."""

    # HTTP headers to match.
    headers: List["___api_v2_route__.HeaderMatcher"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class OutputConfig(betterproto.Message):
    """Tap output configuration."""

    # Output sinks for tap data. Currently a single sink is allowed in the list.
    # Once multiple sink types are supported this constraint will be relaxed.
    sinks: List["OutputSink"] = betterproto.message_field(1)
    # For buffered tapping, the maximum amount of received body that will be
    # buffered prior to truncation. If truncation occurs, the :ref:`truncated
    # <envoy_api_field_data.tap.v2alpha.Body.truncated>` field will be set. If
    # not specified, the default is 1KiB.
    max_buffered_rx_bytes: Optional[int] = betterproto.message_field(
        2, wraps=betterproto.TYPE_UINT32
    )
    # For buffered tapping, the maximum amount of transmitted body that will be
    # buffered prior to truncation. If truncation occurs, the :ref:`truncated
    # <envoy_api_field_data.tap.v2alpha.Body.truncated>` field will be set. If
    # not specified, the default is 1KiB.
    max_buffered_tx_bytes: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT32
    )
    # Indicates whether taps produce a single buffered message per tap, or
    # multiple streamed messages per tap in the emitted :ref:`TraceWrapper
    # <envoy_api_msg_data.tap.v2alpha.TraceWrapper>` messages. Note that streamed
    # tapping does not mean that no buffering takes place. Buffering may be
    # required if data is processed before a match can be determined. See the
    # HTTP tap filter :ref:`streaming <config_http_filters_tap_streaming>`
    # documentation for more information.
    streaming: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class OutputSink(betterproto.Message):
    """Tap output sink configuration."""

    # Sink output format.
    format: "OutputSinkFormat" = betterproto.enum_field(1)
    # Tap output will be streamed out the :http:post:`/tap` admin endpoint. ..
    # attention::   It is only allowed to specify the streaming admin output sink
    # if the tap is being   configured from the :http:post:`/tap` admin endpoint.
    # Thus, if an extension has   been configured to receive tap configuration
    # from some other source (e.g., static   file, XDS, etc.) configuring the
    # streaming admin output type will fail.
    streaming_admin: "StreamingAdminSink" = betterproto.message_field(
        2, group="output_sink_type"
    )
    # Tap output will be written to a file per tap sink.
    file_per_tap: "FilePerTapSink" = betterproto.message_field(
        3, group="output_sink_type"
    )
    # [#not-implemented-hide:] GrpcService to stream data to. The format argument
    # must be PROTO_BINARY.
    streaming_grpc: "StreamingGrpcSink" = betterproto.message_field(
        4, group="output_sink_type"
    )


@dataclass(eq=False, repr=False)
class StreamingAdminSink(betterproto.Message):
    """Streaming admin sink configuration."""

    pass


@dataclass(eq=False, repr=False)
class FilePerTapSink(betterproto.Message):
    """
    The file per tap sink outputs a discrete file for every tapped stream.
    """

    # Path prefix. The output file will be of the form <path_prefix>_<id>.pb,
    # where <id> is an identifier distinguishing the recorded trace for stream
    # instances (the Envoy connection ID, HTTP stream ID, etc.).
    path_prefix: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class StreamingGrpcSink(betterproto.Message):
    """
    [#not-implemented-hide:] Streaming gRPC sink configuration sends the taps
    to an external gRPC server.
    """

    # Opaque identifier, that will be sent back to the streaming grpc server.
    tap_id: str = betterproto.string_field(1)
    # The gRPC server that hosts the Tap Sink Service.
    grpc_service: "___api_v2_core__.GrpcService" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class StreamTapsRequest(betterproto.Message):
    """
    [#not-implemented-hide:] Stream message for the Tap API. Envoy will open a
    stream to the server and stream taps without ever expecting a response.
    """

    # Identifier data effectively is a structured metadata. As a performance
    # optimization this will only be sent in the first message on the stream.
    identifier: "StreamTapsRequestIdentifier" = betterproto.message_field(1)
    # The trace id. this can be used to merge together a streaming trace. Note
    # that the trace_id is not guaranteed to be spatially or temporally unique.
    trace_id: int = betterproto.uint64_field(2)
    # The trace data.
    trace: "___data_tap_v2_alpha__.TraceWrapper" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class StreamTapsRequestIdentifier(betterproto.Message):
    # The node sending taps over the stream.
    node: "___api_v2_core__.Node" = betterproto.message_field(1)
    # The opaque identifier that was set in the :ref:`output config
    # <envoy_api_field_service.tap.v2alpha.StreamingGrpcSink.tap_id>`.
    tap_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class StreamTapsResponse(betterproto.Message):
    """[#not-implemented-hide:]"""

    pass


@dataclass(eq=False, repr=False)
class TapResource(betterproto.Message):
    """
    [#not-implemented-hide:] A tap resource is essentially a tap configuration
    with a name The filter TapDS config references this name.
    """

    # The name of the tap configuration.
    name: str = betterproto.string_field(1)
    # Tap config to apply
    config: "TapConfig" = betterproto.message_field(2)


class TapSinkServiceStub(betterproto.ServiceStub):
    async def stream_taps(
        self,
        request_iterator: Union[
            AsyncIterable["StreamTapsRequest"], Iterable["StreamTapsRequest"]
        ],
    ) -> "StreamTapsResponse":

        return await self._stream_unary(
            "/envoy.service.tap.v2alpha.TapSinkService/StreamTaps",
            request_iterator,
            StreamTapsRequest,
            StreamTapsResponse,
        )


class TapDiscoveryServiceStub(betterproto.ServiceStub):
    async def stream_tap_configs(
        self,
        request_iterator: Union[
            AsyncIterable["___api_v2__.DiscoveryRequest"],
            Iterable["___api_v2__.DiscoveryRequest"],
        ],
    ) -> AsyncIterator["___api_v2__.DiscoveryResponse"]:

        async for response in self._stream_stream(
            "/envoy.service.tap.v2alpha.TapDiscoveryService/StreamTapConfigs",
            request_iterator,
            ___api_v2__.DiscoveryRequest,
            ___api_v2__.DiscoveryResponse,
        ):
            yield response

    async def delta_tap_configs(
        self,
        request_iterator: Union[
            AsyncIterable["___api_v2__.DeltaDiscoveryRequest"],
            Iterable["___api_v2__.DeltaDiscoveryRequest"],
        ],
    ) -> AsyncIterator["___api_v2__.DeltaDiscoveryResponse"]:

        async for response in self._stream_stream(
            "/envoy.service.tap.v2alpha.TapDiscoveryService/DeltaTapConfigs",
            request_iterator,
            ___api_v2__.DeltaDiscoveryRequest,
            ___api_v2__.DeltaDiscoveryResponse,
        ):
            yield response

    async def fetch_tap_configs(
        self,
        *,
        version_info: str = "",
        node: "core.Node" = None,
        resource_names: Optional[List[str]] = None,
        type_url: str = "",
        response_nonce: str = "",
        error_detail: "___google_rpc__.Status" = None,
    ) -> "___api_v2__.DiscoveryResponse":
        resource_names = resource_names or []

        request = ___api_v2__.DiscoveryRequest()
        request.version_info = version_info
        if node is not None:
            request.node = node
        request.resource_names = resource_names
        request.type_url = type_url
        request.response_nonce = response_nonce
        if error_detail is not None:
            request.error_detail = error_detail

        return await self._unary_unary(
            "/envoy.service.tap.v2alpha.TapDiscoveryService/FetchTapConfigs",
            request,
            ___api_v2__.DiscoveryResponse,
        )


class TapSinkServiceBase(ServiceBase):
    async def stream_taps(
        self, request_iterator: AsyncIterator["StreamTapsRequest"]
    ) -> "StreamTapsResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_stream_taps(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        response = await self.stream_taps(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.tap.v2alpha.TapSinkService/StreamTaps": grpclib.const.Handler(
                self.__rpc_stream_taps,
                grpclib.const.Cardinality.STREAM_UNARY,
                StreamTapsRequest,
                StreamTapsResponse,
            ),
        }


class TapDiscoveryServiceBase(ServiceBase):
    async def stream_tap_configs(
        self, request_iterator: AsyncIterator["___api_v2__.DiscoveryRequest"]
    ) -> AsyncIterator["___api_v2__.DiscoveryResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def delta_tap_configs(
        self, request_iterator: AsyncIterator["___api_v2__.DeltaDiscoveryRequest"]
    ) -> AsyncIterator["___api_v2__.DeltaDiscoveryResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def fetch_tap_configs(
        self,
        version_info: str,
        node: "core.Node",
        resource_names: Optional[List[str]],
        type_url: str,
        response_nonce: str,
        error_detail: "___google_rpc__.Status",
    ) -> "___api_v2__.DiscoveryResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_stream_tap_configs(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        await self._call_rpc_handler_server_stream(
            self.stream_tap_configs,
            stream,
            request_kwargs,
        )

    async def __rpc_delta_tap_configs(self, stream: grpclib.server.Stream) -> None:
        request_kwargs = {"request_iterator": stream.__aiter__()}

        await self._call_rpc_handler_server_stream(
            self.delta_tap_configs,
            stream,
            request_kwargs,
        )

    async def __rpc_fetch_tap_configs(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "version_info": request.version_info,
            "node": request.node,
            "resource_names": request.resource_names,
            "type_url": request.type_url,
            "response_nonce": request.response_nonce,
            "error_detail": request.error_detail,
        }

        response = await self.fetch_tap_configs(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.tap.v2alpha.TapDiscoveryService/StreamTapConfigs": grpclib.const.Handler(
                self.__rpc_stream_tap_configs,
                grpclib.const.Cardinality.STREAM_STREAM,
                ___api_v2__.DiscoveryRequest,
                ___api_v2__.DiscoveryResponse,
            ),
            "/envoy.service.tap.v2alpha.TapDiscoveryService/DeltaTapConfigs": grpclib.const.Handler(
                self.__rpc_delta_tap_configs,
                grpclib.const.Cardinality.STREAM_STREAM,
                ___api_v2__.DeltaDiscoveryRequest,
                ___api_v2__.DeltaDiscoveryResponse,
            ),
            "/envoy.service.tap.v2alpha.TapDiscoveryService/FetchTapConfigs": grpclib.const.Handler(
                self.__rpc_fetch_tap_configs,
                grpclib.const.Cardinality.UNARY_UNARY,
                ___api_v2__.DiscoveryRequest,
                ___api_v2__.DiscoveryResponse,
            ),
        }


from ....api import v2 as ___api_v2__
from ....api.v2 import core as ___api_v2_core__
from ....api.v2 import route as ___api_v2_route__
from ....data.tap import v2alpha as ___data_tap_v2_alpha__
