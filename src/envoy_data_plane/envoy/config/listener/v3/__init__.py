# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/listener/v3/api_listener.proto, envoy/config/listener/v3/listener.proto, envoy/config/listener/v3/listener_components.proto, envoy/config/listener/v3/quic_config.proto, envoy/config/listener/v3/udp_listener_config.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from datetime import timedelta
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class FilterChainMatchConnectionSourceType(betterproto.Enum):
    ANY = 0
    SAME_IP_OR_LOOPBACK = 1
    EXTERNAL = 2


class ListenerDrainType(betterproto.Enum):
    DEFAULT = 0
    MODIFY_ONLY = 1


@dataclass(eq=False, repr=False)
class QuicProtocolOptions(betterproto.Message):
    """
    Configuration specific to the UDP QUIC listener. [#next-free-field: 8]
    """

    quic_protocol_options: "__core_v3__.QuicProtocolOptions" = (
        betterproto.message_field(1)
    )
    # Maximum number of milliseconds that connection will be alive when there is
    # no network activity. 300000ms if not specified.
    idle_timeout: timedelta = betterproto.message_field(2)
    # Connection timeout in milliseconds before the crypto handshake is finished.
    # 20000ms if not specified.
    crypto_handshake_timeout: timedelta = betterproto.message_field(3)
    # Runtime flag that controls whether the listener is enabled or not. If not
    # specified, defaults to enabled.
    enabled: "__core_v3__.RuntimeFeatureFlag" = betterproto.message_field(4)
    # A multiplier to number of connections which is used to determine how many
    # packets to read per event loop. A reasonable number should allow the
    # listener to process enough payload but not starve TCP and other UDP sockets
    # and also prevent long event loop duration. The default value is 32. This
    # means if there are N QUIC connections, the total number of packets to read
    # in each read event will be 32 * N. The actual number of packets to read in
    # total by the UDP listener is also bound by 6000, regardless of this field
    # or how many connections there are.
    packets_to_read_to_connection_count_ratio: Optional[
        int
    ] = betterproto.message_field(5, wraps=betterproto.TYPE_UINT32)
    # Configure which implementation of `quic::QuicCryptoClientStreamBase` to be
    # used for this listener. If not specified the :ref:`QUICHE default one
    # configured by <envoy_v3_api_msg_extensions.quic.crypto_stream.v3.CryptoServ
    # erStreamConfig>` will be used. [#extension-category:
    # envoy.quic.server.crypto_stream]
    crypto_stream_config: "__core_v3__.TypedExtensionConfig" = (
        betterproto.message_field(6)
    )
    # Configure which implementation of `quic::ProofSource` to be used for this
    # listener. If not specified the :ref:`default one configured by
    # <envoy_v3_api_msg_extensions.quic.proof_source.v3.ProofSourceConfig>` will
    # be used. [#extension-category: envoy.quic.proof_source]
    proof_source_config: "__core_v3__.TypedExtensionConfig" = betterproto.message_field(
        7
    )


@dataclass(eq=False, repr=False)
class ApiListener(betterproto.Message):
    """
    Describes a type of API listener, which is used in non-proxy clients. The
    type of API exposed to the non-proxy application depends on the type of API
    listener.
    """

    # The type in this field determines the type of API listener. At present, the
    # following types are supported: envoy.extensions.filters.network.http_connec
    # tion_manager.v3.HttpConnectionManager (HTTP) envoy.extensions.filters.netwo
    # rk.http_connection_manager.v3.EnvoyMobileHttpConnectionManager (HTTP)
    # [#next-major-version: In the v3 API, replace this Any field with a oneof
    # containing the specific config message for each type of API listener. We
    # could not do this in v2 because it would have caused circular dependencies
    # for go protos: lds.proto depends on this file, and
    # http_connection_manager.proto depends on rds.proto, which is in the same
    # directory as lds.proto, so lds.proto cannot depend on this file.]
    api_listener: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Filter(betterproto.Message):
    """[#next-free-field: 6]"""

    # The name of the filter to instantiate. The name must match a
    # :ref:`supported filter <config_network_filters>`.
    name: str = betterproto.string_field(1)
    # Filter specific configuration which depends on the filter being
    # instantiated. See the supported filters for further documentation.
    # [#extension-category: envoy.filters.network]
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        4, group="config_type"
    )
    # Configuration source specifier for an extension configuration discovery
    # service. In case of a failure and without the default configuration, the
    # listener closes the connections. [#not-implemented-hide:]
    config_discovery: "__core_v3__.ExtensionConfigSource" = betterproto.message_field(
        5, group="config_type"
    )


