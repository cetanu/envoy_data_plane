# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/rbac/v3/rbac.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class RbacAction(betterproto.Enum):
    ALLOW = 0
    DENY = 1
    LOG = 2


@dataclass(eq=False, repr=False)
class Rbac(betterproto.Message):
    """
    Role Based Access Control (RBAC) provides service-level and method-level
    access control for a service. RBAC policies are additive. The policies are
    examined in order. Requests are allowed or denied based on the `action` and
    whether a matching policy is found. For instance, if the action is ALLOW
    and a matching policy is found the request should be allowed. RBAC can also
    be used to make access logging decisions by communicating with access
    loggers through dynamic metadata. When the action is LOG and at least one
    policy matches, the `access_log_hint` value in the shared key namespace
    'envoy.common' is set to `true` indicating the request should be logged.
    Here is an example of RBAC configuration. It has two policies: * Service
    account "cluster.local/ns/default/sa/admin" has full access to the service,
    and so   does "cluster.local/ns/default/sa/superuser". * Any user can read
    ("GET") the service at paths with prefix "/products", so long as the
    destination port is either 80 or 443.  .. code-block:: yaml   action: ALLOW
    policies:     "service-admin":       permissions:         - any: true
    principals:         - authenticated:             principal_name:
    exact: "cluster.local/ns/default/sa/admin"         - authenticated:
    principal_name:               exact:
    "cluster.local/ns/default/sa/superuser"     "product-viewer":
    permissions:           - and_rules:               rules:                 -
    header: { name: ":method", exact_match: "GET" }                 - url_path:
    path: { prefix: "/products" }                 - or_rules:
    rules:                       - destination_port: 80                       -
    destination_port: 443       principals:         - any: true
    """

    # The action to take if a policy matches. Every action either allows or
    # denies a request, and can also carry out action-specific operations.
    # Actions:  * ALLOW: Allows the request if and only if there is a policy that
    # matches    the request.  * DENY: Allows the request if and only if there
    # are no policies that    match the request.  * LOG: Allows all requests. If
    # at least one policy matches, the dynamic    metadata key `access_log_hint`
    # is set to the value `true` under the shared    key namespace
    # 'envoy.common'. If no policies match, it is set to `false`.    Other
    # actions do not modify this key.
    action: "RbacAction" = betterproto.enum_field(1)
    # Maps from policy name to policy. A match occurs when at least one policy
    # matches the request.
    policies: Dict[str, "Policy"] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass(eq=False, repr=False)
class Policy(betterproto.Message):
    """
    Policy specifies a role and the principals that are assigned/denied the
    role. A policy matches if and only if at least one of its permissions match
    the action taking place AND at least one of its principals match the
    downstream AND the condition is true if specified.
    """

    # Required. The set of permissions that define a role. Each permission is
    # matched with OR semantics. To match all actions for this policy, a single
    # Permission with the `any` field set to true should be used.
    permissions: List["Permission"] = betterproto.message_field(1)
    # Required. The set of principals that are assigned/denied the role based on
    # “action”. Each principal is matched with OR semantics. To match all
    # downstreams for this policy, a single Principal with the `any` field set to
    # true should be used.
    principals: List["Principal"] = betterproto.message_field(2)
    # An optional symbolic expression specifying an access control
    # :ref:`condition <arch_overview_condition>`. The condition is combined with
    # the permissions and the principals as a clause with AND semantics. Only be
    # used when checked_condition is not used.
    condition: "____google_api_expr_v1_alpha1__.Expr" = betterproto.message_field(3)
    # [#not-implemented-hide:] An optional symbolic expression that has been
    # successfully type checked. Only be used when condition is not used.
    checked_condition: "____google_api_expr_v1_alpha1__.CheckedExpr" = (
        betterproto.message_field(4)
    )


@dataclass(eq=False, repr=False)
class Permission(betterproto.Message):
    """
    Permission defines an action (or actions) that a principal can take.
    [#next-free-field: 11]
    """

    # A set of rules that all must match in order to define the action.
    and_rules: "PermissionSet" = betterproto.message_field(1, group="rule")
    # A set of rules where at least one must match in order to define the action.
    or_rules: "PermissionSet" = betterproto.message_field(2, group="rule")
    # When any is set, it matches any action.
    any: bool = betterproto.bool_field(3, group="rule")
    # A header (or pseudo-header such as :path or :method) on the incoming HTTP
    # request. Only available for HTTP request. Note: the pseudo-header :path
    # includes the query and fragment string. Use the `url_path` field if you
    # want to match the URL path without the query and fragment string.
    header: "__route_v3__.HeaderMatcher" = betterproto.message_field(4, group="rule")
    # A URL path on the incoming HTTP request. Only available for HTTP.
    url_path: "___type_matcher_v3__.PathMatcher" = betterproto.message_field(
        10, group="rule"
    )
    # A CIDR block that describes the destination IP.
    destination_ip: "__core_v3__.CidrRange" = betterproto.message_field(5, group="rule")
    # A port number that describes the destination port connecting to.
    destination_port: int = betterproto.uint32_field(6, group="rule")
    # Metadata that describes additional information about the action.
    metadata: "___type_matcher_v3__.MetadataMatcher" = betterproto.message_field(
        7, group="rule"
    )
    # Negates matching the provided permission. For instance, if the value of
    # `not_rule` would match, this permission would not match. Conversely, if the
    # value of `not_rule` would not match, this permission would match.
    not_rule: "Permission" = betterproto.message_field(8, group="rule")
    # The request server from the client's connection request. This is typically
    # TLS SNI. .. attention::   The behavior of this field may be affected by how
    # Envoy is configured   as explained below.   * If the :ref:`TLS Inspector
    # <config_listener_filters_tls_inspector>`     filter is not added, and if a
    # `FilterChainMatch` is not defined for     the :ref:`server name
    # <envoy_api_field_config.listener.v3.FilterChainMatch.server_names>`,     a
    # TLS connection's requested SNI server name will be treated as if it
    # wasn't present.   * A :ref:`listener filter
    # <arch_overview_listener_filters>` may     overwrite a connection's
    # requested server name within Envoy. Please refer to :ref:`this FAQ entry
    # <faq_how_to_setup_sni>` to learn to setup SNI.
    requested_server_name: "___type_matcher_v3__.StringMatcher" = (
        betterproto.message_field(9, group="rule")
    )


