# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/upstreams/http/http/v3/http_connection_pool.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class HttpConnectionPoolProto(betterproto.Message):
    """
    A connection pool which forwards downstream HTTP as HTTP to upstream.
    [#extension: envoy.upstreams.http.http]
    """

    pass