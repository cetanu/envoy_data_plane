# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/network/mongo_proxy/v2/mongo_proxy.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class MongoProxy(betterproto.Message):
    # The human readable prefix to use when emitting :ref:`statistics
    # <config_network_filters_mongo_proxy_stats>`.
    stat_prefix: str = betterproto.string_field(1)
    # The optional path to use for writing Mongo access logs. If not access log
    # path is specified no access logs will be written. Note that access log is
    # also gated :ref:`runtime <config_network_filters_mongo_proxy_runtime>`.
    access_log: str = betterproto.string_field(2)
    # Inject a fixed delay before proxying a Mongo operation. Delays are applied
    # to the following MongoDB operations: Query, Insert, GetMore, and
    # KillCursors. Once an active delay is in progress, all incoming data up
    # until the timer event fires will be a part of the delay.
    delay: "___fault_v2__.FaultDelay" = betterproto.message_field(3)
    # Flag to specify whether :ref:`dynamic metadata
    # <config_network_filters_mongo_proxy_dynamic_metadata>` should be emitted.
    # Defaults to false.
    emit_dynamic_metadata: bool = betterproto.bool_field(4)


from ....fault import v2 as ___fault_v2__