@dataclass(eq=False, repr=False)
class FilterChainMatch(betterproto.Message):
    """
    Specifies the match criteria for selecting a specific filter chain for a
    listener. In order for a filter chain to be selected, *ALL* of its criteria
    must be fulfilled by the incoming connection, properties of which are set
    by the networking stack and/or listener filters. The following order
    applies: 1. Destination port. 2. Destination IP address. 3. Server name
    (e.g. SNI for TLS protocol), 4. Transport protocol. 5. Application
    protocols (e.g. ALPN for TLS protocol). 6. Directly connected source IP
    address (this will only be different from the source IP address    when
    using a listener filter that overrides the source address, such as the
    :ref:`Proxy Protocol    listener filter
    <config_listener_filters_proxy_protocol>`). 7. Source type (e.g. any, local
    or external network). 8. Source IP address. 9. Source port. For criteria
    that allow ranges or wildcards, the most specific value in any of the
    configured filter chains that matches the incoming connection is going to
    be used (e.g. for SNI ``www.example.com`` the most specific match would be
    ``www.example.com``, then ``*.example.com``, then ``*.com``, then any
    filter chain without ``server_names`` requirements). A different way to
    reason about the filter chain matches: Suppose there exists N filter
    chains. Prune the filter chain set using the above 8 steps. In each step,
    filter chains which most specifically matches the attributes continue to
    the next step. The listener guarantees at most 1 filter chain is left after
    all of the steps. Example: For destination port, filter chains specifying
    the destination port of incoming traffic are the most specific match. If
    none of the filter chains specifies the exact destination port, the filter
    chains which do not specify ports are the most specific match. Filter
    chains specifying the wrong port can never be the most specific match.
    [#comment: Implemented rules are kept in the preference order, with
    deprecated fields listed at the end, because that's how we want to list
    them in the docs. [#comment:TODO(PiotrSikora): Add support for configurable
    precedence of the rules] [#next-free-field: 14]
    """

    # Optional destination port to consider when use_original_dst is set on the
    # listener in determining a filter chain match.
    destination_port: Optional[int] = betterproto.message_field(
        8, wraps=betterproto.TYPE_UINT32
    )
    # If non-empty, an IP address and prefix length to match addresses when the
    # listener is bound to 0.0.0.0/:: or when use_original_dst is specified.
    prefix_ranges: List["__core_v3__.CidrRange"] = betterproto.message_field(3)
    # If non-empty, an IP address and suffix length to match addresses when the
    # listener is bound to 0.0.0.0/:: or when use_original_dst is specified.
    # [#not-implemented-hide:]
    address_suffix: str = betterproto.string_field(4)
    # [#not-implemented-hide:]
    suffix_len: Optional[int] = betterproto.message_field(
        5, wraps=betterproto.TYPE_UINT32
    )
    # The criteria is satisfied if the directly connected source IP address of
    # the downstream connection is contained in at least one of the specified
    # subnets. If the parameter is not specified or the list is empty, the
    # directly connected source IP address is ignored.
    direct_source_prefix_ranges: List[
        "__core_v3__.CidrRange"
    ] = betterproto.message_field(13)
    # Specifies the connection source IP match type. Can be any, local or
    # external network.
    source_type: "FilterChainMatchConnectionSourceType" = betterproto.enum_field(12)
    # The criteria is satisfied if the source IP address of the downstream
    # connection is contained in at least one of the specified subnets. If the
    # parameter is not specified or the list is empty, the source IP address is
    # ignored.
    source_prefix_ranges: List["__core_v3__.CidrRange"] = betterproto.message_field(6)
    # The criteria is satisfied if the source port of the downstream connection
    # is contained in at least one of the specified ports. If the parameter is
    # not specified, the source port is ignored.
    source_ports: List[int] = betterproto.uint32_field(7)
    # If non-empty, a list of server names (e.g. SNI for TLS protocol) to
    # consider when determining a filter chain match. Those values will be
    # compared against the server names of a new connection, when detected by one
    # of the listener filters. The server name will be matched against all
    # wildcard domains, i.e. ``www.example.com`` will be first matched against
    # ``www.example.com``, then ``*.example.com``, then ``*.com``. Note that
    # partial wildcards are not supported, and values like ``*w.example.com`` are
    # invalid. .. attention::   See the :ref:`FAQ entry <faq_how_to_setup_sni>`
    # on how to configure SNI for more   information.
    server_names: List[str] = betterproto.string_field(11)
    # If non-empty, a transport protocol to consider when determining a filter
    # chain match. This value will be compared against the transport protocol of
    # a new connection, when it's detected by one of the listener filters.
    # Suggested values include: * ``raw_buffer`` - default, used when no
    # transport protocol is detected, * ``tls`` - set by
    # :ref:`envoy.filters.listener.tls_inspector
    # <config_listener_filters_tls_inspector>`   when TLS protocol is detected.
    transport_protocol: str = betterproto.string_field(9)
    # If non-empty, a list of application protocols (e.g. ALPN for TLS protocol)
    # to consider when determining a filter chain match. Those values will be
    # compared against the application protocols of a new connection, when
    # detected by one of the listener filters. Suggested values include: *
    # ``http/1.1`` - set by :ref:`envoy.filters.listener.tls_inspector
    # <config_listener_filters_tls_inspector>`, * ``h2`` - set by
    # :ref:`envoy.filters.listener.tls_inspector
    # <config_listener_filters_tls_inspector>` .. attention::   Currently, only
    # :ref:`TLS Inspector <config_listener_filters_tls_inspector>` provides
    # application protocol detection based on the requested   `ALPN
    # <https://en.wikipedia.org/wiki/Application-Layer_Protocol_Negotiation>`_
    # values.   However, the use of ALPN is pretty much limited to the HTTP/2
    # traffic on the Internet,   and matching on values other than ``h2`` is
    # going to lead to a lot of false negatives,   unless all connecting clients
    # are known to use ALPN.
    application_protocols: List[str] = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class FilterChain(betterproto.Message):
    """
    A filter chain wraps a set of match criteria, an option TLS context, a set
    of filters, and various other parameters. [#next-free-field: 10]
    """

    # The criteria to use when matching a connection to this filter chain.
    filter_chain_match: "FilterChainMatch" = betterproto.message_field(1)
    # A list of individual network filters that make up the filter chain for
    # connections established with the listener. Order matters as the filters are
    # processed sequentially as connection events happen. Note: If the filter
    # list is empty, the connection will close by default.
    filters: List["Filter"] = betterproto.message_field(3)
    # Whether the listener should expect a PROXY protocol V1 header on new
    # connections. If this option is enabled, the listener will assume that that
    # remote address of the connection is the one specified in the header. Some
    # load balancers including the AWS ELB support this option. If the option is
    # absent or set to false, Envoy will use the physical peer address of the
    # connection as the remote address. This field is deprecated. Add a
    # :ref:`PROXY protocol listener filter
    # <config_listener_filters_proxy_protocol>` explicitly instead.
    use_proxy_proto: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )
    # [#not-implemented-hide:] filter chain metadata.
    metadata: "__core_v3__.Metadata" = betterproto.message_field(5)
    # Optional custom transport socket implementation to use for downstream
    # connections. To setup TLS, set a transport socket with name
    # `envoy.transport_sockets.tls` and :ref:`DownstreamTlsContext <envoy_v3_api_
    # msg_extensions.transport_sockets.tls.v3.DownstreamTlsContext>` in the
    # `typed_config`. If no transport socket configuration is specified, new
    # connections will be set up with plaintext. [#extension-category:
    # envoy.transport_sockets.downstream]
    transport_socket: "__core_v3__.TransportSocket" = betterproto.message_field(6)
    # If present and nonzero, the amount of time to allow incoming connections to
    # complete any transport socket negotiations. If this expires before the
    # transport reports connection establishment, the connection is summarily
    # closed.
    transport_socket_connect_timeout: timedelta = betterproto.message_field(9)
    # [#not-implemented-hide:] The unique name (or empty) by which this filter
    # chain is known. If no name is provided, Envoy will allocate an internal
    # UUID for the filter chain. If the filter chain is to be dynamically updated
    # or removed via FCDS a unique name must be provided.
    name: str = betterproto.string_field(7)
    # [#not-implemented-hide:] The configuration to specify whether the filter
    # chain will be built on-demand. If this field is not empty, the filter chain
    # will be built on-demand. Otherwise, the filter chain will be built normally
    # and block listener warming.
    on_demand_configuration: "FilterChainOnDemandConfiguration" = (
        betterproto.message_field(8)
    )

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.use_proxy_proto:
            warnings.warn(
                "FilterChain.use_proxy_proto is deprecated", DeprecationWarning
            )


