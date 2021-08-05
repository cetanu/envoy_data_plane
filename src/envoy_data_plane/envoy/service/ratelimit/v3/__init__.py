# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/ratelimit/v3/rls.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


class RateLimitResponseCode(betterproto.Enum):
    UNKNOWN = 0
    OK = 1
    OVER_LIMIT = 2


class RateLimitResponseRateLimitUnit(betterproto.Enum):
    UNKNOWN = 0
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4


@dataclass(eq=False, repr=False)
class RateLimitRequest(betterproto.Message):
    """
    Main message for a rate limit request. The rate limit service is designed
    to be fully generic in the sense that it can operate on arbitrary
    hierarchical key/value pairs. The loaded configuration will parse the
    request and find the most specific limit to apply. In addition, a
    RateLimitRequest can contain multiple "descriptors" to limit on. When
    multiple descriptors are provided, the server will limit on *ALL* of them
    and return an OVER_LIMIT response if any of them are over limit. This
    enables more complex application level rate limiting scenarios if desired.
    """

    # All rate limit requests must specify a domain. This enables the
    # configuration to be per application without fear of overlap. E.g., "envoy".
    domain: str = betterproto.string_field(1)
    # All rate limit requests must specify at least one RateLimitDescriptor. Each
    # descriptor is processed by the service (see below). If any of the
    # descriptors are over limit, the entire request is considered to be over
    # limit.
    descriptors: List[
        "___extensions_common_ratelimit_v3__.RateLimitDescriptor"
    ] = betterproto.message_field(2)
    # Rate limit requests can optionally specify the number of hits a request
    # adds to the matched limit. If the value is not set in the message, a
    # request increases the matched limit by 1.
    hits_addend: int = betterproto.uint32_field(3)


@dataclass(eq=False, repr=False)
class RateLimitResponse(betterproto.Message):
    """A response from a ShouldRateLimit call. [#next-free-field: 7]"""

    # The overall response code which takes into account all of the descriptors
    # that were passed in the RateLimitRequest message.
    overall_code: "RateLimitResponseCode" = betterproto.enum_field(1)
    # A list of DescriptorStatus messages which matches the length of the
    # descriptor list passed in the RateLimitRequest. This can be used by the
    # caller to determine which individual descriptors failed and/or what the
    # currently configured limits are for all of them.
    statuses: List["RateLimitResponseDescriptorStatus"] = betterproto.message_field(2)
    # A list of headers to add to the response
    response_headers_to_add: List[
        "___config_core_v3__.HeaderValue"
    ] = betterproto.message_field(3)
    # A list of headers to add to the request when forwarded
    request_headers_to_add: List[
        "___config_core_v3__.HeaderValue"
    ] = betterproto.message_field(4)
    # A response body to send to the downstream client when the response code is
    # not OK.
    raw_body: bytes = betterproto.bytes_field(5)
    # Optional response metadata that will be emitted as dynamic metadata to be
    # consumed by the next filter. This metadata lives in a namespace specified
    # by the canonical name of extension filter that requires it: -
    # :ref:`envoy.filters.http.ratelimit
    # <config_http_filters_ratelimit_dynamic_metadata>` for HTTP filter. -
    # :ref:`envoy.filters.network.ratelimit
    # <config_network_filters_ratelimit_dynamic_metadata>` for network filter. -
    # :ref:`envoy.filters.thrift.rate_limit
    # <config_thrift_filters_rate_limit_dynamic_metadata>` for Thrift filter.
    dynamic_metadata: "betterproto_lib_google_protobuf.Struct" = (
        betterproto.message_field(6)
    )


@dataclass(eq=False, repr=False)
class RateLimitResponseRateLimit(betterproto.Message):
    """
    Defines an actual rate limit in terms of requests per unit of time and the
    unit itself.
    """

    # A name or description of this limit.
    name: str = betterproto.string_field(3)
    # The number of requests per unit of time.
    requests_per_unit: int = betterproto.uint32_field(1)
    # The unit of time.
    unit: "RateLimitResponseRateLimitUnit" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class RateLimitResponseQuota(betterproto.Message):
    """
    Cacheable quota for responses, see documentation for the :ref:`quota <envoy
    _v3_api_field_service.ratelimit.v3.RateLimitResponse.DescriptorStatus.quota
    >` field. [#not-implemented-hide:]
    """

    # Number of matching requests granted in quota. Must be 1 or more.
    requests: int = betterproto.uint32_field(1)
    # Point in time at which the quota expires.
    valid_until: datetime = betterproto.message_field(2, group="expiration_specifier")


