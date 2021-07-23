# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/data/accesslog/v2/accesslog.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class HttpAccessLogEntryHttpVersion(betterproto.Enum):
    PROTOCOL_UNSPECIFIED = 0
    HTTP10 = 1
    HTTP11 = 2
    HTTP2 = 3
    HTTP3 = 4


class ResponseFlagsUnauthorizedReason(betterproto.Enum):
    REASON_UNSPECIFIED = 0
    EXTERNAL_SERVICE = 1


class TlsPropertiesTlsVersion(betterproto.Enum):
    VERSION_UNSPECIFIED = 0
    TLSv1 = 1
    TLSv1_1 = 2
    TLSv1_2 = 3
    TLSv1_3 = 4


@dataclass(eq=False, repr=False)
class TcpAccessLogEntry(betterproto.Message):
    # Common properties shared by all Envoy access logs.
    common_properties: "AccessLogCommon" = betterproto.message_field(1)
    # Properties of the TCP connection.
    connection_properties: "ConnectionProperties" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class HttpAccessLogEntry(betterproto.Message):
    # Common properties shared by all Envoy access logs.
    common_properties: "AccessLogCommon" = betterproto.message_field(1)
    protocol_version: "HttpAccessLogEntryHttpVersion" = betterproto.enum_field(2)
    # Description of the incoming HTTP request.
    request: "HttpRequestProperties" = betterproto.message_field(3)
    # Description of the outgoing HTTP response.
    response: "HttpResponseProperties" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ConnectionProperties(betterproto.Message):
    """Defines fields for a connection"""

    # Number of bytes received from downstream.
    received_bytes: int = betterproto.uint64_field(1)
    # Number of bytes sent to downstream.
    sent_bytes: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class AccessLogCommon(betterproto.Message):
    """
    Defines fields that are shared by all Envoy access logs. [#next-free-field:
    22]
    """

    # [#not-implemented-hide:] This field indicates the rate at which this log
    # entry was sampled. Valid range is (0.0, 1.0].
    sample_rate: float = betterproto.double_field(1)
    # This field is the remote/origin address on which the request from the user
    # was received. Note: This may not be the physical peer. E.g, if the remote
    # address is inferred from for example the x-forwarder-for header, proxy
    # protocol, etc.
    downstream_remote_address: "___api_v2_core__.Address" = betterproto.message_field(2)
    # This field is the local/destination address on which the request from the
    # user was received.
    downstream_local_address: "___api_v2_core__.Address" = betterproto.message_field(3)
    # If the connection is secure,S this field will contain TLS properties.
    tls_properties: "TlsProperties" = betterproto.message_field(4)
    # The time that Envoy started servicing this request. This is effectively the
    # time that the first downstream byte is received.
    start_time: datetime = betterproto.message_field(5)
    # Interval between the first downstream byte received and the last downstream
    # byte received (i.e. time it takes to receive a request).
    time_to_last_rx_byte: timedelta = betterproto.message_field(6)
    # Interval between the first downstream byte received and the first upstream
    # byte sent. There may by considerable delta between *time_to_last_rx_byte*
    # and this value due to filters. Additionally, the same caveats apply as
    # documented in *time_to_last_downstream_tx_byte* about not accounting for
    # kernel socket buffer time, etc.
    time_to_first_upstream_tx_byte: timedelta = betterproto.message_field(7)
    # Interval between the first downstream byte received and the last upstream
    # byte sent. There may by considerable delta between *time_to_last_rx_byte*
    # and this value due to filters. Additionally, the same caveats apply as
    # documented in *time_to_last_downstream_tx_byte* about not accounting for
    # kernel socket buffer time, etc.
    time_to_last_upstream_tx_byte: timedelta = betterproto.message_field(8)
    # Interval between the first downstream byte received and the first upstream
    # byte received (i.e. time it takes to start receiving a response).
    time_to_first_upstream_rx_byte: timedelta = betterproto.message_field(9)
    # Interval between the first downstream byte received and the last upstream
    # byte received (i.e. time it takes to receive a complete response).
    time_to_last_upstream_rx_byte: timedelta = betterproto.message_field(10)
    # Interval between the first downstream byte received and the first
    # downstream byte sent. There may be a considerable delta between the
    # *time_to_first_upstream_rx_byte* and this field due to filters.
    # Additionally, the same caveats apply as documented in
    # *time_to_last_downstream_tx_byte* about not accounting for kernel socket
    # buffer time, etc.
    time_to_first_downstream_tx_byte: timedelta = betterproto.message_field(11)
    # Interval between the first downstream byte received and the last downstream
    # byte sent. Depending on protocol, buffering, windowing, filters, etc. there
    # may be a considerable delta between *time_to_last_upstream_rx_byte* and
    # this field. Note also that this is an approximate time. In the current
    # implementation it does not include kernel socket buffer time. In the
    # current implementation it also does not include send window buffering
    # inside the HTTP/2 codec. In the future it is likely that work will be done
    # to make this duration more accurate.
    time_to_last_downstream_tx_byte: timedelta = betterproto.message_field(12)
    # The upstream remote/destination address that handles this exchange. This
    # does not include retries.
    upstream_remote_address: "___api_v2_core__.Address" = betterproto.message_field(13)
    # The upstream local/origin address that handles this exchange. This does not
    # include retries.
    upstream_local_address: "___api_v2_core__.Address" = betterproto.message_field(14)
    # The upstream cluster that *upstream_remote_address* belongs to.
    upstream_cluster: str = betterproto.string_field(15)
    # Flags indicating occurrences during request/response processing.
    response_flags: "ResponseFlags" = betterproto.message_field(16)
    # All metadata encountered during request processing, including endpoint
    # selection. This can be used to associate IDs attached to the various
    # configurations used to process this request with the access log entry. For
    # example, a route created from a higher level forwarding rule with some ID
    # can place that ID in this field and cross reference later. It can also be
    # used to determine if a canary endpoint was used or not.
    metadata: "___api_v2_core__.Metadata" = betterproto.message_field(17)
    # If upstream connection failed due to transport socket (e.g. TLS handshake),
    # provides the failure reason from the transport socket. The format of this
    # field depends on the configured upstream transport socket. Common TLS
    # failures are in :ref:`TLS trouble shooting
    # <arch_overview_ssl_trouble_shooting>`.
    upstream_transport_failure_reason: str = betterproto.string_field(18)
    # The name of the route
    route_name: str = betterproto.string_field(19)
    # This field is the downstream direct remote address on which the request
    # from the user was received. Note: This is always the physical peer, even if
    # the remote address is inferred from for example the x-forwarder-for header,
    # proxy protocol, etc.
    downstream_direct_remote_address: "___api_v2_core__.Address" = (
        betterproto.message_field(20)
    )
    # Map of filter state in stream info that have been configured to be logged.
    # If the filter state serialized to any message other than
    # `google.protobuf.Any` it will be packed into `google.protobuf.Any`.
    filter_state_objects: Dict[
        str, "betterproto_lib_google_protobuf.Any"
    ] = betterproto.map_field(21, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE)