@dataclass(eq=False, repr=False)
class FilterChainOnDemandConfiguration(betterproto.Message):
    """
    The configuration for on-demand filter chain. If this field is not empty in
    FilterChain message, a filter chain will be built on-demand. On-demand
    filter chains help speedup the warming up of listeners since the building
    and initialization of an on-demand filter chain will be postponed to the
    arrival of new connection requests that require this filter chain. Filter
    chains that are not often used can be set as on-demand.
    """

    # The timeout to wait for filter chain placeholders to complete rebuilding.
    # 1. If this field is set to 0, timeout is disabled. 2. If not specified, a
    # default timeout of 15s is used. Rebuilding will wait until dependencies are
    # ready, have failed, or this timeout is reached. Upon failure or timeout,
    # all connections related to this filter chain will be closed. Rebuilding
    # will start again on the next new connection.
    rebuild_timeout: timedelta = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListenerFilterChainMatchPredicate(betterproto.Message):
    """
    Listener filter chain match configuration. This is a recursive structure
    which allows complex nested match configurations to be built using various
    logical operators. Examples: * Matches if the destination port is 3306. ..
    code-block:: yaml  destination_port_range:   start: 3306   end: 3307 *
    Matches if the destination port is 3306 or 15000. .. code-block:: yaml
    or_match:    rules:      - destination_port_range:          start: 3306
    end: 3307      - destination_port_range:          start: 15000
    end: 15001 [#next-free-field: 6]
    """

    # A set that describes a logical OR. If any member of the set matches, the
    # match configuration matches.
    or_match: "ListenerFilterChainMatchPredicateMatchSet" = betterproto.message_field(
        1, group="rule"
    )
    # A set that describes a logical AND. If all members of the set match, the
    # match configuration matches.
    and_match: "ListenerFilterChainMatchPredicateMatchSet" = betterproto.message_field(
        2, group="rule"
    )
    # A negation match. The match configuration will match if the negated match
    # condition matches.
    not_match: "ListenerFilterChainMatchPredicate" = betterproto.message_field(
        3, group="rule"
    )
    # The match configuration will always match.
    any_match: bool = betterproto.bool_field(4, group="rule")
    # Match destination port. Particularly, the match evaluation must use the
    # recovered local port if the owning listener filter is after :ref:`an
    # original_dst listener filter <config_listener_filters_original_dst>`.
    destination_port_range: "___type_v3__.Int32Range" = betterproto.message_field(
        5, group="rule"
    )


