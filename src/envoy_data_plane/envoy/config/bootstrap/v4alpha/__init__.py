# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/bootstrap/v4alpha/bootstrap.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class WatchdogWatchdogActionWatchdogEvent(betterproto.Enum):
    UNKNOWN = 0
    KILL = 1
    MULTIKILL = 2
    MEGAMISS = 3
    MISS = 4


@dataclass(eq=False, repr=False)
class Bootstrap(betterproto.Message):
    """
    Bootstrap :ref:`configuration overview <config_overview_bootstrap>`.
    [#next-free-field: 30]
    """

    # Node identity to present to the management server and for instance
    # identification purposes (e.g. in generated headers).
    node: "__core_v4_alpha__.Node" = betterproto.message_field(1)
    # A list of :ref:`Node <envoy_v3_api_msg_config.core.v3.Node>` field names
    # that will be included in the context parameters of the effective xdstp://
    # URL that is sent in a discovery request when resource locators are used for
    # LDS/CDS. Any non-string field will have its JSON encoding set as the
    # context parameter value, with the exception of metadata, which will be
    # flattened (see example below). The supported field names are: - "cluster" -
    # "id" - "locality.region" - "locality.sub_zone" - "locality.zone" -
    # "metadata" - "user_agent_build_version.metadata" -
    # "user_agent_build_version.version" - "user_agent_name" -
    # "user_agent_version" The node context parameters act as a base layer
    # dictionary for the context parameters (i.e. more specific resource specific
    # context parameters will override). Field names will be prefixed with
    # “udpa.node.” when included in context parameters. For example, if
    # node_context_params is ``["user_agent_name", "metadata"]``, the implied
    # context parameters might be::   node.user_agent_name: "envoy"
    # node.metadata.foo: "{\"bar\": \"baz\"}"   node.metadata.some: "42"
    # node.metadata.thing: "\"thing\"" [#not-implemented-hide:]
    node_context_params: List[str] = betterproto.string_field(26)
    # Statically specified resources.
    static_resources: "BootstrapStaticResources" = betterproto.message_field(2)
    # xDS configuration sources.
    dynamic_resources: "BootstrapDynamicResources" = betterproto.message_field(3)
    # Configuration for the cluster manager which owns all upstream clusters
    # within the server.
    cluster_manager: "ClusterManager" = betterproto.message_field(4)
    # Health discovery service config option. (:ref:`core.ApiConfigSource
    # <envoy_api_msg_config.core.v4alpha.ApiConfigSource>`)
    hds_config: "__core_v4_alpha__.ApiConfigSource" = betterproto.message_field(14)
    # Optional file system path to search for startup flag files.
    flags_path: str = betterproto.string_field(5)
    # Optional set of stats sinks.
    stats_sinks: List["__metrics_v4_alpha__.StatsSink"] = betterproto.message_field(6)
    # Configuration for internal processing of stats.
    stats_config: "__metrics_v4_alpha__.StatsConfig" = betterproto.message_field(13)
    # Optional duration between flushes to configured stats sinks. For
    # performance reasons Envoy latches counters and only flushes counters and
    # gauges at a periodic interval. If not specified the default is 5000ms (5
    # seconds). Only one of `stats_flush_interval` or `stats_flush_on_admin` can
    # be set. Duration must be at least 1ms and at most 5 min.
    stats_flush_interval: timedelta = betterproto.message_field(7, group="stats_flush")
    # Flush stats to sinks only when queried for on the admin interface. If set,
    # a flush timer is not created. Only one of `stats_flush_on_admin` or
    # `stats_flush_interval` can be set.
    stats_flush_on_admin: bool = betterproto.bool_field(29, group="stats_flush")
    # Optional watchdogs configuration. This is used for specifying different
    # watchdogs for the different subsystems. [#extension-category:
    # envoy.guarddog_actions]
    watchdogs: "Watchdogs" = betterproto.message_field(27)
    # Configuration for the runtime configuration provider. If not specified, a
    # “null” provider will be used which will result in all defaults being used.
    layered_runtime: "LayeredRuntime" = betterproto.message_field(17)
    # Configuration for the local administration HTTP server.
    admin: "Admin" = betterproto.message_field(12)
    # Optional overload manager configuration.
    overload_manager: "__overload_v3__.OverloadManager" = betterproto.message_field(15)
    # Enable :ref:`stats for event dispatcher <operations_performance>`, defaults
    # to false. Note that this records a value for each iteration of the event
    # loop on every thread. This should normally be minimal overhead, but when
    # using :ref:`statsd <envoy_api_msg_config.metrics.v4alpha.StatsdSink>`, it
    # will send each observed value over the wire individually because the statsd
    # protocol doesn't have any way to represent a histogram summary. Be aware
    # that this can be a very large volume of data.
    enable_dispatcher_stats: bool = betterproto.bool_field(16)
    # Optional string which will be used in lieu of x-envoy in prefixing headers.
    # For example, if this string is present and set to X-Foo, then x-envoy-
    # retry-on will be transformed into x-foo-retry-on etc. Note this applies to
    # the headers Envoy will generate, the headers Envoy will sanitize, and the
    # headers Envoy will trust for core code and core extensions only. Be VERY
    # careful making changes to this string, especially in multi-layer Envoy
    # deployments or deployments using extensions which are not upstream.
    header_prefix: str = betterproto.string_field(18)
    # Optional proxy version which will be used to set the value of
    # :ref:`server.version statistic <server_statistics>` if specified. Envoy
    # will not process this value, it will be sent as is to :ref:`stats sinks
    # <envoy_api_msg_config.metrics.v4alpha.StatsSink>`.
    stats_server_version_override: Optional[int] = betterproto.message_field(
        19, wraps=betterproto.TYPE_UINT64
    )
    # Always use TCP queries instead of UDP queries for DNS lookups. This may be
    # overridden on a per-cluster basis in cds_config, when :ref:`dns_resolvers
    # <envoy_api_field_config.cluster.v4alpha.Cluster.dns_resolvers>` and
    # :ref:`use_tcp_for_dns_lookups
    # <envoy_api_field_config.cluster.v4alpha.Cluster.use_tcp_for_dns_lookups>`
    # are specified. Setting this value causes failure if the
    # ``envoy.restart_features.use_apple_api_for_dns_lookups`` runtime value is
    # true during server startup. Apple' API only uses UDP for DNS resolution.
    use_tcp_for_dns_lookups: bool = betterproto.bool_field(20)
    # Specifies optional bootstrap extensions to be instantiated at startup time.
    # Each item contains extension specific configuration. [#extension-category:
    # envoy.bootstrap]
    bootstrap_extensions: List[
        "__core_v4_alpha__.TypedExtensionConfig"
    ] = betterproto.message_field(21)
    # Specifies optional extensions instantiated at startup time and invoked
    # during crash time on the request that caused the crash.
    fatal_actions: List["FatalAction"] = betterproto.message_field(28)
    # Configuration sources that will participate in xdstp:// URL authority
    # resolution. The algorithm is as follows: 1. The authority field is taken
    # from the xdstp:// URL, call    this *resource_authority*. 2.
    # *resource_authority* is compared against the authorities in any peer
    # *ConfigSource*. The peer *ConfigSource* is the configuration source
    # message which would have been used unconditionally for resolution    with
    # opaque resource names. If there is a match with an authority, the    peer
    # *ConfigSource* message is used. 3. *resource_authority* is compared
    # sequentially with the authorities in    each configuration source in
    # *config_sources*. The first *ConfigSource*    to match wins. 4. As a
    # fallback, if no configuration source matches, then
    # *default_config_source* is used. 5. If *default_config_source* is not
    # specified, resolution fails. [#not-implemented-hide:]
    config_sources: List["__core_v4_alpha__.ConfigSource"] = betterproto.message_field(
        22
    )
    # Default configuration source for xdstp:// URLs if all other resolution
    # fails. [#not-implemented-hide:]
    default_config_source: "__core_v4_alpha__.ConfigSource" = betterproto.message_field(
        23
    )
    # Optional overriding of default socket interface. The value must be the name
    # of one of the socket interface factories initialized through a bootstrap
    # extension
    default_socket_interface: str = betterproto.string_field(24)
    # Global map of CertificateProvider instances. These instances are referred
    # to by name in the
    # :ref:`CommonTlsContext.CertificateProviderInstance.instance_name <envoy_api
    # _field_extensions.transport_sockets.tls.v4alpha.CommonTlsContext.Certificat
    # eProviderInstance.instance_name>` field. [#not-implemented-hide:]
    certificate_provider_instances: Dict[
        str, "__core_v4_alpha__.TypedExtensionConfig"
    ] = betterproto.map_field(25, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE)


