# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/http/grpc_stats/v2alpha/config.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class FilterConfig(betterproto.Message):
    """gRPC statistics filter configuration"""

    # If true, the filter maintains a filter state object with the request and
    # response message counts.
    emit_filter_state: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class FilterObject(betterproto.Message):
    """gRPC statistics filter state object in protobuf form."""

    # Count of request messages in the request stream.
    request_message_count: int = betterproto.uint64_field(1)
    # Count of response messages in the response stream.
    response_message_count: int = betterproto.uint64_field(2)
