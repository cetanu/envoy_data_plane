# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/network/thrift_proxy/v4alpha/route.proto, envoy/extensions/filters/network/thrift_proxy/v4alpha/thrift_proxy.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class TransportType(betterproto.Enum):
    """Thrift transport types supported by Envoy."""

    # For downstream connections, the Thrift proxy will attempt to determine
    # which transport to use. For upstream connections, the Thrift proxy will use
    # same transport as the downstream connection.
    AUTO_TRANSPORT = 0
    # The Thrift proxy will use the Thrift framed transport.
    FRAMED = 1
    # The Thrift proxy will use the Thrift unframed transport.
    UNFRAMED = 2
    # The Thrift proxy will assume the client is using the Thrift header
    # transport.
    HEADER = 3


class ProtocolType(betterproto.Enum):
    """Thrift Protocol types supported by Envoy."""

    # For downstream connections, the Thrift proxy will attempt to determine
    # which protocol to use. Note that the older, non-strict (or lax) binary
    # protocol is not included in automatic protocol detection. For upstream
    # connections, the Thrift proxy will use the same protocol as the downstream
    # connection.
    AUTO_PROTOCOL = 0
    # The Thrift proxy will use the Thrift binary protocol.
    BINARY = 1
    # The Thrift proxy will use Thrift non-strict binary protocol.
    LAX_BINARY = 2
    # The Thrift proxy will use the Thrift compact protocol.
    COMPACT = 3
    # The Thrift proxy will use the Thrift "Twitter" protocol implemented by the
    # finagle library.
    TWITTER = 4