@dataclass(eq=False, repr=False)
class BootstrapStaticResources(betterproto.Message):
    # Static :ref:`Listeners <envoy_api_msg_config.listener.v4alpha.Listener>`.
    # These listeners are available regardless of LDS configuration.
    listeners: List["__listener_v4_alpha__.Listener"] = betterproto.message_field(1)
    # If a network based configuration source is specified for :ref:`cds_config <
    # envoy_api_field_config.bootstrap.v4alpha.Bootstrap.DynamicResources.cds_con
    # fig>`, it's necessary to have some initial cluster definitions available to
    # allow Envoy to know how to speak to the management server. These cluster
    # definitions may not use :ref:`EDS <arch_overview_dynamic_config_eds>` (i.e.
    # they should be static IP or DNS-based).
    clusters: List["__cluster_v4_alpha__.Cluster"] = betterproto.message_field(2)
    # These static secrets can be used by :ref:`SdsSecretConfig
    # <envoy_api_msg_extensions.transport_sockets.tls.v4alpha.SdsSecretConfig>`
    secrets: List[
        "___extensions_transport_sockets_tls_v4_alpha__.Secret"
    ] = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class BootstrapDynamicResources(betterproto.Message):
    """[#next-free-field: 7]"""

    # All :ref:`Listeners <envoy_api_msg_config.listener.v4alpha.Listener>` are
    # provided by a single :ref:`LDS <arch_overview_dynamic_config_lds>`
    # configuration source.
    lds_config: "__core_v4_alpha__.ConfigSource" = betterproto.message_field(1)
    # xdstp:// resource locator for listener collection. [#not-implemented-hide:]
    lds_resources_locator: str = betterproto.string_field(5)
    # All post-bootstrap :ref:`Cluster
    # <envoy_api_msg_config.cluster.v4alpha.Cluster>` definitions are provided by
    # a single :ref:`CDS <arch_overview_dynamic_config_cds>` configuration
    # source.
    cds_config: "__core_v4_alpha__.ConfigSource" = betterproto.message_field(2)
    # xdstp:// resource locator for cluster collection. [#not-implemented-hide:]
    cds_resources_locator: str = betterproto.string_field(6)
    # A single :ref:`ADS <config_overview_ads>` source may be optionally
    # specified. This must have :ref:`api_type
    # <envoy_api_field_config.core.v4alpha.ApiConfigSource.api_type>` :ref:`GRPC
    # <envoy_api_enum_value_config.core.v4alpha.ApiConfigSource.ApiType.GRPC>`.
    # Only :ref:`ConfigSources <envoy_api_msg_config.core.v4alpha.ConfigSource>`
    # that have the :ref:`ads
    # <envoy_api_field_config.core.v4alpha.ConfigSource.ads>` field set will be
    # streamed on the ADS channel.
    ads_config: "__core_v4_alpha__.ApiConfigSource" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class Admin(betterproto.Message):
    """
    Administration interface :ref:`operations documentation
    <operations_admin_interface>`. [#next-free-field: 6]
    """

    # Configuration for :ref:`access logs <arch_overview_access_logs>` emitted by
    # the administration server.
    access_log: List["__accesslog_v4_alpha__.AccessLog"] = betterproto.message_field(5)
    # The cpu profiler output path for the administration server. If no profile
    # path is specified, the default is ‘/var/log/envoy/envoy.prof’.
    profile_path: str = betterproto.string_field(2)
    # The TCP address that the administration server will listen on. If not
    # specified, Envoy will not start an administration server.
    address: "__core_v4_alpha__.Address" = betterproto.message_field(3)
    # Additional socket options that may not be present in Envoy source code or
    # precompiled binaries.
    socket_options: List["__core_v4_alpha__.SocketOption"] = betterproto.message_field(
        4
    )


