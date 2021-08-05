# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/listener/v2/api_listener.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class ApiListener(betterproto.Message):
    """
    Describes a type of API listener, which is used in non-proxy clients. The
    type of API exposed to the non-proxy application depends on the type of API
    listener.
    """

    # The type in this field determines the type of API listener. At present, the
    # following types are supported: envoy.config.filter.network.http_connection_
    # manager.v2.HttpConnectionManager (HTTP) [#next-major-version: In the v3
    # API, replace this Any field with a oneof containing the specific config
    # message for each type of API listener. We could not do this in v2 because
    # it would have caused circular dependencies for go protos: lds.proto depends
    # on this file, and http_connection_manager.proto depends on rds.proto, which
    # is in the same directory as lds.proto, so lds.proto cannot depend on this
    # file.]
    api_listener: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf