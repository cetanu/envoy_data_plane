# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/clusters/dynamic_forward_proxy/v4alpha/cluster.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ClusterConfig(betterproto.Message):
    """
    Configuration for the dynamic forward proxy cluster. See the
    :ref:`architecture overview <arch_overview_http_dynamic_forward_proxy>` for
    more information. [#extension: envoy.clusters.dynamic_forward_proxy]
    """

    # The DNS cache configuration that the cluster will attach to. Note this
    # configuration must match that of associated :ref:`dynamic forward proxy
    # HTTP filter configuration <envoy_v3_api_field_extensions.filters.http.dynam
    # ic_forward_proxy.v3.FilterConfig.dns_cache_config>`.
    dns_cache_config: "___common_dynamic_forward_proxy_v4_alpha__.DnsCacheConfig" = (
        betterproto.message_field(1)
    )
    # If true allow the cluster configuration to disable the auto_sni and
    # auto_san_validation options in the :ref:`cluster's
    # upstream_http_protocol_options <envoy_v3_api_field_config.cluster.v3.Cluste
    # r.upstream_http_protocol_options>`
    allow_insecure_cluster_options: bool = betterproto.bool_field(2)


from ....common.dynamic_forward_proxy import (
    v4alpha as ___common_dynamic_forward_proxy_v4_alpha__,
)