@dataclass(eq=False, repr=False)
class PermissionSet(betterproto.Message):
    """
    Used in the `and_rules` and `or_rules` fields in the `rule` oneof.
    Depending on the context, each are applied with the associated behavior.
    """

    rules: List["Permission"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Principal(betterproto.Message):
    """
    Principal defines an identity or a group of identities for a downstream
    subject. [#next-free-field: 12]
    """

    # A set of identifiers that all must match in order to define the downstream.
    and_ids: "PrincipalSet" = betterproto.message_field(1, group="identifier")
    # A set of identifiers at least one must match in order to define the
    # downstream.
    or_ids: "PrincipalSet" = betterproto.message_field(2, group="identifier")
    # When any is set, it matches any downstream.
    any: bool = betterproto.bool_field(3, group="identifier")
    # Authenticated attributes that identify the downstream.
    authenticated: "PrincipalAuthenticated" = betterproto.message_field(
        4, group="identifier"
    )
    # A CIDR block that describes the downstream IP. This address will honor
    # proxy protocol, but will not honor XFF.
    source_ip: "__core_v3__.CidrRange" = betterproto.message_field(
        5, group="identifier"
    )
    # A CIDR block that describes the downstream remote/origin address. Note:
    # This is always the physical peer even if the :ref:`remote_ip
    # <envoy_api_field_config.rbac.v3.Principal.remote_ip>` is inferred from for
    # example the x-forwarder-for header, proxy protocol, etc.
    direct_remote_ip: "__core_v3__.CidrRange" = betterproto.message_field(
        10, group="identifier"
    )
    # A CIDR block that describes the downstream remote/origin address. Note:
    # This may not be the physical peer and could be different from the
    # :ref:`direct_remote_ip
    # <envoy_api_field_config.rbac.v3.Principal.direct_remote_ip>`. E.g, if the
    # remote ip is inferred from for example the x-forwarder-for header, proxy
    # protocol, etc.
    remote_ip: "__core_v3__.CidrRange" = betterproto.message_field(
        11, group="identifier"
    )
    # A header (or pseudo-header such as :path or :method) on the incoming HTTP
    # request. Only available for HTTP request. Note: the pseudo-header :path
    # includes the query and fragment string. Use the `url_path` field if you
    # want to match the URL path without the query and fragment string.
    header: "__route_v3__.HeaderMatcher" = betterproto.message_field(
        6, group="identifier"
    )
    # A URL path on the incoming HTTP request. Only available for HTTP.
    url_path: "___type_matcher_v3__.PathMatcher" = betterproto.message_field(
        9, group="identifier"
    )
    # Metadata that describes additional information about the principal.
    metadata: "___type_matcher_v3__.MetadataMatcher" = betterproto.message_field(
        7, group="identifier"
    )
    # Negates matching the provided principal. For instance, if the value of
    # `not_id` would match, this principal would not match. Conversely, if the
    # value of `not_id` would not match, this principal would match.
    not_id: "Principal" = betterproto.message_field(8, group="identifier")

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.source_ip:
            warnings.warn("Principal.source_ip is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class PrincipalSet(betterproto.Message):
    """
    Used in the `and_ids` and `or_ids` fields in the `identifier` oneof.
    Depending on the context, each are applied with the associated behavior.
    """

    ids: List["Principal"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PrincipalAuthenticated(betterproto.Message):
    """Authentication attributes for a downstream."""

    # The name of the principal. If set, The URI SAN or DNS SAN in that order is
    # used from the certificate, otherwise the subject field is used. If unset,
    # it applies to any user that is authenticated.
    principal_name: "___type_matcher_v3__.StringMatcher" = betterproto.message_field(2)


from .....google.api.expr import v1alpha1 as ____google_api_expr_v1_alpha1__
from ....type.matcher import v3 as ___type_matcher_v3__
from ...core import v3 as __core_v3__
from ...route import v3 as __route_v3__