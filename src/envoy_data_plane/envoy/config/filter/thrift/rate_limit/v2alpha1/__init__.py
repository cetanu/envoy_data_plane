# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/thrift/rate_limit/v2alpha1/rate_limit.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class RateLimit(betterproto.Message):
    """[#next-free-field: 6]"""

    # The rate limit domain to use in the rate limit service request.
    domain: str = betterproto.string_field(1)
    # Specifies the rate limit configuration stage. Each configured rate limit
    # filter performs a rate limit check using descriptors configured in the :ref
    # :`envoy_api_msg_config.filter.network.thrift_proxy.v2alpha1.RouteAction`
    # for the request. Only those entries with a matching stage number are used
    # for a given filter. If not set, the default stage number is 0. .. note::
    # The filter supports a range of 0 - 10 inclusively for stage numbers.
    stage: int = betterproto.uint32_field(2)
    # The timeout in milliseconds for the rate limit service RPC. If not set,
    # this defaults to 20ms.
    timeout: timedelta = betterproto.message_field(3)
    # The filter's behaviour in case the rate limiting service does not respond
    # back. When it is set to true, Envoy will not allow traffic in case of
    # communication failure between rate limiting service and the proxy. Defaults
    # to false.
    failure_mode_deny: bool = betterproto.bool_field(4)
    # Configuration for an external rate limit service provider. If not
    # specified, any calls to the rate limit service will immediately return
    # success.
    rate_limit_service: "____ratelimit_v2__.RateLimitServiceConfig" = (
        betterproto.message_field(5)
    )


from .....ratelimit import v2 as ____ratelimit_v2__