@dataclass(eq=False, repr=False)
class ResponseFlags(betterproto.Message):
    """
    Flags indicating occurrences during request/response processing. [#next-
    free-field: 20]
    """

    # Indicates local server healthcheck failed.
    failed_local_healthcheck: bool = betterproto.bool_field(1)
    # Indicates there was no healthy upstream.
    no_healthy_upstream: bool = betterproto.bool_field(2)
    # Indicates an there was an upstream request timeout.
    upstream_request_timeout: bool = betterproto.bool_field(3)
    # Indicates local codec level reset was sent on the stream.
    local_reset: bool = betterproto.bool_field(4)
    # Indicates remote codec level reset was received on the stream.
    upstream_remote_reset: bool = betterproto.bool_field(5)
    # Indicates there was a local reset by a connection pool due to an initial
    # connection failure.
    upstream_connection_failure: bool = betterproto.bool_field(6)
    # Indicates the stream was reset due to an upstream connection termination.
    upstream_connection_termination: bool = betterproto.bool_field(7)
    # Indicates the stream was reset because of a resource overflow.
    upstream_overflow: bool = betterproto.bool_field(8)
    # Indicates no route was found for the request.
    no_route_found: bool = betterproto.bool_field(9)
    # Indicates that the request was delayed before proxying.
    delay_injected: bool = betterproto.bool_field(10)
    # Indicates that the request was aborted with an injected error code.
    fault_injected: bool = betterproto.bool_field(11)
    # Indicates that the request was rate-limited locally.
    rate_limited: bool = betterproto.bool_field(12)
    # Indicates if the request was deemed unauthorized and the reason for it.
    unauthorized_details: "ResponseFlagsUnauthorized" = betterproto.message_field(13)
    # Indicates that the request was rejected because there was an error in rate
    # limit service.
    rate_limit_service_error: bool = betterproto.bool_field(14)
    # Indicates the stream was reset due to a downstream connection termination.
    downstream_connection_termination: bool = betterproto.bool_field(15)
    # Indicates that the upstream retry limit was exceeded, resulting in a
    # downstream error.
    upstream_retry_limit_exceeded: bool = betterproto.bool_field(16)
    # Indicates that the stream idle timeout was hit, resulting in a downstream
    # 408.
    stream_idle_timeout: bool = betterproto.bool_field(17)
    # Indicates that the request was rejected because an envoy request header
    # failed strict validation.
    invalid_envoy_request_headers: bool = betterproto.bool_field(18)
    # Indicates there was an HTTP protocol error on the downstream request.
    downstream_protocol_error: bool = betterproto.bool_field(19)


