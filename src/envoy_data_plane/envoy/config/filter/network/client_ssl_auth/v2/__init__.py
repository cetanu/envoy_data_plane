# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/network/client_ssl_auth/v2/client_ssl_auth.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ClientSslAuth(betterproto.Message):
    # The :ref:`cluster manager <arch_overview_cluster_manager>` cluster that
    # runs the authentication service. The filter will connect to the service
    # every 60s to fetch the list of principals. The service must support the
    # expected :ref:`REST API <config_network_filters_client_ssl_auth_rest_api>`.
    auth_api_cluster: str = betterproto.string_field(1)
    # The prefix to use when emitting :ref:`statistics
    # <config_network_filters_client_ssl_auth_stats>`.
    stat_prefix: str = betterproto.string_field(2)
    # Time in milliseconds between principal refreshes from the authentication
    # service. Default is 60000 (60s). The actual fetch time will be this value
    # plus a random jittered value between 0-refresh_delay_ms milliseconds.
    refresh_delay: timedelta = betterproto.message_field(3)
    # An optional list of IP address and subnet masks that should be white listed
    # for access by the filter. If no list is provided, there is no IP allowlist.
    ip_white_list: List["_____api_v2_core__.CidrRange"] = betterproto.message_field(4)


from ......api.v2 import core as _____api_v2_core__
