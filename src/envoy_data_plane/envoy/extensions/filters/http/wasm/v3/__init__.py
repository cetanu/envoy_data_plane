# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/wasm/v3/wasm.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Wasm(betterproto.Message):
    """[[#not-implemented-hide:]"""

    # General Plugin configuration.
    config: "____wasm_v3__.PluginConfig" = betterproto.message_field(1)


from .....wasm import v3 as ____wasm_v3__
