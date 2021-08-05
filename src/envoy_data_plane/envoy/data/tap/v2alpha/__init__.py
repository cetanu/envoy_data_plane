# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/data/tap/v2alpha/common.proto, envoy/data/tap/v2alpha/http.proto, envoy/data/tap/v2alpha/transport.proto, envoy/data/tap/v2alpha/wrapper.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Body(betterproto.Message):
    """
    Wrapper for tapped body data. This includes HTTP request/response body,
    transport socket received and transmitted data, etc.
    """

    # Body data as bytes. By default, tap body data will be present in this
    # field, as the proto `bytes` type can contain any valid byte.
    as_bytes: bytes = betterproto.bytes_field(1, group="body_type")
    # Body data as string. This field is only used when the
    # :ref:`JSON_BODY_AS_STRING <envoy_api_enum_value_service.tap.v2alpha.OutputS
    # ink.Format.JSON_BODY_AS_STRING>` sink format type is selected. See the
    # documentation for that option for why this is useful.
    as_string: str = betterproto.string_field(2, group="body_type")
    # Specifies whether body data has been truncated to fit within the specified
    # :ref:`max_buffered_rx_bytes
    # <envoy_api_field_service.tap.v2alpha.OutputConfig.max_buffered_rx_bytes>`
    # and :ref:`max_buffered_tx_bytes
    # <envoy_api_field_service.tap.v2alpha.OutputConfig.max_buffered_tx_bytes>`
    # settings.
    truncated: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class HttpBufferedTrace(betterproto.Message):
    """A fully buffered HTTP trace message."""

    # Request message.
    request: "HttpBufferedTraceMessage" = betterproto.message_field(1)
    # Response message.
    response: "HttpBufferedTraceMessage" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class HttpBufferedTraceMessage(betterproto.Message):
    """HTTP message wrapper."""

    # Message headers.
    headers: List["___api_v2_core__.HeaderValue"] = betterproto.message_field(1)
    # Message body.
    body: "Body" = betterproto.message_field(2)
    # Message trailers.
    trailers: List["___api_v2_core__.HeaderValue"] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class HttpStreamedTraceSegment(betterproto.Message):
    """
    A streamed HTTP trace segment. Multiple segments make up a full trace.
    [#next-free-field: 8]
    """

    # Trace ID unique to the originating Envoy only. Trace IDs can repeat and
    # should not be used for long term stable uniqueness.
    trace_id: int = betterproto.uint64_field(1)
    # Request headers.
    request_headers: "___api_v2_core__.HeaderMap" = betterproto.message_field(
        2, group="message_piece"
    )
    # Request body chunk.
    request_body_chunk: "Body" = betterproto.message_field(3, group="message_piece")
    # Request trailers.
    request_trailers: "___api_v2_core__.HeaderMap" = betterproto.message_field(
        4, group="message_piece"
    )
    # Response headers.
    response_headers: "___api_v2_core__.HeaderMap" = betterproto.message_field(
        5, group="message_piece"
    )
    # Response body chunk.
    response_body_chunk: "Body" = betterproto.message_field(6, group="message_piece")
    # Response trailers.
    response_trailers: "___api_v2_core__.HeaderMap" = betterproto.message_field(
        7, group="message_piece"
    )


@dataclass(eq=False, repr=False)
class Connection(betterproto.Message):
    """Connection properties."""

    # Local address.
    local_address: "___api_v2_core__.Address" = betterproto.message_field(2)
    # Remote address.
    remote_address: "___api_v2_core__.Address" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class SocketEvent(betterproto.Message):
    """Event in a socket trace."""

    # Timestamp for event.
    timestamp: datetime = betterproto.message_field(1)
    read: "SocketEventRead" = betterproto.message_field(2, group="event_selector")
    write: "SocketEventWrite" = betterproto.message_field(3, group="event_selector")
    closed: "SocketEventClosed" = betterproto.message_field(4, group="event_selector")


@dataclass(eq=False, repr=False)
class SocketEventRead(betterproto.Message):
    """Data read by Envoy from the transport socket."""

    # Binary data read.
    data: "Body" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class SocketEventWrite(betterproto.Message):
    """Data written by Envoy to the transport socket."""

    # Binary data written.
    data: "Body" = betterproto.message_field(1)
    # Stream was half closed after this write.
    end_stream: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class SocketEventClosed(betterproto.Message):
    """The connection was closed."""

    pass


@dataclass(eq=False, repr=False)
class SocketBufferedTrace(betterproto.Message):
    """
    Sequence of read/write events that constitute a buffered trace on a socket.
    [#next-free-field: 6]
    """

    # Trace ID unique to the originating Envoy only. Trace IDs can repeat and
    # should not be used for long term stable uniqueness. Matches connection IDs
    # used in Envoy logs.
    trace_id: int = betterproto.uint64_field(1)
    # Connection properties.
    connection: "Connection" = betterproto.message_field(2)
    # Sequence of observed events.
    events: List["SocketEvent"] = betterproto.message_field(3)
    # Set to true if read events were truncated due to the
    # :ref:`max_buffered_rx_bytes
    # <envoy_api_field_service.tap.v2alpha.OutputConfig.max_buffered_rx_bytes>`
    # setting.
    read_truncated: bool = betterproto.bool_field(4)
    # Set to true if write events were truncated due to the
    # :ref:`max_buffered_tx_bytes
    # <envoy_api_field_service.tap.v2alpha.OutputConfig.max_buffered_tx_bytes>`
    # setting.
    write_truncated: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class SocketStreamedTraceSegment(betterproto.Message):
    """
    A streamed socket trace segment. Multiple segments make up a full trace.
    """

    # Trace ID unique to the originating Envoy only. Trace IDs can repeat and
    # should not be used for long term stable uniqueness. Matches connection IDs
    # used in Envoy logs.
    trace_id: int = betterproto.uint64_field(1)
    # Connection properties.
    connection: "Connection" = betterproto.message_field(2, group="message_piece")
    # Socket event.
    event: "SocketEvent" = betterproto.message_field(3, group="message_piece")


@dataclass(eq=False, repr=False)
class TraceWrapper(betterproto.Message):
    """
    Wrapper for all fully buffered and streamed tap traces that Envoy emits.
    This is required for sending traces over gRPC APIs or more easily
    persisting binary messages to files.
    """

    # An HTTP buffered tap trace.
    http_buffered_trace: "HttpBufferedTrace" = betterproto.message_field(
        1, group="trace"
    )
    # An HTTP streamed tap trace segment.
    http_streamed_trace_segment: "HttpStreamedTraceSegment" = betterproto.message_field(
        2, group="trace"
    )
    # A socket buffered tap trace.
    socket_buffered_trace: "SocketBufferedTrace" = betterproto.message_field(
        3, group="trace"
    )
    # A socket streamed tap trace segment.
    socket_streamed_trace_segment: "SocketStreamedTraceSegment" = (
        betterproto.message_field(4, group="trace")
    )


from ....api.v2 import core as ___api_v2_core__
