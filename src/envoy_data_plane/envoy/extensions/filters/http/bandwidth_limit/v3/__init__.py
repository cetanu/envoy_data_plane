# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/bandwidth_limit/v3/bandwidth_limit.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class BandwidthLimitEnableMode(betterproto.Enum):
    DISABLED = 0
    REQUEST = 1
    RESPONSE = 2
    REQUEST_AND_RESPONSE = 3


@dataclass(eq=False, repr=False)
class BandwidthLimit(betterproto.Message):
    """[#next-free-field: 8]"""

    # The human readable prefix to use when emitting stats.
    stat_prefix: str = betterproto.string_field(1)
    # The enable mode for the bandwidth limit filter. Default is Disabled.
    enable_mode: "BandwidthLimitEnableMode" = betterproto.enum_field(2)
    # The limit supplied in KiB/s. .. note::   It's fine for the limit to be
    # unset for the global configuration since the bandwidth limit   can be
    # applied at a the virtual host or route level. Thus, the limit must be set
    # for the   per route configuration otherwise the config will be rejected. ..
    # note::   When using per route configuration, the limit becomes unique to
    # that route.
    limit_kbps: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT64
    )
    # Optional Fill interval in milliseconds for the token refills. Defaults to
    # 50ms. It must be at least 20ms to avoid too aggressive refills.
    fill_interval: timedelta = betterproto.message_field(4)
    # Runtime flag that controls whether the filter is enabled or not. If not
    # specified, defaults to enabled.
    runtime_enabled: "_____config_core_v3__.RuntimeFeatureFlag" = (
        betterproto.message_field(5)
    )
    # Enable response trailers. .. note::   * If set true, the response trailers
    # *bandwidth-request-delay-ms* and *bandwidth-response-delay-ms* will be
    # added, prefixed by *response_trailer_prefix*.   * bandwidth-request-delay-
    # ms: delay time in milliseconds it took for the request stream transfer.   *
    # bandwidth-response-delay-ms: delay time in milliseconds it took for the
    # response stream transfer.   * If :ref:`enable_mode <envoy_v3_api_field_exte
    # nsions.filters.http.bandwidth_limit.v3.BandwidthLimit.enable_mode>` is
    # DISABLED or REQUEST, the trailers will not be set.   * If both the request
    # and response delay time is 0, the trailers will not be set.
    enable_response_trailers: bool = betterproto.bool_field(6)
    # Optional The prefix for the response trailers.
    response_trailer_prefix: str = betterproto.string_field(7)


from ......config.core import v3 as _____config_core_v3__
