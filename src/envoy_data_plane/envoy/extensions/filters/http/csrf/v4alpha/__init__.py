# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/csrf/v4alpha/csrf.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class CsrfPolicy(betterproto.Message):
    """CSRF filter config."""

    # Specifies the % of requests for which the CSRF filter is enabled. If
    # :ref:`runtime_key
    # <envoy_v3_api_field_config.core.v3.RuntimeFractionalPercent.runtime_key>`
    # is specified, Envoy will lookup the runtime key to get the percentage of
    # requests to filter. .. note::   This field defaults to 100/:ref:`HUNDRED
    # <envoy_v3_api_enum_type.v3.FractionalPercent.DenominatorType>`.
    filter_enabled: "_____config_core_v4_alpha__.RuntimeFractionalPercent" = (
        betterproto.message_field(1)
    )
    # Specifies that CSRF policies will be evaluated and tracked, but not
    # enforced. This is intended to be used when ``filter_enabled`` is off and
    # will be ignored otherwise. If :ref:`runtime_key
    # <envoy_v3_api_field_config.core.v3.RuntimeFractionalPercent.runtime_key>`
    # is specified, Envoy will lookup the runtime key to get the percentage of
    # requests for which it will evaluate and track the request's *Origin* and
    # *Destination* to determine if it's valid, but will not enforce any
    # policies.
    shadow_enabled: "_____config_core_v4_alpha__.RuntimeFractionalPercent" = (
        betterproto.message_field(2)
    )
    # Specifies additional source origins that will be allowed in addition to the
    # destination origin. More information on how this can be configured via
    # runtime can be found :ref:`here <csrf-configuration>`.
    additional_origins: List[
        "_____type_matcher_v4_alpha__.StringMatcher"
    ] = betterproto.message_field(3)


from ......config.core import v4alpha as _____config_core_v4_alpha__
from ......type.matcher import v4alpha as _____type_matcher_v4_alpha__