@dataclass(eq=False, repr=False)
class ListenerFilterChainMatchPredicateMatchSet(betterproto.Message):
    """A set of match configurations used for logical operations."""

    # The list of rules that make up the set.
    rules: List["ListenerFilterChainMatchPredicate"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListenerFilter(betterproto.Message):
    # The name of the filter to instantiate. The name must match a
    # :ref:`supported filter <config_listener_filters>`.
    name: str = betterproto.string_field(1)
    # Filter specific configuration which depends on the filter being
    # instantiated. See the supported filters for further documentation.
    # [#extension-category: envoy.filters.listener,envoy.filters.udp_listener]
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3, group="config_type"
    )
    # Optional match predicate used to disable the filter. The filter is enabled
    # when this field is empty. See :ref:`ListenerFilterChainMatchPredicate
    # <envoy_v3_api_msg_config.listener.v3.ListenerFilterChainMatchPredicate>`
    # for further examples.
    filter_disabled: "ListenerFilterChainMatchPredicate" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class UdpListenerConfig(betterproto.Message):
    """[#next-free-field: 8]"""

    # UDP socket configuration for the listener. The default for :ref:`prefer_gro
    # <envoy_v3_api_field_config.core.v3.UdpSocketConfig.prefer_gro>` is false
    # for listener sockets. If receiving a large amount of datagrams from a small
    # number of sources, it may be worthwhile to enable this option after
    # performance testing.
    downstream_socket_config: "__core_v3__.UdpSocketConfig" = betterproto.message_field(
        5
    )
    # Configuration for QUIC protocol. If empty, QUIC will not be enabled on this
    # listener. Set to the default object to enable QUIC without modifying any
    # additional options. .. warning::   QUIC support is currently alpha and
    # should be used with caution. Please   see :ref:`here <arch_overview_http3>`
    # for details.
    quic_options: "QuicProtocolOptions" = betterproto.message_field(7)


