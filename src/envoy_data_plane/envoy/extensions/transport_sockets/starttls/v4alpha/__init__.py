# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/transport_sockets/starttls/v4alpha/starttls.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class StartTlsConfig(betterproto.Message):
    """
    Configuration for a downstream StartTls transport socket. StartTls
    transport socket wraps two sockets: * raw_buffer socket which is used at
    the beginning of the session * TLS socket used when a protocol negotiates a
    switch to encrypted traffic.
    """

    # (optional) Configuration for clear-text socket used at the beginning of the
    # session.
    cleartext_socket_config: "__raw_buffer_v3__.RawBuffer" = betterproto.message_field(
        1
    )
    # Configuration for a downstream TLS socket.
    tls_socket_config: "__tls_v4_alpha__.DownstreamTlsContext" = (
        betterproto.message_field(2)
    )


@dataclass(eq=False, repr=False)
class UpstreamStartTlsConfig(betterproto.Message):
    """
    Configuration for an upstream StartTls transport socket. StartTls transport
    socket wraps two sockets: * raw_buffer socket which is used at the
    beginning of the session * TLS socket used when a protocol negotiates a
    switch to encrypted traffic.
    """

    # (optional) Configuration for clear-text socket used at the beginning of the
    # session.
    cleartext_socket_config: "__raw_buffer_v3__.RawBuffer" = betterproto.message_field(
        1
    )
    # Configuration for an upstream TLS socket.
    tls_socket_config: "__tls_v4_alpha__.UpstreamTlsContext" = (
        betterproto.message_field(2)
    )


from ...raw_buffer import v3 as __raw_buffer_v3__
from ...tls import v4alpha as __tls_v4_alpha__
