# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/udp/dns_filter/v4alpha/dns_filter.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class DnsFilterConfig(betterproto.Message):
    """Configuration for the DNS filter."""

    # The stat prefix used when emitting DNS filter statistics
    stat_prefix: str = betterproto.string_field(1)
    # Server context configuration contains the data that the filter uses to
    # respond to DNS requests.
    server_config: "DnsFilterConfigServerContextConfig" = betterproto.message_field(2)
    # Client context configuration controls Envoy's behavior when it must use
    # external resolvers to answer a query. This object is optional and if
    # omitted instructs the filter to resolve queries from the data in the
    # server_config
    client_config: "DnsFilterConfigClientContextConfig" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class DnsFilterConfigServerContextConfig(betterproto.Message):
    """
    This message contains the configuration for the DNS Filter operating in a
    server context. This message will contain the virtual hosts and associated
    addresses with which Envoy will respond to queries
    """

    # Load the configuration specified from the control plane
    inline_dns_table: "_____data_dns_v4_alpha__.DnsTable" = betterproto.message_field(
        1, group="config_source"
    )
    # Seed the filter configuration from an external path. This source is a yaml
    # formatted file that contains the DnsTable driving Envoy's responses to DNS
    # queries
    external_dns_table: "_____config_core_v4_alpha__.DataSource" = (
        betterproto.message_field(2, group="config_source")
    )


@dataclass(eq=False, repr=False)
class DnsFilterConfigClientContextConfig(betterproto.Message):
    """
    This message contains the configuration for the DNS Filter operating in a
    client context. This message will contain the timeouts, retry, and
    forwarding configuration for Envoy to make DNS requests to other resolvers
    """

    # Sets the maximum time we will wait for the upstream query to complete We
    # allow 5s for the upstream resolution to complete, so the minimum value here
    # is 1. Note that the total latency for a failed query is the number of
    # retries multiplied by the resolver_timeout.
    resolver_timeout: timedelta = betterproto.message_field(1)
    # DNS resolution configuration which includes the underlying dns resolver
    # addresses and options.
    dns_resolution_config: "_____config_core_v4_alpha__.DnsResolutionConfig" = (
        betterproto.message_field(2)
    )
    # Controls how many outstanding external lookup contexts the filter tracks.
    # The context structure allows the filter to respond to every query even if
    # the external resolution times out or is otherwise unsuccessful
    max_pending_lookups: int = betterproto.uint64_field(3)


from ......config.core import v4alpha as _____config_core_v4_alpha__
from ......data.dns import v4alpha as _____data_dns_v4_alpha__
