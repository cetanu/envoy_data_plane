# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/buffer/v3/buffer.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Buffer(betterproto.Message):
    # The maximum request size that the filter will buffer before the connection
    # manager will stop buffering and return a 413 response.
    max_request_bytes: Optional[int] = betterproto.message_field(
        1, wraps=betterproto.TYPE_UINT32
    )


@dataclass(eq=False, repr=False)
class BufferPerRoute(betterproto.Message):
    # Disable the buffer filter for this particular vhost or route.
    disabled: bool = betterproto.bool_field(1, group="override")
    # Override the global configuration of the filter with this new config.
    buffer: "Buffer" = betterproto.message_field(2, group="override")
