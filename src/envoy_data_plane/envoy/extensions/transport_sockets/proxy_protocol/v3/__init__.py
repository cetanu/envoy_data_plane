# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/transport_sockets/proxy_protocol/v3/upstream_proxy_protocol.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ProxyProtocolUpstreamTransport(betterproto.Message):
    """Configuration for PROXY protocol socket"""

    # The PROXY protocol settings
    config: "____config_core_v3__.ProxyProtocolConfig" = betterproto.message_field(1)
    # The underlying transport socket being wrapped.
    transport_socket: "____config_core_v3__.TransportSocket" = (
        betterproto.message_field(2)
    )


from .....config.core import v3 as ____config_core_v3__