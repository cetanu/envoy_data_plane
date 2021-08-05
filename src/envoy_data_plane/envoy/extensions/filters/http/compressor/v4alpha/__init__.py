# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/compressor/v4alpha/compressor.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Compressor(betterproto.Message):
    """[#next-free-field: 9]"""

    # A compressor library to use for compression. Currently only :ref:`envoy.com
    # pression.gzip.compressor<envoy_api_msg_extensions.compression.gzip.compress
    # or.v3.Gzip>` is included in Envoy. This field is ignored if used in the
    # context of the gzip http-filter, but is mandatory otherwise. [#extension-
    # category: envoy.compression.compressor]
    compressor_library: "_____config_core_v4_alpha__.TypedExtensionConfig" = (
        betterproto.message_field(6)
    )
    # Configuration for request compression. Compression is disabled by default
    # if left empty.
    request_direction_config: "CompressorRequestDirectionConfig" = (
        betterproto.message_field(7)
    )
    # Configuration for response compression. Compression is enabled by default
    # if left empty. .. attention::    If the field is not empty then the
    # duplicate deprecated fields of the `Compressor` message,    such as
    # `content_length`, `content_type`, `disable_on_etag_header`,
    # `remove_accept_encoding_header` and `runtime_enabled`, are ignored.    Also
    # all the statistics related to response compression will be rooted in    `<s
    # tat_prefix>.compressor.<compressor_library.name>.<compressor_library_stat_p
    # refix>.response.*`    instead of    `<stat_prefix>.compressor.<compressor_l
    # ibrary.name>.<compressor_library_stat_prefix>.*`.
    response_direction_config: "CompressorResponseDirectionConfig" = (
        betterproto.message_field(8)
    )


@dataclass(eq=False, repr=False)
class CompressorCommonDirectionConfig(betterproto.Message):
    # Runtime flag that controls whether compression is enabled or not for the
    # direction this common config is put in. If set to false, the filter will
    # operate as a pass-through filter in the chosen direction. If the field is
    # omitted, the filter will be enabled.
    enabled: "_____config_core_v4_alpha__.RuntimeFeatureFlag" = (
        betterproto.message_field(1)
    )
    # Minimum value of Content-Length header of request or response messages
    # (depending on the direction this common config is put in), in bytes, which
    # will trigger compression. The default value is 30.
    min_content_length: Optional[int] = betterproto.message_field(
        2, wraps=betterproto.TYPE_UINT32
    )
    # Set of strings that allows specifying which mime-types yield compression;
    # e.g., application/json, text/html, etc. When this field is not defined,
    # compression will be applied to the following mime-types:
    # "application/javascript", "application/json", "application/xhtml+xml",
    # "image/svg+xml", "text/css", "text/html", "text/plain", "text/xml" and
    # their synonyms.
    content_type: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class CompressorRequestDirectionConfig(betterproto.Message):
    """Configuration for filter behavior on the request direction."""

    common_config: "CompressorCommonDirectionConfig" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class CompressorResponseDirectionConfig(betterproto.Message):
    """Configuration for filter behavior on the response direction."""

    common_config: "CompressorCommonDirectionConfig" = betterproto.message_field(1)
    # If true, disables compression when the response contains an etag header.
    # When it is false, the filter will preserve weak etags and remove the ones
    # that require strong validation.
    disable_on_etag_header: bool = betterproto.bool_field(2)
    # If true, removes accept-encoding from the request headers before
    # dispatching it to the upstream so that responses do not get compressed
    # before reaching the filter. .. attention::    To avoid interfering with
    # other compression filters in the same chain use this option in    the
    # filter closest to the upstream.
    remove_accept_encoding_header: bool = betterproto.bool_field(3)


from ......config.core import v4alpha as _____config_core_v4_alpha__