@dataclass(eq=False, repr=False)
class ActiveRawUdpListenerConfig(betterproto.Message):
    pass


@dataclass(eq=False, repr=False)
class ListenerCollection(betterproto.Message):
    """
    Listener list collections. Entries are *Listener* resources or references.
    [#not-implemented-hide:]
    """

    entries: List["____xds_core_v3__.CollectionEntry"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Listener(betterproto.Message):
    """[#next-free-field: 30]"""

    # The unique name by which this listener is known. If no name is provided,
    # Envoy will allocate an internal UUID for the listener. If the listener is
    # to be dynamically updated or removed via :ref:`LDS <config_listeners_lds>`
    # a unique name must be provided.
    name: str = betterproto.string_field(1)
    # The address that the listener should listen on. In general, the address
    # must be unique, though that is governed by the bind rules of the OS. E.g.,
    # multiple listeners can listen on port 0 on Linux as the actual port will be
    # allocated by the OS.
    address: "__core_v3__.Address" = betterproto.message_field(2)
    # Optional prefix to use on listener stats. If empty, the stats will be
    # rooted at `listener.<address as string>.`. If non-empty, stats will be
    # rooted at `listener.<stat_prefix>.`.
    stat_prefix: str = betterproto.string_field(28)
    # A list of filter chains to consider for this listener. The
    # :ref:`FilterChain <envoy_v3_api_msg_config.listener.v3.FilterChain>` with
    # the most specific :ref:`FilterChainMatch
    # <envoy_v3_api_msg_config.listener.v3.FilterChainMatch>` criteria is used on
    # a connection. Example using SNI for filter chain selection can be found in
    # the :ref:`FAQ entry <faq_how_to_setup_sni>`.
    filter_chains: List["FilterChain"] = betterproto.message_field(3)
    # If a connection is redirected using *iptables*, the port on which the proxy
    # receives it might be different from the original destination address. When
    # this flag is set to true, the listener hands off redirected connections to
    # the listener associated with the original destination address. If there is
    # no listener associated with the original destination address, the
    # connection is handled by the listener that receives it. Defaults to false.
    use_original_dst: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )
    # The default filter chain if none of the filter chain matches. If no default
    # filter chain is supplied, the connection will be closed. The filter chain
    # match is ignored in this field.
    default_filter_chain: "FilterChain" = betterproto.message_field(25)
    # Soft limit on size of the listener’s new connection read and write buffers.
    # If unspecified, an implementation defined default is applied (1MiB).
    per_connection_buffer_limit_bytes: Optional[int] = betterproto.message_field(
        5, wraps=betterproto.TYPE_UINT32
    )
    # Listener metadata.
    metadata: "__core_v3__.Metadata" = betterproto.message_field(6)
    # [#not-implemented-hide:]
    deprecated_v1: "ListenerDeprecatedV1" = betterproto.message_field(7)
    # The type of draining to perform at a listener-wide level.
    drain_type: "ListenerDrainType" = betterproto.enum_field(8)
    # Listener filters have the opportunity to manipulate and augment the
    # connection metadata that is used in connection filter chain matching, for
    # example. These filters are run before any in :ref:`filter_chains
    # <envoy_v3_api_field_config.listener.v3.Listener.filter_chains>`. Order
    # matters as the filters are processed sequentially right after a socket has
    # been accepted by the listener, and before a connection is created. UDP
    # Listener filters can be specified when the protocol in the listener socket
    # address in :ref:`protocol
    # <envoy_v3_api_field_config.core.v3.SocketAddress.protocol>` is :ref:`UDP
    # <envoy_v3_api_enum_value_config.core.v3.SocketAddress.Protocol.UDP>`. UDP
    # listeners currently support a single filter.
    listener_filters: List["ListenerFilter"] = betterproto.message_field(9)
    # The timeout to wait for all listener filters to complete operation. If the
    # timeout is reached, the accepted socket is closed without a connection
    # being created unless `continue_on_listener_filters_timeout` is set to true.
    # Specify 0 to disable the timeout. If not specified, a default timeout of
    # 15s is used.
    listener_filters_timeout: timedelta = betterproto.message_field(15)
    # Whether a connection should be created when listener filters timeout.
    # Default is false. .. attention::   Some listener filters, such as
    # :ref:`Proxy Protocol filter   <config_listener_filters_proxy_protocol>`,
    # should not be used with this option. It will cause   unexpected behavior
    # when a connection is created.
    continue_on_listener_filters_timeout: bool = betterproto.bool_field(17)
    # Whether the listener should be set as a transparent socket. When this flag
    # is set to true, connections can be redirected to the listener using an
    # *iptables* *TPROXY* target, in which case the original source and
    # destination addresses and ports are preserved on accepted connections. This
    # flag should be used in combination with :ref:`an original_dst
    # <config_listener_filters_original_dst>` :ref:`listener filter
    # <envoy_v3_api_field_config.listener.v3.Listener.listener_filters>` to mark
    # the connections' local addresses as "restored." This can be used to hand
    # off each redirected connection to another listener associated with the
    # connection's destination address. Direct connections to the socket without
    # using *TPROXY* cannot be distinguished from connections redirected using
    # *TPROXY* and are therefore treated as if they were redirected. When this
    # flag is set to false, the listener's socket is explicitly reset as non-
    # transparent. Setting this flag requires Envoy to run with the
    # *CAP_NET_ADMIN* capability. When this flag is not set (default), the socket
    # is not modified, i.e. the transparent option is neither set nor reset.
    transparent: Optional[bool] = betterproto.message_field(
        10, wraps=betterproto.TYPE_BOOL
    )
    # Whether the listener should set the *IP_FREEBIND* socket option. When this
    # flag is set to true, listeners can be bound to an IP address that is not
    # configured on the system running Envoy. When this flag is set to false, the
    # option *IP_FREEBIND* is disabled on the socket. When this flag is not set
    # (default), the socket is not modified, i.e. the option is neither enabled
    # nor disabled.
    freebind: Optional[bool] = betterproto.message_field(
        11, wraps=betterproto.TYPE_BOOL
    )
    # Additional socket options that may not be present in Envoy source code or
    # precompiled binaries.
    socket_options: List["__core_v3__.SocketOption"] = betterproto.message_field(13)
    # Whether the listener should accept TCP Fast Open (TFO) connections. When
    # this flag is set to a value greater than 0, the option TCP_FASTOPEN is
    # enabled on the socket, with a queue length of the specified size (see
    # `details in RFC7413 <https://tools.ietf.org/html/rfc7413#section-5.1>`_).
    # When this flag is set to 0, the option TCP_FASTOPEN is disabled on the
    # socket. When this flag is not set (default), the socket is not modified,
    # i.e. the option is neither enabled nor disabled. On Linux, the
    # net.ipv4.tcp_fastopen kernel parameter must include flag 0x2 to enable
    # TCP_FASTOPEN. See `ip-sysctl.txt
    # <https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt>`_. On
    # macOS, only values of 0, 1, and unset are valid; other values may result in
    # an error. To set the queue length on macOS, set the
    # net.inet.tcp.fastopen_backlog kernel parameter.
    tcp_fast_open_queue_length: Optional[int] = betterproto.message_field(
        12, wraps=betterproto.TYPE_UINT32
    )
    # Specifies the intended direction of the traffic relative to the local
    # Envoy. This property is required on Windows for listeners using the
    # original destination filter, see :ref:`Original Destination
    # <config_listener_filters_original_dst>`.
    traffic_direction: "__core_v3__.TrafficDirection" = betterproto.enum_field(16)
    # If the protocol in the listener socket address in :ref:`protocol
    # <envoy_v3_api_field_config.core.v3.SocketAddress.protocol>` is :ref:`UDP
    # <envoy_v3_api_enum_value_config.core.v3.SocketAddress.Protocol.UDP>`, this
    # field specifies UDP listener specific configuration.
    udp_listener_config: "UdpListenerConfig" = betterproto.message_field(18)
    # Used to represent an API listener, which is used in non-proxy clients. The
    # type of API exposed to the non-proxy application depends on the type of API
    # listener. When this field is set, no other field except for
    # :ref:`name<envoy_v3_api_field_config.listener.v3.Listener.name>` should be
    # set. .. note::  Currently only one ApiListener can be installed; and it can
    # only be done via bootstrap config,  not LDS. [#next-major-version: In the
    # v3 API, instead of this messy approach where the socket listener fields are
    # directly in the top-level Listener message and the API listener types are
    # in the ApiListener message, the socket listener messages should be in their
    # own message, and the top-level Listener should essentially be a oneof that
    # selects between the socket listener and the various types of API listener.
    # That way, a given Listener message can structurally only contain the fields
    # of the relevant type.]
    api_listener: "ApiListener" = betterproto.message_field(19)
    # The listener's connection balancer configuration, currently only applicable
    # to TCP listeners. If no configuration is specified, Envoy will not attempt
    # to balance active connections between worker threads. In the scenario that
    # the listener X redirects all the connections to the listeners Y1 and Y2 by
    # setting :ref:`use_original_dst
    # <envoy_v3_api_field_config.listener.v3.Listener.use_original_dst>` in X and
    # :ref:`bind_to_port
    # <envoy_v3_api_field_config.listener.v3.Listener.bind_to_port>` to false in
    # Y1 and Y2, it is recommended to disable the balance config in listener X to
    # avoid the cost of balancing, and enable the balance config in Y1 and Y2 to
    # balance the connections among the workers.
    connection_balance_config: "ListenerConnectionBalanceConfig" = (
        betterproto.message_field(20)
    )
    # Deprecated. Use `enable_reuse_port` instead.
    reuse_port: bool = betterproto.bool_field(21)
    # When this flag is set to true, listeners set the *SO_REUSEPORT* socket
    # option and create one socket for each worker thread. This makes inbound
    # connections distribute among worker threads roughly evenly in cases where
    # there are a high number of connections. When this flag is set to false, all
    # worker threads share one socket. This field defaults to true. ..
    # attention::   Although this field defaults to true, it has different
    # behavior on different platforms. See   the following text for more
    # information. * On Linux, reuse_port is respected for both TCP and UDP
    # listeners. It also works correctly   with hot restart. * On macOS,
    # reuse_port for TCP does not do what it does on Linux. Instead of load
    # balancing,   the last socket wins and receives all connections/packets. For
    # TCP, reuse_port is force   disabled and the user is warned. For UDP, it is
    # enabled, but only one worker will receive   packets. For QUIC/H3, SW
    # routing will send packets to other workers. For "raw" UDP, only   a single
    # worker will currently receive packets. * On Windows, reuse_port for TCP has
    # undefined behavior. It is force disabled and the user   is warned similar
    # to macOS. It is left enabled for UDP with undefined behavior currently.
    enable_reuse_port: Optional[bool] = betterproto.message_field(
        29, wraps=betterproto.TYPE_BOOL
    )
    # Configuration for :ref:`access logs <arch_overview_access_logs>` emitted by
    # this listener.
    access_log: List["__accesslog_v3__.AccessLog"] = betterproto.message_field(22)
    # The maximum length a tcp listener's pending connections queue can grow to.
    # If no value is provided net.core.somaxconn will be used on Linux and 128
    # otherwise.
    tcp_backlog_size: Optional[int] = betterproto.message_field(
        24, wraps=betterproto.TYPE_UINT32
    )
    # Whether the listener should bind to the port. A listener that doesn't bind
    # can only receive connections redirected from other listeners that set
    # :ref:`use_original_dst
    # <envoy_v3_api_field_config.listener.v3.Listener.use_original_dst>` to true.
    # Default is true.
    bind_to_port: Optional[bool] = betterproto.message_field(
        26, wraps=betterproto.TYPE_BOOL
    )
    # Used to represent an internal listener which does not listen on OSI L4
    # address but can be used by the :ref:`envoy cluster
    # <envoy_v3_api_msg_config.cluster.v3.Cluster>` to create a user space
    # connection to. The internal listener acts as a tcp listener. It supports
    # listener filters and network filter chains. The internal listener require
    # :ref:`address <envoy_v3_api_field_config.listener.v3.Listener.address>` has
    # field `envoy_internal_address`. There are some limitations are derived from
    # the implementation. The known limitations include *
    # :ref:`ConnectionBalanceConfig
    # <envoy_v3_api_msg_config.listener.v3.Listener.ConnectionBalanceConfig>` is
    # not   allowed because both cluster connection and listener connection must
    # be owned by the same dispatcher. * :ref:`tcp_backlog_size
    # <envoy_v3_api_field_config.listener.v3.Listener.tcp_backlog_size>` *
    # :ref:`freebind <envoy_v3_api_field_config.listener.v3.Listener.freebind>` *
    # :ref:`transparent
    # <envoy_v3_api_field_config.listener.v3.Listener.transparent>` [#not-
    # implemented-hide:]
    internal_listener: "ListenerInternalListenerConfig" = betterproto.message_field(
        27, group="listener_specifier"
    )

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.deprecated_v1:
            warnings.warn("Listener.deprecated_v1 is deprecated", DeprecationWarning)
        if self.reuse_port:
            warnings.warn("Listener.reuse_port is deprecated", DeprecationWarning)


