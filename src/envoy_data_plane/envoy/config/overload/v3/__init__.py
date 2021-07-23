# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/overload/v3/overload.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ResourceMonitor(betterproto.Message):
    # The name of the resource monitor to instantiate. Must match a registered
    # resource monitor type. The built-in resource monitors are: *
    # :ref:`envoy.resource_monitors.fixed_heap
    # <envoy_api_msg_config.resource_monitor.fixed_heap.v2alpha.FixedHeapConfig>`
    # * :ref:`envoy.resource_monitors.injected_resource   <envoy_api_msg_config.r
    # esource_monitor.injected_resource.v2alpha.InjectedResourceConfig>`
    name: str = betterproto.string_field(1)
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3, group="config_type"
    )


@dataclass(eq=False, repr=False)
class ThresholdTrigger(betterproto.Message):
    # If the resource pressure is greater than or equal to this value, the
    # trigger will fire.
    value: float = betterproto.double_field(1)


@dataclass(eq=False, repr=False)
class Trigger(betterproto.Message):
    # The name of the resource this is a trigger for.
    name: str = betterproto.string_field(1)
    threshold: "ThresholdTrigger" = betterproto.message_field(2, group="trigger_oneof")


@dataclass(eq=False, repr=False)
class OverloadAction(betterproto.Message):
    # The name of the overload action. This is just a well-known string that
    # listeners can use for registering callbacks. Custom overload actions should
    # be named using reverse DNS to ensure uniqueness.
    name: str = betterproto.string_field(1)
    # A set of triggers for this action. If any of these triggers fire the
    # overload action is activated. Listeners are notified when the overload
    # action transitions from inactivated to activated, or vice versa.
    triggers: List["Trigger"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class OverloadManager(betterproto.Message):
    # The interval for refreshing resource usage.
    refresh_interval: timedelta = betterproto.message_field(1)
    # The set of resources to monitor.
    resource_monitors: List["ResourceMonitor"] = betterproto.message_field(2)
    # The set of overload actions.
    actions: List["OverloadAction"] = betterproto.message_field(3)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