@dataclass(eq=False, repr=False)
class ClusterManager(betterproto.Message):
    """
    Cluster manager :ref:`architecture overview
    <arch_overview_cluster_manager>`.
    """

    # Name of the local cluster (i.e., the cluster that owns the Envoy running
    # this configuration). In order to enable :ref:`zone aware routing
    # <arch_overview_load_balancing_zone_aware_routing>` this option must be set.
    # If *local_cluster_name* is defined then :ref:`clusters
    # <envoy_api_msg_config.cluster.v4alpha.Cluster>` must be defined in the
    # :ref:`Bootstrap static cluster resources <envoy_api_field_config.bootstrap.
    # v4alpha.Bootstrap.StaticResources.clusters>`. This is unrelated to the
    # :option:`--service-cluster` option which does not `affect zone aware
    # routing <https://github.com/envoyproxy/envoy/issues/774>`_.
    local_cluster_name: str = betterproto.string_field(1)
    # Optional global configuration for outlier detection.
    outlier_detection: "ClusterManagerOutlierDetection" = betterproto.message_field(2)
    # Optional configuration used to bind newly established upstream connections.
    # This may be overridden on a per-cluster basis by upstream_bind_config in
    # the cds_config.
    upstream_bind_config: "__core_v4_alpha__.BindConfig" = betterproto.message_field(3)
    # A management server endpoint to stream load stats to via *StreamLoadStats*.
    # This must have :ref:`api_type
    # <envoy_api_field_config.core.v4alpha.ApiConfigSource.api_type>` :ref:`GRPC
    # <envoy_api_enum_value_config.core.v4alpha.ApiConfigSource.ApiType.GRPC>`.
    load_stats_config: "__core_v4_alpha__.ApiConfigSource" = betterproto.message_field(
        4
    )


