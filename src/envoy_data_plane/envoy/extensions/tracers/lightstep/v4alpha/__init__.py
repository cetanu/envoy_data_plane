# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/tracers/lightstep/v4alpha/lightstep.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class LightstepConfigPropagationMode(betterproto.Enum):
    ENVOY = 0
    LIGHTSTEP = 1
    B3 = 2
    TRACE_CONTEXT = 3


@dataclass(eq=False, repr=False)
class LightstepConfig(betterproto.Message):
    """
    Configuration for the LightStep tracer. [#extension:
    envoy.tracers.lightstep]
    """

    # The cluster manager cluster that hosts the LightStep collectors.
    collector_cluster: str = betterproto.string_field(1)
    # File containing the access token to the `LightStep
    # <https://lightstep.com/>`_ API.
    access_token_file: str = betterproto.string_field(2)
    # Propagation modes to use by LightStep's tracer.
    propagation_modes: List["LightstepConfigPropagationMode"] = betterproto.enum_field(
        3
    )