@dataclass(eq=False, repr=False)
class RateLimitResponseDescriptorStatus(betterproto.Message):
    """[#next-free-field: 6]"""

    # The response code for an individual descriptor.
    code: "RateLimitResponseCode" = betterproto.enum_field(1)
    # The current limit as configured by the server. Useful for debugging, etc.
    current_limit: "RateLimitResponseRateLimit" = betterproto.message_field(2)
    # The limit remaining in the current time unit.
    limit_remaining: int = betterproto.uint32_field(3)
    # Duration until reset of the current limit window.
    duration_until_reset: timedelta = betterproto.message_field(4)
    # Quota granted for the descriptor. This is a certain number of requests over
    # a period of time. The client may cache this result and apply the effective
    # RateLimitResponse to future matching requests containing a matching
    # descriptor without querying rate limit service. Quota is available for a
    # request if its descriptor set has cached quota available for all
    # descriptors. If quota is available, a RLS request will not be made and the
    # quota will be reduced by 1 for all matching descriptors. If there is not
    # sufficient quota, there are three cases: 1. A cached entry exists for a RLS
    # descriptor that is out-of-quota, but not expired.    In this case, the
    # request will be treated as OVER_LIMIT. 2. Some RLS descriptors have a
    # cached entry that has valid quota but some RLS descriptors    have no
    # cached entry. This will trigger a new RLS request.    When the result is
    # returned, a single unit will be consumed from the quota for all    matching
    # descriptors.    If the server did not provide a quota, such as the quota
    # message is empty for some of    the descriptors, then the request admission
    # is determined by the    :ref:`overall_code
    # <envoy_v3_api_field_service.ratelimit.v3.RateLimitResponse.overall_code>`.
    # 3. All RLS descriptors lack a cached entry, this will trigger a new RLS
    # request,    When the result is returned, a single unit will be consumed
    # from the quota for all    matching descriptors.    If the server did not
    # provide a quota, such as the quota message is empty for some of    the
    # descriptors, then the request admission is determined by the
    # :ref:`overall_code
    # <envoy_v3_api_field_service.ratelimit.v3.RateLimitResponse.overall_code>`.
    # When quota expires due to timeout, a new RLS request will also be made. The
    # implementation may choose to preemptively query the rate limit server for
    # more quota on or before expiration or before the available quota runs out.
    # [#not-implemented-hide:]
    quota: "RateLimitResponseQuota" = betterproto.message_field(5)


class RateLimitServiceStub(betterproto.ServiceStub):
    async def should_rate_limit(
        self,
        *,
        domain: str = "",
        descriptors: Optional[
            List["___extensions_common_ratelimit_v3__.RateLimitDescriptor"]
        ] = None,
        hits_addend: int = 0,
    ) -> "RateLimitResponse":
        descriptors = descriptors or []

        request = RateLimitRequest()
        request.domain = domain
        if descriptors is not None:
            request.descriptors = descriptors
        request.hits_addend = hits_addend

        return await self._unary_unary(
            "/envoy.service.ratelimit.v3.RateLimitService/ShouldRateLimit",
            request,
            RateLimitResponse,
        )


class RateLimitServiceBase(ServiceBase):
    async def should_rate_limit(
        self,
        domain: str,
        descriptors: Optional[
            List["___extensions_common_ratelimit_v3__.RateLimitDescriptor"]
        ],
        hits_addend: int,
    ) -> "RateLimitResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_should_rate_limit(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "domain": request.domain,
            "descriptors": request.descriptors,
            "hits_addend": request.hits_addend,
        }

        response = await self.should_rate_limit(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.ratelimit.v3.RateLimitService/ShouldRateLimit": grpclib.const.Handler(
                self.__rpc_should_rate_limit,
                grpclib.const.Cardinality.UNARY_UNARY,
                RateLimitRequest,
                RateLimitResponse,
            ),
        }


from ....config.core import v3 as ___config_core_v3__
from ....extensions.common.ratelimit import v3 as ___extensions_common_ratelimit_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
