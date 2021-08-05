# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/common/tap/v4alpha/common.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class CommonExtensionConfig(betterproto.Message):
    """Common configuration for all tap extensions."""

    # If specified, the tap filter will be configured via an admin handler.
    admin_config: "AdminConfig" = betterproto.message_field(1, group="config_type")
    # If specified, the tap filter will be configured via a static configuration
    # that cannot be changed.
    static_config: "____config_tap_v4_alpha__.TapConfig" = betterproto.message_field(
        2, group="config_type"
    )


@dataclass(eq=False, repr=False)
class AdminConfig(betterproto.Message):
    """
    Configuration for the admin handler. See :ref:`here
    <config_http_filters_tap_admin_handler>` for more information.
    """

    # Opaque configuration ID. When requests are made to the admin handler, the
    # passed opaque ID is matched to the configured filter opaque ID to determine
    # which filter to configure.
    config_id: str = betterproto.string_field(1)


from .....config.tap import v4alpha as ____config_tap_v4_alpha__