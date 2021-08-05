# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/network/ext_authz/v4alpha/ext_authz.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ExtAuthz(betterproto.Message):
    """
    External Authorization filter calls out to an external service over the
    gRPC Authorization API defined by :ref:`CheckRequest
    <envoy_v3_api_msg_service.auth.v3.CheckRequest>`. A failed check will cause
    this filter to close the TCP connection. [#next-free-field: 8]
    """

    # The prefix to use when emitting statistics.
    stat_prefix: str = betterproto.string_field(1)
    # The external authorization gRPC service configuration. The default timeout
    # is set to 200ms by this filter.
    grpc_service: "_____config_core_v4_alpha__.GrpcService" = betterproto.message_field(
        2
    )
    # The filter's behaviour in case the external authorization service does not
    # respond back. When it is set to true, Envoy will also allow traffic in case
    # of communication failure between authorization service and the proxy.
    # Defaults to false.
    failure_mode_allow: bool = betterproto.bool_field(3)
    # Specifies if the peer certificate is sent to the external service. When
    # this field is true, Envoy will include the peer X.509 certificate, if
    # available, in the :ref:`certificate<envoy_v3_api_field_service.auth.v3.Attr
    # ibuteContext.Peer.certificate>`.
    include_peer_certificate: bool = betterproto.bool_field(4)
    # API version for ext_authz transport protocol. This describes the ext_authz
    # gRPC endpoint and version of Check{Request,Response} used on the wire.
    transport_api_version: "_____config_core_v4_alpha__.ApiVersion" = (
        betterproto.enum_field(5)
    )
    # Specifies if the filter is enabled with metadata matcher. If this field is
    # not specified, the filter will be enabled for all requests.
    filter_enabled_metadata: "_____type_matcher_v4_alpha__.MetadataMatcher" = (
        betterproto.message_field(6)
    )
    # Optional labels that will be passed to :ref:`labels<envoy_v3_api_field_serv
    # ice.auth.v3.AttributeContext.Peer.labels>` in :ref:`destination<envoy_v3_ap
    # i_field_service.auth.v3.AttributeContext.destination>`. The labels will be
    # read from :ref:`metadata<envoy_v3_api_msg_config.core.v3.Node>` with the
    # specified key.
    bootstrap_metadata_labels_key: str = betterproto.string_field(7)


from ......config.core import v4alpha as _____config_core_v4_alpha__
from ......type.matcher import v4alpha as _____type_matcher_v4_alpha__
