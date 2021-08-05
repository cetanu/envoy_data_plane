# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/network/tcp_proxy/v4alpha/tcp_proxy.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class TcpProxy(betterproto.Message):
    """[#next-free-field: 14]"""

    # The prefix to use when emitting :ref:`statistics
    # <config_network_filters_tcp_proxy_stats>`.
    stat_prefix: str = betterproto.string_field(1)
    # The upstream cluster to connect to.
    cluster: str = betterproto.string_field(2, group="cluster_specifier")
    # Multiple upstream clusters can be specified for a given route. The request
    # is routed to one of the upstream clusters based on weights assigned to each
    # cluster.
    weighted_clusters: "TcpProxyWeightedCluster" = betterproto.message_field(
        10, group="cluster_specifier"
    )
    # Optional endpoint metadata match criteria. Only endpoints in the upstream
    # cluster with metadata matching that set in metadata_match will be
    # considered. The filter name should be specified as *envoy.lb*.
    metadata_match: "_____config_core_v4_alpha__.Metadata" = betterproto.message_field(
        9
    )
    # The idle timeout for connections managed by the TCP proxy filter. The idle
    # timeout is defined as the period in which there are no bytes sent or
    # received on either the upstream or downstream connection. If not set, the
    # default idle timeout is 1 hour. If set to 0s, the timeout will be disabled.
    # .. warning::   Disabling this timeout has a highly likelihood of yielding
    # connection leaks due to lost TCP   FIN packets, etc.
    idle_timeout: timedelta = betterproto.message_field(8)
    # [#not-implemented-hide:] The idle timeout for connections managed by the
    # TCP proxy filter. The idle timeout is defined as the period in which there
    # is no active traffic. If not set, there is no idle timeout. When the idle
    # timeout is reached the connection will be closed. The distinction between
    # downstream_idle_timeout/upstream_idle_timeout provides a means to set
    # timeout based on the last byte sent on the downstream/upstream connection.
    downstream_idle_timeout: timedelta = betterproto.message_field(3)
    # [#not-implemented-hide:]
    upstream_idle_timeout: timedelta = betterproto.message_field(4)
    # Configuration for :ref:`access logs <arch_overview_access_logs>` emitted by
    # the this tcp_proxy.
    access_log: List[
        "_____config_accesslog_v4_alpha__.AccessLog"
    ] = betterproto.message_field(5)
    # The maximum number of unsuccessful connection attempts that will be made
    # before giving up. If the parameter is not specified, 1 connection attempt
    # will be made.
    max_connect_attempts: Optional[int] = betterproto.message_field(
        7, wraps=betterproto.TYPE_UINT32
    )
    # Optional configuration for TCP proxy hash policy. If hash_policy is not
    # set, the hash-based load balancing algorithms will select a host randomly.
    # Currently the number of hash policies is limited to 1.
    hash_policy: List["_____type_v3__.HashPolicy"] = betterproto.message_field(11)
    # If set, this configures tunneling, e.g. configuration options to tunnel TCP
    # payload over HTTP CONNECT. If this message is absent, the payload will be
    # proxied upstream as per usual.
    tunneling_config: "TcpProxyTunnelingConfig" = betterproto.message_field(12)
    # The maximum duration of a connection. The duration is defined as the period
    # since a connection was established. If not set, there is no max duration.
    # When max_downstream_connection_duration is reached the connection will be
    # closed. Duration must be at least 1ms.
    max_downstream_connection_duration: timedelta = betterproto.message_field(13)


@dataclass(eq=False, repr=False)
class TcpProxyWeightedCluster(betterproto.Message):
    """
    Allows for specification of multiple upstream clusters along with weights
    that indicate the percentage of traffic to be forwarded to each cluster.
    The router selects an upstream cluster based on these weights.
    """

    # Specifies one or more upstream clusters associated with the route.
    clusters: List["TcpProxyWeightedClusterClusterWeight"] = betterproto.message_field(
        1
    )


@dataclass(eq=False, repr=False)
class TcpProxyWeightedClusterClusterWeight(betterproto.Message):
    # Name of the upstream cluster.
    name: str = betterproto.string_field(1)
    # When a request matches the route, the choice of an upstream cluster is
    # determined by its weight. The sum of weights across all entries in the
    # clusters array determines the total weight.
    weight: int = betterproto.uint32_field(2)
    # Optional endpoint metadata match criteria used by the subset load balancer.
    # Only endpoints in the upstream cluster with metadata matching what is set
    # in this field will be considered for load balancing. Note that this will be
    # merged with what's provided in :ref:`TcpProxy.metadata_match <envoy_v3_api_
    # field_extensions.filters.network.tcp_proxy.v3.TcpProxy.metadata_match>`,
    # with values here taking precedence. The filter name should be specified as
    # *envoy.lb*.
    metadata_match: "_____config_core_v4_alpha__.Metadata" = betterproto.message_field(
        3
    )


@dataclass(eq=False, repr=False)
class TcpProxyTunnelingConfig(betterproto.Message):
    """
    Configuration for tunneling TCP over other transports or application
    layers. Tunneling is supported over both HTTP/1.1 and HTTP/2. Upstream
    protocol is determined by the cluster configuration.
    """

    # The hostname to send in the synthesized CONNECT headers to the upstream
    # proxy.
    hostname: str = betterproto.string_field(1)
    # Use POST method instead of CONNECT method to tunnel the TCP stream. The
    # 'protocol: bytestream' header is also NOT set for HTTP/2 to comply with the
    # spec. The upstream proxy is expected to convert POST payload as raw TCP.
    use_post: bool = betterproto.bool_field(2)
    # Additional request headers to upstream proxy. This is mainly used to
    # trigger upstream to convert POST requests back to CONNECT requests. Neither
    # *:-prefixed* pseudo-headers nor the Host: header can be overridden.
    headers_to_add: List[
        "_____config_core_v4_alpha__.HeaderValueOption"
    ] = betterproto.message_field(3)


from ......config.accesslog import v4alpha as _____config_accesslog_v4_alpha__
from ......config.core import v4alpha as _____config_core_v4_alpha__
from ......type import v3 as _____type_v3__
