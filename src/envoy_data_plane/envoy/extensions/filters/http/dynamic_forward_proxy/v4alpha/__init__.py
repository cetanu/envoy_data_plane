# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/dynamic_forward_proxy/v4alpha/dynamic_forward_proxy.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class FilterConfig(betterproto.Message):
    """
    Configuration for the dynamic forward proxy HTTP filter. See the
    :ref:`architecture overview <arch_overview_http_dynamic_forward_proxy>` for
    more information. [#extension: envoy.filters.http.dynamic_forward_proxy]
    """

    # The DNS cache configuration that the filter will attach to. Note this
    # configuration must match that of associated :ref:`dynamic forward proxy
    # cluster configuration <envoy_v3_api_field_extensions.clusters.dynamic_forwa
    # rd_proxy.v3.ClusterConfig.dns_cache_config>`.
    dns_cache_config: "____common_dynamic_forward_proxy_v4_alpha__.DnsCacheConfig" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class PerRouteConfig(betterproto.Message):
    """Per route Configuration for the dynamic forward proxy HTTP filter."""

    # Indicates that before DNS lookup, the host header will be swapped with this
    # value. If not set or empty, the original host header value will be used and
    # no rewrite will happen. Note: this rewrite affects both DNS lookup and host
    # header forwarding. However, this option shouldn't be used with :ref:`HCM
    # host rewrite
    # <envoy_v3_api_field_config.route.v3.RouteAction.host_rewrite_literal>`
    # given that the value set here would be used for DNS lookups whereas the
    # value set in the HCM would be used for host header forwarding which is not
    # the desired outcome.
    host_rewrite_literal: str = betterproto.string_field(
        1, group="host_rewrite_specifier"
    )
    # Indicates that before DNS lookup, the host header will be swapped with the
    # value of this header. If not set or empty, the original host header value
    # will be used and no rewrite will happen. Note: this rewrite affects both
    # DNS lookup and host header forwarding. However, this option shouldn't be
    # used with :ref:`HCM host rewrite header
    # <envoy_v3_api_field_config.route.v3.RouteAction.auto_host_rewrite>` given
    # that the value set here would be used for DNS lookups whereas the value set
    # in the HCM would be used for host header forwarding which is not the
    # desired outcome. .. note::   If the header appears multiple times only the
    # first value is used.
    host_rewrite_header: str = betterproto.string_field(
        2, group="host_rewrite_specifier"
    )


from .....common.dynamic_forward_proxy import (
    v4alpha as ____common_dynamic_forward_proxy_v4_alpha__,
)