@dataclass(eq=False, repr=False)
class RouteConfiguration(betterproto.Message):
    # The name of the route configuration. Reserved for future use in
    # asynchronous route discovery.
    name: str = betterproto.string_field(1)
    # The list of routes that will be matched, in order, against incoming
    # requests. The first route that matches will be used.
    routes: List["Route"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Route(betterproto.Message):
    # Route matching parameters.
    match: "RouteMatch" = betterproto.message_field(1)
    # Route request to some upstream cluster.
    route: "RouteAction" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class RouteMatch(betterproto.Message):
    # If specified, the route must exactly match the request method name. As a
    # special case, an empty string matches any request method name.
    method_name: str = betterproto.string_field(1, group="match_specifier")
    # If specified, the route must have the service name as the request method
    # name prefix. As a special case, an empty string matches any service name.
    # Only relevant when service multiplexing.
    service_name: str = betterproto.string_field(2, group="match_specifier")
    # Inverts whatever matching is done in the :ref:`method_name <envoy_v3_api_fi
    # eld_extensions.filters.network.thrift_proxy.v3.RouteMatch.method_name>` or
    # :ref:`service_name <envoy_v3_api_field_extensions.filters.network.thrift_pr
    # oxy.v3.RouteMatch.service_name>` fields. Cannot be combined with wildcard
    # matching as that would result in routes never being matched. .. note::
    # This does not invert matching done as part of the :ref:`headers field   <en
    # voy_v3_api_field_extensions.filters.network.thrift_proxy.v3.RouteMatch.head
    # ers>` field. To   invert header matching, see :ref:`invert_match
    # <envoy_v3_api_field_config.route.v3.HeaderMatcher.invert_match>`.
    invert: bool = betterproto.bool_field(3)
    # Specifies a set of headers that the route should match on. The router will
    # check the request’s headers against all the specified headers in the route
    # config. A match will happen if all the headers in the route are present in
    # the request with the same values (or based on presence if the value field
    # is not in the config). Note that this only applies for Thrift transports
    # and/or protocols that support headers.
    headers: List[
        "_____config_route_v4_alpha__.HeaderMatcher"
    ] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class RouteAction(betterproto.Message):
    """[#next-free-field: 7]"""

    # Indicates a single upstream cluster to which the request should be routed
    # to.
    cluster: str = betterproto.string_field(1, group="cluster_specifier")
    # Multiple upstream clusters can be specified for a given route. The request
    # is routed to one of the upstream clusters based on weights assigned to each
    # cluster.
    weighted_clusters: "WeightedCluster" = betterproto.message_field(
        2, group="cluster_specifier"
    )
    # Envoy will determine the cluster to route to by reading the value of the
    # Thrift header named by cluster_header from the request headers. If the
    # header is not found or the referenced cluster does not exist Envoy will
    # respond with an unknown method exception or an internal error exception,
    # respectively.
    cluster_header: str = betterproto.string_field(6, group="cluster_specifier")
    # Optional endpoint metadata match criteria used by the subset load balancer.
    # Only endpoints in the upstream cluster with metadata matching what is set
    # in this field will be considered. Note that this will be merged with what's
    # provided in :ref:`WeightedCluster.metadata_match <envoy_v3_api_field_extens
    # ions.filters.network.thrift_proxy.v3.WeightedCluster.ClusterWeight.metadata
    # _match>`, with values there taking precedence. Keys and values should be
    # provided under the "envoy.lb" metadata key.
    metadata_match: "_____config_core_v4_alpha__.Metadata" = betterproto.message_field(
        3
    )
    # Specifies a set of rate limit configurations that could be applied to the
    # route. N.B. Thrift service or method name matching can be achieved by
    # specifying a RequestHeaders action with the header name ":method-name".
    rate_limits: List[
        "_____config_route_v4_alpha__.RateLimit"
    ] = betterproto.message_field(4)
    # Strip the service prefix from the method name, if there's a prefix. For
    # example, the method call Service:method would end up being just method.
    strip_service_name: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class WeightedCluster(betterproto.Message):
    """
    Allows for specification of multiple upstream clusters along with weights
    that indicate the percentage of traffic to be forwarded to each cluster.
    The router selects an upstream cluster based on these weights.
    """

    # Specifies one or more upstream clusters associated with the route.
    clusters: List["WeightedClusterClusterWeight"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class WeightedClusterClusterWeight(betterproto.Message):
    # Name of the upstream cluster.
    name: str = betterproto.string_field(1)
    # When a request matches the route, the choice of an upstream cluster is
    # determined by its weight. The sum of weights across all entries in the
    # clusters array determines the total weight.
    weight: Optional[int] = betterproto.message_field(2, wraps=betterproto.TYPE_UINT32)
    # Optional endpoint metadata match criteria used by the subset load balancer.
    # Only endpoints in the upstream cluster with metadata matching what is set
    # in this field, combined with what's provided in :ref:`RouteAction's
    # metadata_match <envoy_v3_api_field_extensions.filters.network.thrift_proxy.
    # v3.RouteAction.metadata_match>`, will be considered. Values here will take
    # precedence. Keys and values should be provided under the "envoy.lb"
    # metadata key.
    metadata_match: "_____config_core_v4_alpha__.Metadata" = betterproto.message_field(
        3
    )


@dataclass(eq=False, repr=False)
class ThriftProxy(betterproto.Message):
    """[#next-free-field: 8]"""

    # Supplies the type of transport that the Thrift proxy should use. Defaults
    # to :ref:`AUTO_TRANSPORT<envoy_v3_api_enum_value_extensions.filters.network.
    # thrift_proxy.v3.TransportType.AUTO_TRANSPORT>`.
    transport: "TransportType" = betterproto.enum_field(2)
    # Supplies the type of protocol that the Thrift proxy should use. Defaults to
    # :ref:`AUTO_PROTOCOL<envoy_v3_api_enum_value_extensions.filters.network.thri
    # ft_proxy.v3.ProtocolType.AUTO_PROTOCOL>`.
    protocol: "ProtocolType" = betterproto.enum_field(3)
    # The human readable prefix to use when emitting statistics.
    stat_prefix: str = betterproto.string_field(1)
    # The route table for the connection manager is static and is specified in
    # this property.
    route_config: "RouteConfiguration" = betterproto.message_field(4)
    # A list of individual Thrift filters that make up the filter chain for
    # requests made to the Thrift proxy. Order matters as the filters are
    # processed sequentially. For backwards compatibility, if no thrift_filters
    # are specified, a default Thrift router filter
    # (`envoy.filters.thrift.router`) is used. [#extension-category:
    # envoy.thrift_proxy.filters]
    thrift_filters: List["ThriftFilter"] = betterproto.message_field(5)
    # If set to true, Envoy will try to skip decode data after metadata in the
    # Thrift message. This mode will only work if the upstream and downstream
    # protocols are the same and the transport is the same, the transport type is
    # framed and the protocol is not Twitter. Otherwise Envoy will fallback to
    # decode the data.
    payload_passthrough: bool = betterproto.bool_field(6)
    # Optional maximum requests for a single downstream connection. If not
    # specified, there is no limit.
    max_requests_per_connection: Optional[int] = betterproto.message_field(
        7, wraps=betterproto.TYPE_UINT32
    )


@dataclass(eq=False, repr=False)
class ThriftFilter(betterproto.Message):
    """ThriftFilter configures a Thrift filter."""

    # The name of the filter to instantiate. The name must match a supported
    # filter. The built-in filters are: [#comment:TODO(zuercher): Auto generate
    # the following list] * :ref:`envoy.filters.thrift.router
    # <config_thrift_filters_router>` * :ref:`envoy.filters.thrift.rate_limit
    # <config_thrift_filters_rate_limit>`
    name: str = betterproto.string_field(1)
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3, group="config_type"
    )


@dataclass(eq=False, repr=False)
class ThriftProtocolOptions(betterproto.Message):
    """
    ThriftProtocolOptions specifies Thrift upstream protocol options. This
    object is used in in :ref:`typed_extension_protocol_options<envoy_v3_api_fi
    eld_config.cluster.v3.Cluster.typed_extension_protocol_options>`, keyed by
    the name `envoy.filters.network.thrift_proxy`.
    """

    # Supplies the type of transport that the Thrift proxy should use for
    # upstream connections. Selecting :ref:`AUTO_TRANSPORT<envoy_v3_api_enum_valu
    # e_extensions.filters.network.thrift_proxy.v3.TransportType.AUTO_TRANSPORT>`
    # , which is the default, causes the proxy to use the same transport as the
    # downstream connection.
    transport: "TransportType" = betterproto.enum_field(1)
    # Supplies the type of protocol that the Thrift proxy should use for upstream
    # connections. Selecting :ref:`AUTO_PROTOCOL<envoy_v3_api_enum_value_extensio
    # ns.filters.network.thrift_proxy.v3.ProtocolType.AUTO_PROTOCOL>`, which is
    # the default, causes the proxy to use the same protocol as the downstream
    # connection.
    protocol: "ProtocolType" = betterproto.enum_field(2)


from ......config.core import v4alpha as _____config_core_v4_alpha__
from ......config.route import v4alpha as _____config_route_v4_alpha__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