@dataclass(eq=False, repr=False)
class ClusterManagerOutlierDetection(betterproto.Message):
    # Specifies the path to the outlier event log.
    event_log_path: str = betterproto.string_field(1)
    # [#not-implemented-hide:] The gRPC service for the outlier detection event
    # service. If empty, outlier detection events won't be sent to a remote
    # endpoint.
    event_service: "__core_v4_alpha__.EventServiceConfig" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Watchdogs(betterproto.Message):
    """
    Allows you to specify different watchdog configs for different subsystems.
    This allows finer tuned policies for the watchdog. If a subsystem is
    omitted the default values for that system will be used.
    """

    # Watchdog for the main thread.
    main_thread_watchdog: "Watchdog" = betterproto.message_field(1)
    # Watchdog for the worker threads.
    worker_watchdog: "Watchdog" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Watchdog(betterproto.Message):
    """
    Envoy process watchdog configuration. When configured, this monitors for
    nonresponsive threads and kills the process after the configured
    thresholds. See the :ref:`watchdog documentation
    <operations_performance_watchdog>` for more information. [#next-free-field:
    8]
    """

    # Register actions that will fire on given WatchDog events. See
    # *WatchDogAction* for priority of events.
    actions: List["WatchdogWatchdogAction"] = betterproto.message_field(7)
    # The duration after which Envoy counts a nonresponsive thread in the
    # *watchdog_miss* statistic. If not specified the default is 200ms.
    miss_timeout: timedelta = betterproto.message_field(1)
    # The duration after which Envoy counts a nonresponsive thread in the
    # *watchdog_mega_miss* statistic. If not specified the default is 1000ms.
    megamiss_timeout: timedelta = betterproto.message_field(2)
    # If a watched thread has been nonresponsive for this duration, assume a
    # programming error and kill the entire Envoy process. Set to 0 to disable
    # kill behavior. If not specified the default is 0 (disabled).
    kill_timeout: timedelta = betterproto.message_field(3)
    # Defines the maximum jitter used to adjust the *kill_timeout* if
    # *kill_timeout* is enabled. Enabling this feature would help to reduce risk
    # of synchronized watchdog kill events across proxies due to external
    # triggers. Set to 0 to disable. If not specified the default is 0
    # (disabled).
    max_kill_timeout_jitter: timedelta = betterproto.message_field(6)
    # If max(2, ceil(registered_threads * Fraction(*multikill_threshold*)))
    # threads have been nonresponsive for at least this duration kill the entire
    # Envoy process. Set to 0 to disable this behavior. If not specified the
    # default is 0 (disabled).
    multikill_timeout: timedelta = betterproto.message_field(4)
    # Sets the threshold for *multikill_timeout* in terms of the percentage of
    # nonresponsive threads required for the *multikill_timeout*. If not
    # specified the default is 0.
    multikill_threshold: "___type_v3__.Percent" = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class WatchdogWatchdogAction(betterproto.Message):
    # Extension specific configuration for the action.
    config: "__core_v4_alpha__.TypedExtensionConfig" = betterproto.message_field(1)
    event: "WatchdogWatchdogActionWatchdogEvent" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class FatalAction(betterproto.Message):
    """
    Fatal actions to run while crashing. Actions can be safe (meaning they are
    async-signal safe) or unsafe. We run all safe actions before we run unsafe
    actions. If using an unsafe action that could get stuck or deadlock, it
    important to have an out of band system to terminate the process. The
    interface for the extension is
    ``Envoy::Server::Configuration::FatalAction``. *FatalAction* extensions
    live in the ``envoy.extensions.fatal_actions`` API namespace.
    """

    # Extension specific configuration for the action. It's expected to conform
    # to the ``Envoy::Server::Configuration::FatalAction`` interface.
    config: "__core_v4_alpha__.TypedExtensionConfig" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Runtime(betterproto.Message):
    """Runtime :ref:`configuration overview <config_runtime>` (deprecated)."""

    # The implementation assumes that the file system tree is accessed via a
    # symbolic link. An atomic link swap is used when a new tree should be
    # switched to. This parameter specifies the path to the symbolic link. Envoy
    # will watch the location for changes and reload the file system tree when
    # they happen. If this parameter is not set, there will be no disk based
    # runtime.
    symlink_root: str = betterproto.string_field(1)
    # Specifies the subdirectory to load within the root directory. This is
    # useful if multiple systems share the same delivery mechanism. Envoy
    # configuration elements can be contained in a dedicated subdirectory.
    subdirectory: str = betterproto.string_field(2)
    # Specifies an optional subdirectory to load within the root directory. If
    # specified and the directory exists, configuration values within this
    # directory will override those found in the primary subdirectory. This is
    # useful when Envoy is deployed across many different types of servers.
    # Sometimes it is useful to have a per service cluster directory for runtime
    # configuration. See below for exactly how the override directory is used.
    override_subdirectory: str = betterproto.string_field(3)
    # Static base runtime. This will be :ref:`overridden
    # <config_runtime_layering>` by other runtime layers, e.g. disk or admin.
    # This follows the :ref:`runtime protobuf JSON representation encoding
    # <config_runtime_proto_json>`.
    base: "betterproto_lib_google_protobuf.Struct" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class RuntimeLayer(betterproto.Message):
    """[#next-free-field: 6]"""

    # Descriptive name for the runtime layer. This is only used for the runtime
    # :http:get:`/runtime` output.
    name: str = betterproto.string_field(1)
    # :ref:`Static runtime <config_runtime_bootstrap>` layer. This follows the
    # :ref:`runtime protobuf JSON representation encoding
    # <config_runtime_proto_json>`. Unlike static xDS resources, this static
    # layer is overridable by later layers in the runtime virtual filesystem.
    static_layer: "betterproto_lib_google_protobuf.Struct" = betterproto.message_field(
        2, group="layer_specifier"
    )
    disk_layer: "RuntimeLayerDiskLayer" = betterproto.message_field(
        3, group="layer_specifier"
    )
    admin_layer: "RuntimeLayerAdminLayer" = betterproto.message_field(
        4, group="layer_specifier"
    )
    rtds_layer: "RuntimeLayerRtdsLayer" = betterproto.message_field(
        5, group="layer_specifier"
    )


