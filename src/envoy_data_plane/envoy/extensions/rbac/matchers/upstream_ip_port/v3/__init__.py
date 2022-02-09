# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/rbac/matchers/upstream_ip_port/v3/upstream_ip_port_matcher.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class UpstreamIpPortMatcher(betterproto.Message):
    """
    This is configuration for matching upstream ip and port. Note that although
    both fields are optional, at least one of IP or port must be supplied. If
    only one is supplied the other is a wildcard match. This matcher requires a
    filter in the chain to have saved the upstream address in the filter state
    before the matcher is executed by RBAC filter. The state should be saved
    with key `envoy.stream.upstream_address` (See
    :repo:`upstream_address.h<source/common/stream_info/upstream_address.h>`).
    Also, See :repo:`proxy_filter.cc<
    source/extensions/filters/http/dynamic_forward_proxy/proxy_filter.cc>` for
    an example of a filter which populates the FilterState.
    """

    # A CIDR block that will be used to match the upstream IP. Both Ipv4 and Ipv6
    # ranges can be matched.
    upstream_ip: "_____config_core_v3__.CidrRange" = betterproto.message_field(1)
    # A port range that will be used to match the upstream port.
    upstream_port_range: "_____type_v3__.Int64Range" = betterproto.message_field(2)


from ......config.core import v3 as _____config_core_v3__
from ......type import v3 as _____type_v3__