@dataclass(eq=False, repr=False)
class ResponseFlagsUnauthorized(betterproto.Message):
    reason: "ResponseFlagsUnauthorizedReason" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class TlsProperties(betterproto.Message):
    """Properties of a negotiated TLS connection. [#next-free-field: 7]"""

    # Version of TLS that was negotiated.
    tls_version: "TlsPropertiesTlsVersion" = betterproto.enum_field(1)
    # TLS cipher suite negotiated during handshake. The value is a four-digit hex
    # code defined by the IANA TLS Cipher Suite Registry (e.g. ``009C`` for
    # ``TLS_RSA_WITH_AES_128_GCM_SHA256``). Here it is expressed as an integer.
    tls_cipher_suite: Optional[int] = betterproto.message_field(
        2, wraps=betterproto.TYPE_UINT32
    )
    # SNI hostname from handshake.
    tls_sni_hostname: str = betterproto.string_field(3)
    # Properties of the local certificate used to negotiate TLS.
    local_certificate_properties: "TlsPropertiesCertificateProperties" = (
        betterproto.message_field(4)
    )
    # Properties of the peer certificate used to negotiate TLS.
    peer_certificate_properties: "TlsPropertiesCertificateProperties" = (
        betterproto.message_field(5)
    )
    # The TLS session ID.
    tls_session_id: str = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class TlsPropertiesCertificateProperties(betterproto.Message):
    # SANs present in the certificate.
    subject_alt_name: List[
        "TlsPropertiesCertificatePropertiesSubjectAltName"
    ] = betterproto.message_field(1)
    # The subject field of the certificate.
    subject: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class TlsPropertiesCertificatePropertiesSubjectAltName(betterproto.Message):
    uri: str = betterproto.string_field(1, group="san")
    # [#not-implemented-hide:]
    dns: str = betterproto.string_field(2, group="san")


@dataclass(eq=False, repr=False)
class HttpRequestProperties(betterproto.Message):
    """[#next-free-field: 14]"""

    # The request method (RFC 7231/2616).
    request_method: "___api_v2_core__.RequestMethod" = betterproto.enum_field(1)
    # The scheme portion of the incoming request URI.
    scheme: str = betterproto.string_field(2)
    # HTTP/2 ``:authority`` or HTTP/1.1 ``Host`` header value.
    authority: str = betterproto.string_field(3)
    # The port of the incoming request URI (unused currently, as port is composed
    # onto authority).
    port: Optional[int] = betterproto.message_field(4, wraps=betterproto.TYPE_UINT32)
    # The path portion from the incoming request URI.
    path: str = betterproto.string_field(5)
    # Value of the ``User-Agent`` request header.
    user_agent: str = betterproto.string_field(6)
    # Value of the ``Referer`` request header.
    referer: str = betterproto.string_field(7)
    # Value of the ``X-Forwarded-For`` request header.
    forwarded_for: str = betterproto.string_field(8)
    # Value of the ``X-Request-Id`` request header This header is used by Envoy
    # to uniquely identify a request. It will be generated for all external
    # requests and internal requests that do not already have a request ID.
    request_id: str = betterproto.string_field(9)
    # Value of the ``X-Envoy-Original-Path`` request header.
    original_path: str = betterproto.string_field(10)
    # Size of the HTTP request headers in bytes. This value is captured from the
    # OSI layer 7 perspective, i.e. it does not include overhead from framing or
    # encoding at other networking layers.
    request_headers_bytes: int = betterproto.uint64_field(11)
    # Size of the HTTP request body in bytes. This value is captured from the OSI
    # layer 7 perspective, i.e. it does not include overhead from framing or
    # encoding at other networking layers.
    request_body_bytes: int = betterproto.uint64_field(12)
    # Map of additional headers that have been configured to be logged.
    request_headers: Dict[str, str] = betterproto.map_field(
        13, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class HttpResponseProperties(betterproto.Message):
    """[#next-free-field: 7]"""

    # The HTTP response code returned by Envoy.
    response_code: Optional[int] = betterproto.message_field(
        1, wraps=betterproto.TYPE_UINT32
    )
    # Size of the HTTP response headers in bytes. This value is captured from the
    # OSI layer 7 perspective, i.e. it does not include overhead from framing or
    # encoding at other networking layers.
    response_headers_bytes: int = betterproto.uint64_field(2)
    # Size of the HTTP response body in bytes. This value is captured from the
    # OSI layer 7 perspective, i.e. it does not include overhead from framing or
    # encoding at other networking layers.
    response_body_bytes: int = betterproto.uint64_field(3)
    # Map of additional headers configured to be logged.
    response_headers: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    # Map of trailers configured to be logged.
    response_trailers: Dict[str, str] = betterproto.map_field(
        5, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    # The HTTP response code details.
    response_code_details: str = betterproto.string_field(6)


from ....api.v2 import core as ___api_v2_core__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
