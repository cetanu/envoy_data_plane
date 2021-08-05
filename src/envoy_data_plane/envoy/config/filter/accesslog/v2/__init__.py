# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/accesslog/v2/accesslog.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class ComparisonFilterOp(betterproto.Enum):
    EQ = 0
    GE = 1
    LE = 2


class GrpcStatusFilterStatus(betterproto.Enum):
    OK = 0
    CANCELED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    RESOURCE_EXHAUSTED = 8
    FAILED_PRECONDITION = 9
    ABORTED = 10
    OUT_OF_RANGE = 11
    UNIMPLEMENTED = 12
    INTERNAL = 13
    UNAVAILABLE = 14
    DATA_LOSS = 15
    UNAUTHENTICATED = 16


@dataclass(eq=False, repr=False)
class AccessLog(betterproto.Message):
    # The name of the access log implementation to instantiate. The name must
    # match a statically registered access log. Current built-in loggers include:
    # #. "envoy.access_loggers.file" #. "envoy.access_loggers.http_grpc" #.
    # "envoy.access_loggers.tcp_grpc"
    name: str = betterproto.string_field(1)
    # Filter which is used to determine if the access log needs to be written.
    filter: "AccessLogFilter" = betterproto.message_field(2)
    config: "betterproto_lib_google_protobuf.Struct" = betterproto.message_field(
        3, group="config_type"
    )
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        4, group="config_type"
    )

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.config:
            warnings.warn("AccessLog.config is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class AccessLogFilter(betterproto.Message):
    """[#next-free-field: 12]"""

    # Status code filter.
    status_code_filter: "StatusCodeFilter" = betterproto.message_field(
        1, group="filter_specifier"
    )
    # Duration filter.
    duration_filter: "DurationFilter" = betterproto.message_field(
        2, group="filter_specifier"
    )
    # Not health check filter.
    not_health_check_filter: "NotHealthCheckFilter" = betterproto.message_field(
        3, group="filter_specifier"
    )
    # Traceable filter.
    traceable_filter: "TraceableFilter" = betterproto.message_field(
        4, group="filter_specifier"
    )
    # Runtime filter.
    runtime_filter: "RuntimeFilter" = betterproto.message_field(
        5, group="filter_specifier"
    )
    # And filter.
    and_filter: "AndFilter" = betterproto.message_field(6, group="filter_specifier")
    # Or filter.
    or_filter: "OrFilter" = betterproto.message_field(7, group="filter_specifier")
    # Header filter.
    header_filter: "HeaderFilter" = betterproto.message_field(
        8, group="filter_specifier"
    )
    # Response flag filter.
    response_flag_filter: "ResponseFlagFilter" = betterproto.message_field(
        9, group="filter_specifier"
    )
    # gRPC status filter.
    grpc_status_filter: "GrpcStatusFilter" = betterproto.message_field(
        10, group="filter_specifier"
    )
    # Extension filter.
    extension_filter: "ExtensionFilter" = betterproto.message_field(
        11, group="filter_specifier"
    )


@dataclass(eq=False, repr=False)
class ComparisonFilter(betterproto.Message):
    """Filter on an integer comparison."""

    # Comparison operator.
    op: "ComparisonFilterOp" = betterproto.enum_field(1)
    # Value to compare against.
    value: "____api_v2_core__.RuntimeUInt32" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class StatusCodeFilter(betterproto.Message):
    """Filters on HTTP response/status code."""

    # Comparison.
    comparison: "ComparisonFilter" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DurationFilter(betterproto.Message):
    """Filters on total request duration in milliseconds."""

    # Comparison.
    comparison: "ComparisonFilter" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class NotHealthCheckFilter(betterproto.Message):
    """
    Filters for requests that are not health check requests. A health check
    request is marked by the health check filter.
    """

    pass


@dataclass(eq=False, repr=False)
class TraceableFilter(betterproto.Message):
    """
    Filters for requests that are traceable. See the tracing overview for more
    information on how a request becomes traceable.
    """

    pass


@dataclass(eq=False, repr=False)
class RuntimeFilter(betterproto.Message):
    """Filters for random sampling of requests."""

    # Runtime key to get an optional overridden numerator for use in the
    # *percent_sampled* field. If found in runtime, this value will replace the
    # default numerator.
    runtime_key: str = betterproto.string_field(1)
    # The default sampling percentage. If not specified, defaults to 0% with
    # denominator of 100.
    percent_sampled: "____type__.FractionalPercent" = betterproto.message_field(2)
    # By default, sampling pivots on the header :ref:`x-request-
    # id<config_http_conn_man_headers_x-request-id>` being present. If
    # :ref:`x-request-id<config_http_conn_man_headers_x-request-id>` is present,
    # the filter will consistently sample across multiple hosts based on the
    # runtime key value and the value extracted from :ref:`x-request-
    # id<config_http_conn_man_headers_x-request-id>`. If it is missing, or
    # *use_independent_randomness* is set to true, the filter will randomly
    # sample based on the runtime key value alone. *use_independent_randomness*
    # can be used for logging kill switches within complex nested :ref:`AndFilter
    # <envoy_api_msg_config.filter.accesslog.v2.AndFilter>` and :ref:`OrFilter
    # <envoy_api_msg_config.filter.accesslog.v2.OrFilter>` blocks that are easier
    # to reason about from a probability perspective (i.e., setting to true will
    # cause the filter to behave like an independent random variable when
    # composed within logical operator filters).
    use_independent_randomness: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class AndFilter(betterproto.Message):
    """
    Performs a logical “and” operation on the result of each filter in filters.
    Filters are evaluated sequentially and if one of them returns false, the
    filter returns false immediately.
    """

    filters: List["AccessLogFilter"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class OrFilter(betterproto.Message):
    """
    Performs a logical “or” operation on the result of each individual filter.
    Filters are evaluated sequentially and if one of them returns true, the
    filter returns true immediately.
    """

    filters: List["AccessLogFilter"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class HeaderFilter(betterproto.Message):
    """Filters requests based on the presence or value of a request header."""

    # Only requests with a header which matches the specified HeaderMatcher will
    # pass the filter check.
    header: "____api_v2_route__.HeaderMatcher" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ResponseFlagFilter(betterproto.Message):
    """
    Filters requests that received responses with an Envoy response flag set. A
    list of the response flags can be found in the access log formatter
    :ref:`documentation<config_access_log_format_response_flags>`.
    """

    # Only responses with the any of the flags listed in this field will be
    # logged. This field is optional. If it is not specified, then any response
    # flag will pass the filter check.
    flags: List[str] = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class GrpcStatusFilter(betterproto.Message):
    """
    Filters gRPC requests based on their response status. If a gRPC status is
    not provided, the filter will infer the status from the HTTP status code.
    """

    # Logs only responses that have any one of the gRPC statuses in this field.
    statuses: List["GrpcStatusFilterStatus"] = betterproto.enum_field(1)
    # If included and set to true, the filter will instead block all responses
    # with a gRPC status or inferred gRPC status enumerated in statuses, and
    # allow all other responses.
    exclude: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class ExtensionFilter(betterproto.Message):
    """Extension filter is statically registered at runtime."""

    # The name of the filter implementation to instantiate. The name must match a
    # statically registered filter.
    name: str = betterproto.string_field(1)
    config: "betterproto_lib_google_protobuf.Struct" = betterproto.message_field(
        2, group="config_type"
    )
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3, group="config_type"
    )

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.config:
            warnings.warn("ExtensionFilter.config is deprecated", DeprecationWarning)


from ..... import type as ____type__
from .....api.v2 import core as ____api_v2_core__
from .....api.v2 import route as ____api_v2_route__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf