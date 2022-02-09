# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: xds/core/v3/authority.proto, xds/core/v3/collection_entry.proto, xds/core/v3/context_params.proto, xds/core/v3/extension.proto, xds/core/v3/resource_locator.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class ResourceLocatorScheme(betterproto.Enum):
    XDSTP = 0
    HTTP = 1
    FILE = 2


@dataclass(eq=False, repr=False)
class ContextParams(betterproto.Message):
    """
    Additional parameters that can be used to select resource variants. These
    include any global context parameters, per-resource type client feature
    capabilities and per-resource type functional attributes. All per-resource
    type attributes will be `xds.resource.` prefixed and some of these are
    documented below: `xds.resource.listening_address`: The value is "IP:port"
    (e.g. "10.1.1.3:8080") which is   the listening address of a Listener. Used
    in a Listener resource query.
    """

    params: Dict[str, str] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class Authority(betterproto.Message):
    """xDS authority information."""

    name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class ResourceLocator(betterproto.Message):
    """
    xDS resource locators identify a xDS resource name and instruct the data-
    plane load balancer on how the resource may be located. Resource locators
    have a canonical xdstp:// URI representation:
    xdstp://{authority}/{type_url}/{id}?{context_params}{#directive,*} where
    context_params take the form of URI query parameters. Resource locators
    have a similar canonical http:// URI representation:
    http://{authority}/{type_url}/{id}?{context_params}{#directive,*} Resource
    locators also have a simplified file:// URI representation:
    file:///{id}{#directive,*}
    """

    # URI scheme.
    scheme: "ResourceLocatorScheme" = betterproto.enum_field(1)
    # Opaque identifier for the resource. Any '/' will not be escaped during URI
    # encoding and will form part of the URI path. This may end with ‘*’ for glob
    # collection references.
    id: str = betterproto.string_field(2)
    # Logical authority for resource (not necessarily transport network address).
    # Authorities are opaque in the xDS API, data-plane load balancers will map
    # them to concrete network transports such as an xDS management server, e.g.
    # via envoy.config.core.v3.ConfigSource.
    authority: str = betterproto.string_field(3)
    # Fully qualified resource type (as in type URL without types.googleapis.com/
    # prefix).
    resource_type: str = betterproto.string_field(4)
    # Additional parameters that can be used to select resource variants. Matches
    # must be exact, i.e. all context parameters must match exactly and there
    # must be no additional context parameters set on the matched resource.
    exact_context: "ContextParams" = betterproto.message_field(
        5, group="context_param_specifier"
    )
    # A list of directives that appear in the xDS resource locator #fragment.
    # When encoding to URI form, directives are percent encoded with comma
    # separation.
    directives: List["ResourceLocatorDirective"] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class ResourceLocatorDirective(betterproto.Message):
    """
    Directives provide information to data-plane load balancers on how xDS
    resource names are to be interpreted and potentially further resolved. For
    example, they may provide alternative resource locators for when primary
    resolution fails. Directives are not part of resource names and do not
    appear in a xDS transport discovery request. When encoding to URIs,
    directives take the form: <directive name>=<string representation of
    directive value> For example, we can have alt=xdstp://foo/bar or
    entry=some%20thing. Each directive value type may have its own string
    encoding, in the case of ResourceLocator there is a recursive URI encoding.
    Percent encoding applies to the URI encoding of the directive value.
    Multiple directives are comma-separated, so the reserved characters that
    require percent encoding in a directive value are [',', '#', '[', ']',
    '%']. These are the RFC3986 fragment reserved characters with the addition
    of the xDS scheme specific ','. See
    https://tools.ietf.org/html/rfc3986#page-49 for further details on URI ABNF
    and reserved characters.
    """

    # An alternative resource locator for fallback if the resource is
    # unavailable. For example, take the resource locator:   xdstp://foo/some-
    # type/some-route-table#alt=xdstp://bar/some-type/another-route-table If the
    # data-plane load balancer is unable to reach `foo` to fetch the resource, it
    # will fallback to `bar`. Alternative resources do not need to have
    # equivalent content, but they should be functional substitutes.
    alt: "ResourceLocator" = betterproto.message_field(1, group="directive")
    # List collections support inlining of resources via the entry field in
    # Resource. These inlined Resource objects may have an optional name field
    # specified. When specified, the entry directive allows ResourceLocator to
    # directly reference these inlined resources, e.g. xdstp://.../foo#entry=bar.
    entry: str = betterproto.string_field(2, group="directive")


@dataclass(eq=False, repr=False)
class CollectionEntry(betterproto.Message):
    """
    xDS collection resource wrapper. This encapsulates a xDS resource when
    appearing inside a list collection resource. List collection resources are
    regular Resource messages of type: message <T>Collection {   repeated
    CollectionEntry resources = 1; }
    """

    # A resource locator describing how the member resource is to be located.
    locator: "ResourceLocator" = betterproto.message_field(
        1, group="resource_specifier"
    )
    # The resource is inlined in the list collection.
    inline_entry: "CollectionEntryInlineEntry" = betterproto.message_field(
        2, group="resource_specifier"
    )


@dataclass(eq=False, repr=False)
class CollectionEntryInlineEntry(betterproto.Message):
    """Inlined resource entry."""

    # Optional name to describe the inlined resource. Resource names must
    # [a-zA-Z0-9_-\./]+ (TODO(htuch): turn this into a PGV constraint once
    # finalized, probably should be a RFC3986 pchar). This name allows reference
    # via the #entry directive in ResourceLocator.
    name: str = betterproto.string_field(1)
    # The resource's logical version. It is illegal to have the same named xDS
    # resource name at a given version with different resource payloads.
    version: str = betterproto.string_field(2)
    # The resource payload, including type URL.
    resource: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class TypedExtensionConfig(betterproto.Message):
    """Message type for extension configuration."""

    # The name of an extension. This is not used to select the extension, instead
    # it serves the role of an opaque identifier.
    name: str = betterproto.string_field(1)
    # The typed config for the extension. The type URL will be used to identify
    # the extension. In the case that the type URL is *xds.type.v3.TypedStruct*
    # (or, for historical reasons, *udpa.type.v1.TypedStruct*), the inner type
    # URL of *TypedStruct* will be utilized. See the :ref:`extension
    # configuration overview <config_overview_extension_configuration>` for
    # further details.
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(2)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf