# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/upstreams/http/v4alpha/http_protocol_options.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class HttpProtocolOptions(betterproto.Message):
    """
    HttpProtocolOptions specifies Http upstream protocol options. This object
    is used in :ref:`typed_extension_protocol_options<envoy_v3_api_field_config
    .cluster.v3.Cluster.typed_extension_protocol_options>`, keyed by the name
    `envoy.extensions.upstreams.http.v3.HttpProtocolOptions`. This controls
    what protocol(s) should be used for upstream and how said protocol(s) are
    configured. This replaces the prior pattern of explicit protocol
    configuration directly in the cluster. So a configuration like this,
    explicitly configuring the use of HTTP/2 upstream: .. code::   clusters:
    - name: some_service       connect_timeout: 5s
    upstream_http_protocol_options:         auto_sni: true
    common_http_protocol_options:         idle_timeout: 1s
    http2_protocol_options:         max_concurrent_streams: 100        ....
    [further cluster config] Would now look like this: .. code::   clusters:
    - name: some_service       connect_timeout: 5s
    typed_extension_protocol_options:
    envoy.extensions.upstreams.http.v3.HttpProtocolOptions:           "@type":
    type.googleapis.com/envoy.extensions.upstreams.http.v3.HttpProtocolOptions
    upstream_http_protocol_options:             auto_sni: true
    common_http_protocol_options:             idle_timeout: 1s
    explicit_http_config:             http2_protocol_options:
    max_concurrent_streams: 100        .... [further cluster config] [#next-
    free-field: 6]
    """

    # This contains options common across HTTP/1 and HTTP/2
    common_http_protocol_options: "____config_core_v4_alpha__.HttpProtocolOptions" = (
        betterproto.message_field(1)
    )
    # This contains common protocol options which are only applied upstream.
    upstream_http_protocol_options: "____config_core_v4_alpha__.UpstreamHttpProtocolOptions" = betterproto.message_field(
        2
    )
    # To explicitly configure either HTTP/1 or HTTP/2 (but not both!) use
    # *explicit_http_config*. If the *explicit_http_config* is empty, HTTP/1.1 is
    # used.
    explicit_http_config: "HttpProtocolOptionsExplicitHttpConfig" = (
        betterproto.message_field(3, group="upstream_protocol_options")
    )
    # This allows switching on protocol based on what protocol the downstream
    # connection used.
    use_downstream_protocol_config: "HttpProtocolOptionsUseDownstreamHttpConfig" = (
        betterproto.message_field(4, group="upstream_protocol_options")
    )
    # This allows switching on protocol based on ALPN
    auto_config: "HttpProtocolOptionsAutoHttpConfig" = betterproto.message_field(
        5, group="upstream_protocol_options"
    )


@dataclass(eq=False, repr=False)
class HttpProtocolOptionsExplicitHttpConfig(betterproto.Message):
    """
    If this is used, the cluster will only operate on one of the possible
    upstream protocols. Note that HTTP/2 or above should generally be used for
    upstream gRPC clusters.
    """

    http_protocol_options: "____config_core_v4_alpha__.Http1ProtocolOptions" = (
        betterproto.message_field(1, group="protocol_config")
    )
    http2_protocol_options: "____config_core_v4_alpha__.Http2ProtocolOptions" = (
        betterproto.message_field(2, group="protocol_config")
    )
    # .. warning::   QUIC support is currently alpha and should be used with
    # caution. Please   see :ref:`here <arch_overview_http3>` for details.
    http3_protocol_options: "____config_core_v4_alpha__.Http3ProtocolOptions" = (
        betterproto.message_field(3, group="protocol_config")
    )


@dataclass(eq=False, repr=False)
class HttpProtocolOptionsUseDownstreamHttpConfig(betterproto.Message):
    """
    If this is used, the cluster can use either of the configured protocols,
    and will use whichever protocol was used by the downstream connection.
    """

    http_protocol_options: "____config_core_v4_alpha__.Http1ProtocolOptions" = (
        betterproto.message_field(1)
    )
    http2_protocol_options: "____config_core_v4_alpha__.Http2ProtocolOptions" = (
        betterproto.message_field(2)
    )
    # .. warning::   QUIC support is currently alpha and should be used with
    # caution. Please   see :ref:`here <arch_overview_http3>` for details.
    http3_protocol_options: "____config_core_v4_alpha__.Http3ProtocolOptions" = (
        betterproto.message_field(3)
    )


@dataclass(eq=False, repr=False)
class HttpProtocolOptionsAutoHttpConfig(betterproto.Message):
    """
    If this is used, the cluster can use either HTTP/1 or HTTP/2, and will use
    whichever protocol is negotiated by ALPN with the upstream. Clusters
    configured with *AutoHttpConfig* will use the highest available protocol;
    HTTP/2 if supported, otherwise HTTP/1. If the upstream does not support
    ALPN, *AutoHttpConfig* will fail over to HTTP/1. This can only be used with
    transport sockets which support ALPN. Using a transport socket which does
    not support ALPN will result in configuration failure. The transport layer
    may be configured with custom ALPN, but the default ALPN for the cluster
    (or if custom ALPN fails) will be "h2,http/1.1".
    """

    http_protocol_options: "____config_core_v4_alpha__.Http1ProtocolOptions" = (
        betterproto.message_field(1)
    )
    http2_protocol_options: "____config_core_v4_alpha__.Http2ProtocolOptions" = (
        betterproto.message_field(2)
    )
    # Unlike HTTP/1 and HTTP/2, HTTP/3 will not be configured unless it is
    # present, and (soon) only if there is an indication of server side support.
    # See :ref:`here <arch_overview_http3_upstream>` for more information on when
    # HTTP/3 will be used, and when Envoy will fail over to TCP. .. warning::
    # QUIC support is currently alpha and should be used with caution. Please
    # see :ref:`here <arch_overview_http3>` for details.   AutoHttpConfig config
    # is undergoing especially rapid change and as it   is alpha is not
    # guaranteed to be API-stable.
    http3_protocol_options: "____config_core_v4_alpha__.Http3ProtocolOptions" = (
        betterproto.message_field(3)
    )
    # [#not-implemented-hide:] The presence of alternate protocols cache options
    # causes the use of the alternate protocols cache, which is responsible for
    # parsing and caching HTTP Alt-Svc headers. This enables the use of HTTP/3
    # for origins that advertise supporting it. TODO(RyanTheOptimist): Make this
    # field required when HTTP/3 is enabled.
    alternate_protocols_cache_options: "____config_core_v4_alpha__.AlternateProtocolsCacheOptions" = betterproto.message_field(
        4
    )


from .....config.core import v4alpha as ____config_core_v4_alpha__
