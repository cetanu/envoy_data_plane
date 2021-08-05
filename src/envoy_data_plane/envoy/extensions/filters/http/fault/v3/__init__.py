# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/fault/v3/fault.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class FaultAbort(betterproto.Message):
    """[#next-free-field: 6]"""

    # HTTP status code to use to abort the HTTP request.
    http_status: int = betterproto.uint32_field(2, group="error_type")
    # gRPC status code to use to abort the gRPC request.
    grpc_status: int = betterproto.uint32_field(5, group="error_type")
    # Fault aborts are controlled via an HTTP header (if applicable).
    header_abort: "FaultAbortHeaderAbort" = betterproto.message_field(
        4, group="error_type"
    )
    # The percentage of requests/operations/connections that will be aborted with
    # the error code provided.
    percentage: "_____type_v3__.FractionalPercent" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class FaultAbortHeaderAbort(betterproto.Message):
    """
    Fault aborts are controlled via an HTTP header (if applicable). See the
    :ref:`HTTP fault filter <config_http_filters_fault_injection_http_header>`
    documentation for more information.
    """

    pass


@dataclass(eq=False, repr=False)
class HttpFault(betterproto.Message):
    """[#next-free-field: 16]"""

    # If specified, the filter will inject delays based on the values in the
    # object.
    delay: "___common_fault_v3__.FaultDelay" = betterproto.message_field(1)
    # If specified, the filter will abort requests based on the values in the
    # object. At least *abort* or *delay* must be specified.
    abort: "FaultAbort" = betterproto.message_field(2)
    # Specifies the name of the (destination) upstream cluster that the filter
    # should match on. Fault injection will be restricted to requests bound to
    # the specific upstream cluster.
    upstream_cluster: str = betterproto.string_field(3)
    # Specifies a set of headers that the filter should match on. The fault
    # injection filter can be applied selectively to requests that match a set of
    # headers specified in the fault filter config. The chances of actual fault
    # injection further depend on the value of the :ref:`percentage <envoy_v3_api
    # _field_extensions.filters.http.fault.v3.FaultAbort.percentage>` field. The
    # filter will check the request's headers against all the specified headers
    # in the filter config. A match will happen if all the headers in the config
    # are present in the request with the same values (or based on presence if
    # the *value* field is not in the config).
    headers: List["_____config_route_v3__.HeaderMatcher"] = betterproto.message_field(4)
    # Faults are injected for the specified list of downstream hosts. If this
    # setting is not set, faults are injected for all downstream nodes.
    # Downstream node name is taken from :ref:`the HTTP x-envoy-downstream-
    # service-node <config_http_conn_man_headers_downstream-service-node>` header
    # and compared against downstream_nodes list.
    downstream_nodes: List[str] = betterproto.string_field(5)
    # The maximum number of faults that can be active at a single time via the
    # configured fault filter. Note that because this setting can be overridden
    # at the route level, it's possible for the number of active faults to be
    # greater than this value (if injected via a different route). If not
    # specified, defaults to unlimited. This setting can be overridden via
    # `runtime <config_http_filters_fault_injection_runtime>` and any faults that
    # are not injected due to overflow will be indicated via the `faults_overflow
    # <config_http_filters_fault_injection_stats>` stat. .. attention::   Like
    # other :ref:`circuit breakers <arch_overview_circuit_break>` in Envoy, this
    # is a fuzzy   limit. It's possible for the number of active faults to rise
    # slightly above the configured   amount due to the implementation details.
    max_active_faults: Optional[int] = betterproto.message_field(
        6, wraps=betterproto.TYPE_UINT32
    )
    # The response rate limit to be applied to the response body of the stream.
    # When configured, the percentage can be overridden by the
    # :ref:`fault.http.rate_limit.response_percent
    # <config_http_filters_fault_injection_runtime>` runtime key. .. attention::
    # This is a per-stream limit versus a connection level limit. This means that
    # concurrent streams  will each get an independent limit.
    response_rate_limit: "___common_fault_v3__.FaultRateLimit" = (
        betterproto.message_field(7)
    )
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.delay.fixed_delay_percent
    delay_percent_runtime: str = betterproto.string_field(8)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.abort.abort_percent
    abort_percent_runtime: str = betterproto.string_field(9)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.delay.fixed_duration_ms
    delay_duration_runtime: str = betterproto.string_field(10)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.abort.http_status
    abort_http_status_runtime: str = betterproto.string_field(11)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.max_active_faults
    max_active_faults_runtime: str = betterproto.string_field(12)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.rate_limit.response_percent
    response_rate_limit_percent_runtime: str = betterproto.string_field(13)
    # The runtime key to override the :ref:`default
    # <config_http_filters_fault_injection_runtime>` runtime. The default is:
    # fault.http.abort.grpc_status
    abort_grpc_status_runtime: str = betterproto.string_field(14)
    # To control whether stats storage is allocated dynamically for each
    # downstream server. If set to true, "x-envoy-downstream-service-cluster"
    # field of header will be ignored by this filter. If set to false, dynamic
    # stats storage will be allocated for the downstream cluster name. Default
    # value is false.
    disable_downstream_cluster_stats: bool = betterproto.bool_field(15)


from ......config.route import v3 as _____config_route_v3__
from ......type import v3 as _____type_v3__
from ....common.fault import v3 as ___common_fault_v3__
