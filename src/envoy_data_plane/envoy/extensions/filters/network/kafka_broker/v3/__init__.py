# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/network/kafka_broker/v3/kafka_broker.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class KafkaBroker(betterproto.Message):
    # The prefix to use when emitting :ref:`statistics
    # <config_network_filters_kafka_broker_stats>`.
    stat_prefix: str = betterproto.string_field(1)
