# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/stateful_session/v3/stateful_session.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class StatefulSession(betterproto.Message):
    # Specific implementation of session state. This session state will be used
    # to store and get address of the upstream host to which the session is
    # assigned. [#extension-category: envoy.http.stateful_session]
    session_state: "_____config_core_v3__.TypedExtensionConfig" = (
        betterproto.message_field(1)
    )


@dataclass(eq=False, repr=False)
class StatefulSessionPerRoute(betterproto.Message):
    # Disable the stateful session filter for this particular vhost or route. If
    # disabled is specified in multiple per-filter-configs, the most specific one
    # will be used.
    disabled: bool = betterproto.bool_field(1, group="override")
    # Per-route stateful session configuration that can be served by RDS or
    # static route table.
    stateful_session: "StatefulSession" = betterproto.message_field(2, group="override")


from ......config.core import v3 as _____config_core_v3__
