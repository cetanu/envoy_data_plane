# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/tracers/skywalking/v4alpha/skywalking.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class SkyWalkingConfig(betterproto.Message):
    """
    Configuration for the SkyWalking tracer. Please note that if SkyWalking
    tracer is used as the provider of http tracer, then :ref:`start_child_span
    <envoy_v3_api_field_extensions.filters.http.router.v3.Router.start_child_sp
    an>` in the router must be set to true to get the correct topology and
    tracing data. Moreover, SkyWalking Tracer does not support SkyWalking
    extension header (``sw8-x``) temporarily. [#extension:
    envoy.tracers.skywalking]
    """

    # SkyWalking collector service.
    grpc_service: "____config_core_v4_alpha__.GrpcService" = betterproto.message_field(
        1
    )
    client_config: "ClientConfig" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ClientConfig(betterproto.Message):
    """Client config for SkyWalking tracer."""

    # Service name for SkyWalking tracer. If this field is empty, then local
    # service cluster name that configured by :ref:`Bootstrap node
    # <envoy_v3_api_field_config.bootstrap.v3.Bootstrap.node>` message's
    # :ref:`cluster <envoy_v3_api_field_config.core.v3.Node.cluster>` field or
    # command line option :option:`--service-cluster` will be used. If both this
    # field and local service cluster name are empty, ``EnvoyProxy`` is used as
    # the service name by default.
    service_name: str = betterproto.string_field(1)
    # Service instance name for SkyWalking tracer. If this field is empty, then
    # local service node that configured by :ref:`Bootstrap node
    # <envoy_v3_api_field_config.bootstrap.v3.Bootstrap.node>` message's :ref:`id
    # <envoy_v3_api_field_config.core.v3.Node.id>` field or command line  option
    # :option:`--service-node` will be used. If both this field and local service
    # node are empty, ``EnvoyProxy`` is used as the instance name by default.
    instance_name: str = betterproto.string_field(2)
    # Inline authentication token string.
    backend_token: str = betterproto.string_field(3, group="backend_token_specifier")
    # Envoy caches the segment in memory when the SkyWalking backend service is
    # temporarily unavailable. This field specifies the maximum number of
    # segments that can be cached. If not specified, the default is 1024.
    max_cache_size: Optional[int] = betterproto.message_field(
        4, wraps=betterproto.TYPE_UINT32
    )


from .....config.core import v4alpha as ____config_core_v4_alpha__
