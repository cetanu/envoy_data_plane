# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/common/mutation_rules/v3/mutation_rules.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class HeaderMutationRules(betterproto.Message):
    """
    The HeaderMutationRules structure specifies what headers may be manipulated
    by a processing filter. This set of rules makes it possible to control
    which modifications a filter may make. By default, an external processing
    server may add, modify, or remove any header except for an "Envoy internal"
    header (which is typically denoted by an x-envoy prefix) or specific
    headers that may affect further filter processing: * host * :authority *
    :scheme * :method Every attempt to add, change, append, or remove a header
    will be tested against the rules here. Disallowed header mutations will be
    ignored unless *disallow_is_error* is set to true. In addition, a counter
    will be incremented whenever a mutation is rejected. In the ext_proc
    filter, that counter is named "rejected_header_mutations". [#next-free-
    field: 8] [#not-implemented-hide:]
    """

    # By default, certain headers that could affect processing of subsequent
    # filters or request routing cannot be modified. These headers are "host",
    # ":authority", ":scheme", and ":method". Setting this parameter to true
    # allows these headers to be modified as well.
    allow_all_routing: Optional[bool] = betterproto.message_field(
        1, wraps=betterproto.TYPE_BOOL
    )
    # If true, allow modification of envoy internal headers. By default, these
    # start with "x-envoy" but this may be overridden in the *Bootstrap*
    # configuration using the :ref:`header_prefix
    # <envoy_v3_api_field_config.bootstrap.v3.Bootstrap.header_prefix>` field.
    # Default is false.
    allow_envoy: Optional[bool] = betterproto.message_field(
        2, wraps=betterproto.TYPE_BOOL
    )
    # If true, prevent modification of any system header, defined as a header
    # that starts with a ":" character, regardless of any other settings. A
    # processing server may still override the ":status" of an HTTP response
    # using an *ImmediateResponse* message. Default is false.
    disallow_system: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    # If true, prevent modifications of all header values, regardless of any
    # other settings. A processing server may still override the ":status" of an
    # HTTP response using an *ImmediateResponse* message. Default is false.
    disallow_all: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )
    # If set, specifically allow any header that matches this regular expression.
    # This overrides all other settings except for *disallow_expression*.
    allow_expression: "____type_matcher_v3__.RegexMatcher" = betterproto.message_field(
        5
    )
    # If set, specifically disallow any header that matches this regular
    # expression regardless of any other settings.
    disallow_expression: "____type_matcher_v3__.RegexMatcher" = (
        betterproto.message_field(6)
    )
    # If true, and if the rules in this list cause a header mutation to be
    # disallowed, then the filter using this configuration will terminate the
    # request with a 500 error. In addition, regardless of the setting of this
    # parameter, any attempt to set, add, or modify a disallowed header will
    # cause the "rejected_header_mutations" counter to be incremented. Default is
    # false.
    disallow_is_error: Optional[bool] = betterproto.message_field(
        7, wraps=betterproto.TYPE_BOOL
    )


from .....type.matcher import v3 as ____type_matcher_v3__