@dataclass(eq=False, repr=False)
class RuntimeLayerDiskLayer(betterproto.Message):
    """:ref:`Disk runtime <config_runtime_local_disk>` layer."""

    # The implementation assumes that the file system tree is accessed via a
    # symbolic link. An atomic link swap is used when a new tree should be
    # switched to. This parameter specifies the path to the symbolic link. Envoy
    # will watch the location for changes and reload the file system tree when
    # they happen. See documentation on runtime :ref:`atomicity
    # <config_runtime_atomicity>` for further details on how reloads are treated.
    symlink_root: str = betterproto.string_field(1)
    # Specifies the subdirectory to load within the root directory. This is
    # useful if multiple systems share the same delivery mechanism. Envoy
    # configuration elements can be contained in a dedicated subdirectory.
    subdirectory: str = betterproto.string_field(3)
    # :ref:`Append <config_runtime_local_disk_service_cluster_subdirs>` the
    # service cluster to the path under symlink root.
    append_service_cluster: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class RuntimeLayerAdminLayer(betterproto.Message):
    """:ref:`Admin console runtime <config_runtime_admin>` layer."""

    pass


@dataclass(eq=False, repr=False)
class RuntimeLayerRtdsLayer(betterproto.Message):
    """:ref:`Runtime Discovery Service (RTDS) <config_runtime_rtds>` layer."""

    # Resource to subscribe to at *rtds_config* for the RTDS layer.
    name: str = betterproto.string_field(1)
    # RTDS configuration source.
    rtds_config: "__core_v4_alpha__.ConfigSource" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class LayeredRuntime(betterproto.Message):
    """Runtime :ref:`configuration overview <config_runtime>`."""

    # The :ref:`layers <config_runtime_layering>` of the runtime. This is ordered
    # such that later layers in the list overlay earlier entries.
    layers: List["RuntimeLayer"] = betterproto.message_field(1)


from ....extensions.transport_sockets.tls import (
    v4alpha as ___extensions_transport_sockets_tls_v4_alpha__,
)
from ....type import v3 as ___type_v3__
from ...accesslog import v4alpha as __accesslog_v4_alpha__
from ...cluster import v4alpha as __cluster_v4_alpha__
from ...core import v4alpha as __core_v4_alpha__
from ...listener import v4alpha as __listener_v4_alpha__
from ...metrics import v4alpha as __metrics_v4_alpha__
from ...overload import v3 as __overload_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf