# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/upstreams/tcp/generic/v3/generic_connection_pool.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class GenericConnectionPoolProto(betterproto.Message):
    """
    A connection pool which forwards downstream TCP as TCP or HTTP to upstream,
    based on CONNECT configuration. [#extension: envoy.upstreams.tcp.generic]
    """

    pass