@dataclass(eq=False, repr=False)
class ListenerDeprecatedV1(betterproto.Message):
    """[#not-implemented-hide:]"""

    # Whether the listener should bind to the port. A listener that doesn't bind
    # can only receive connections redirected from other listeners that set
    # use_original_dst parameter to true. Default is true. This is deprecated.
    # Use :ref:`Listener.bind_to_port
    # <envoy_v3_api_field_config.listener.v3.Listener.bind_to_port>`
    bind_to_port: Optional[bool] = betterproto.message_field(
        1, wraps=betterproto.TYPE_BOOL
    )


@dataclass(eq=False, repr=False)
class ListenerConnectionBalanceConfig(betterproto.Message):
    """Configuration for listener connection balancing."""

    # If specified, the listener will use the exact connection balancer.
    exact_balance: "ListenerConnectionBalanceConfigExactBalance" = (
        betterproto.message_field(1, group="balance_type")
    )


@dataclass(eq=False, repr=False)
class ListenerConnectionBalanceConfigExactBalance(betterproto.Message):
    """
    A connection balancer implementation that does exact balancing. This means
    that a lock is held during balancing so that connection counts are nearly
    exactly balanced between worker threads. This is "nearly" exact in the
    sense that a connection might close in parallel thus making the counts
    incorrect, but this should be rectified on the next accept. This balancer
    sacrifices accept throughput for accuracy and should be used when there are
    a small number of connections that rarely cycle (e.g., service mesh gRPC
    egress).
    """

    pass


@dataclass(eq=False, repr=False)
class ListenerInternalListenerConfig(betterproto.Message):
    """
    Configuration for envoy internal listener. All the future internal listener
    features should be added here. [#not-implemented-hide:]
    """

    pass


from .....xds.core import v3 as ____xds_core_v3__
from ....type import v3 as ___type_v3__
from ...accesslog import v3 as __accesslog_v3__
from ...core import v3 as __core_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
