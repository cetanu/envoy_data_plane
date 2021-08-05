# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/network/postgres_proxy/v3alpha/postgres_proxy.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class PostgresProxy(betterproto.Message):
    # The human readable prefix to use when emitting :ref:`statistics
    # <config_network_filters_postgres_proxy_stats>`.
    stat_prefix: str = betterproto.string_field(1)
    # Controls whether SQL statements received in Frontend Query messages are
    # parsed. Parsing is required to produce Postgres proxy filter metadata.
    # Defaults to true.
    enable_sql_parsing: Optional[bool] = betterproto.message_field(
        2, wraps=betterproto.TYPE_BOOL
    )
    # Controls whether to terminate SSL session initiated by a client. If the
    # value is false, the Postgres proxy filter will not try to terminate SSL
    # session, but will pass all the packets to the upstream server. If the value
    # is true, the Postgres proxy filter will try to terminate SSL session. In
    # order to do that, the filter chain must use :ref:`starttls transport socket
    # <envoy_api_msg_extensions.transport_sockets.starttls.v3.StartTlsConfig>`.
    # If the filter does not manage to terminate the SSL session, it will close
    # the connection from the client. Refer to official documentation for details
    # `SSL Session Encryption Message Flow
    # <https://www.postgresql.org/docs/current/protocol-
    # flow.html#id-1.10.5.7.11>`_.
    terminate_ssl: bool = betterproto.bool_field(3)
