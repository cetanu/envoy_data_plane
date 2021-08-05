# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/router/v4alpha/router.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Router(betterproto.Message):
    """[#next-free-field: 7]"""

    # Whether the router generates dynamic cluster statistics. Defaults to true.
    # Can be disabled in high performance scenarios.
    dynamic_stats: Optional[bool] = betterproto.message_field(
        1, wraps=betterproto.TYPE_BOOL
    )
    # Whether to start a child span for egress routed calls. This can be useful
    # in scenarios where other filters (auth, ratelimit, etc.) make outbound
    # calls and have child spans rooted at the same ingress parent. Defaults to
    # false.
    start_child_span: bool = betterproto.bool_field(2)
    # Configuration for HTTP upstream logs emitted by the router. Upstream logs
    # are configured in the same way as access logs, but each log entry
    # represents an upstream request. Presuming retries are configured, multiple
    # upstream requests may be made for each downstream (inbound) request.
    upstream_log: List[
        "_____config_accesslog_v4_alpha__.AccessLog"
    ] = betterproto.message_field(3)
    # Do not add any additional *x-envoy-* headers to requests or responses. This
    # only affects the :ref:`router filter generated *x-envoy-* headers
    # <config_http_filters_router_headers_set>`, other Envoy filters and the HTTP
    # connection manager may continue to set *x-envoy-* headers.
    suppress_envoy_headers: bool = betterproto.bool_field(4)
    # Specifies a list of HTTP headers to strictly validate. Envoy will reject a
    # request and respond with HTTP status 400 if the request contains an invalid
    # value for any of the headers listed in this field. Strict header checking
    # is only supported for the following headers: Value must be a ','-delimited
    # list (i.e. no spaces) of supported retry policy values: *
    # :ref:`config_http_filters_router_x-envoy-retry-grpc-on` *
    # :ref:`config_http_filters_router_x-envoy-retry-on` Value must be an
    # integer: * :ref:`config_http_filters_router_x-envoy-max-retries` *
    # :ref:`config_http_filters_router_x-envoy-upstream-rq-timeout-ms` *
    # :ref:`config_http_filters_router_x-envoy-upstream-rq-per-try-timeout-ms`
    strict_check_headers: List[str] = betterproto.string_field(5)
    # If not set, ingress Envoy will ignore :ref:`config_http_filters_router_x-
    # envoy-expected-rq-timeout-ms` header, populated by egress Envoy, when
    # deriving timeout for upstream cluster.
    respect_expected_rq_timeout: bool = betterproto.bool_field(6)


from ......config.accesslog import v4alpha as _____config_accesslog_v4_alpha__