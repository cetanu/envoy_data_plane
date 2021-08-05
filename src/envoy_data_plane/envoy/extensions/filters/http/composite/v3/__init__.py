# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/composite/v3/composite.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Composite(betterproto.Message):
    """
    :ref:`Composite filter <config_http_filters_composite>` config. The
    composite filter config allows delegating filter handling to another filter
    as determined by matching on the request headers. This makes it possible to
    use different filters or filter configurations based on the incoming
    request. This is intended to be used with :ref:`ExtensionWithMatcher
    <envoy_api_msg_extensions.common.matching.v3.ExtensionWithMatcher>` where a
    match tree is specified that indicates (via :ref:`ExecuteFilterAction
    <envoy_api_msg_extensions.filters.http.composite.v3.ExecuteFilterAction>`)
    which filter configuration to create and delegate to.
    """

    pass


@dataclass(eq=False, repr=False)
class ExecuteFilterAction(betterproto.Message):
    """
    Composite match action (see :ref:`matching docs
    <arch_overview_matching_api>` for more info on match actions). This
    specifies the filter configuration of the filter that the composite filter
    should delegate filter interactions to.
    """

    typed_config: "_____config_core_v3__.TypedExtensionConfig" = (
        betterproto.message_field(1)
    )


from ......config.core import v3 as _____config_core_v3__
