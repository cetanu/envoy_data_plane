# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/metrics/v3/metrics_service.proto, envoy/config/metrics/v3/stats.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class StatsSink(betterproto.Message):
    """Configuration for pluggable stats sinks."""

    # The name of the stats sink to instantiate. The name must match a supported
    # stats sink. See the :ref:`extensions listed in typed_config below
    # <extension_category_envoy.stats_sinks>` for the default list of available
    # stats sink. Sinks optionally support tagged/multiple dimensional metrics.
    name: str = betterproto.string_field(1)
    typed_config: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        3, group="config_type"
    )


@dataclass(eq=False, repr=False)
class StatsConfig(betterproto.Message):
    """Statistics configuration such as tagging."""

    # Each stat name is iteratively processed through these tag specifiers. When
    # a tag is matched, the first capture group is removed from the name so later
    # :ref:`TagSpecifiers <envoy_api_msg_config.metrics.v3.TagSpecifier>` cannot
    # match that same portion of the match.
    stats_tags: List["TagSpecifier"] = betterproto.message_field(1)
    # Use all default tag regexes specified in Envoy. These can be combined with
    # custom tags specified in :ref:`stats_tags
    # <envoy_api_field_config.metrics.v3.StatsConfig.stats_tags>`. They will be
    # processed before the custom tags. .. note::   If any default tags are
    # specified twice, the config will be considered   invalid. See
    # :repo:`well_known_names.h <source/common/config/well_known_names.h>` for a
    # list of the default tags in Envoy. If not provided, the value is assumed to
    # be true.
    use_all_default_tags: Optional[bool] = betterproto.message_field(
        2, wraps=betterproto.TYPE_BOOL
    )
    # Inclusion/exclusion matcher for stat name creation. If not provided, all
    # stats are instantiated as normal. Preventing the instantiation of certain
    # families of stats can improve memory performance for Envoys running
    # especially large configs. .. warning::   Excluding stats may affect Envoy's
    # behavior in undocumented ways. See   `issue #8771
    # <https://github.com/envoyproxy/envoy/issues/8771>`_ for more information.
    # If any unexpected behavior changes are observed, please open a new issue
    # immediately.
    stats_matcher: "StatsMatcher" = betterproto.message_field(3)
    # Defines rules for setting the histogram buckets. Rules are evaluated in
    # order, and the first match is applied. If no match is found (or if no rules
    # are set), the following default buckets are used:   .. code-block:: json
    # [       0.5,       1,       5,       10,       25,       50,       100,
    # 250,       500,       1000,       2500,       5000,       10000,
    # 30000,       60000,       300000,       600000,       1800000,
    # 3600000     ]
    histogram_bucket_settings: List[
        "HistogramBucketSettings"
    ] = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class StatsMatcher(betterproto.Message):
    """Configuration for disabling stat instantiation."""

    # If `reject_all` is true, then all stats are disabled. If `reject_all` is
    # false, then all stats are enabled.
    reject_all: bool = betterproto.bool_field(1, group="stats_matcher")
    # Exclusive match. All stats are enabled except for those matching one of the
    # supplied StringMatcher protos.
    exclusion_list: "___type_matcher_v3__.ListStringMatcher" = (
        betterproto.message_field(2, group="stats_matcher")
    )
    # Inclusive match. No stats are enabled except for those matching one of the
    # supplied StringMatcher protos.
    inclusion_list: "___type_matcher_v3__.ListStringMatcher" = (
        betterproto.message_field(3, group="stats_matcher")
    )


@dataclass(eq=False, repr=False)
class TagSpecifier(betterproto.Message):
    """
    Designates a tag name and value pair. The value may be either a fixed value
    or a regex providing the value via capture groups. The specified tag will
    be unconditionally set if a fixed value, otherwise it will only be set if
    one or more capture groups in the regex match.
    """

    # Attaches an identifier to the tag values to identify the tag being in the
    # sink. Envoy has a set of default names and regexes to extract dynamic
    # portions of existing stats, which can be found in :repo:`well_known_names.h
    # <source/common/config/well_known_names.h>` in the Envoy repository. If a
    # :ref:`tag_name <envoy_api_field_config.metrics.v3.TagSpecifier.tag_name>`
    # is provided in the config and neither :ref:`regex
    # <envoy_api_field_config.metrics.v3.TagSpecifier.regex>` or
    # :ref:`fixed_value
    # <envoy_api_field_config.metrics.v3.TagSpecifier.fixed_value>` were
    # specified, Envoy will attempt to find that name in its set of defaults and
    # use the accompanying regex. .. note::   It is invalid to specify the same
    # tag name twice in a config.
    tag_name: str = betterproto.string_field(1)
    # Designates a tag to strip from the tag extracted name and provide as a
    # named tag value for all statistics. This will only occur if any part of the
    # name matches the regex provided with one or more capture groups. The first
    # capture group identifies the portion of the name to remove. The second
    # capture group (which will normally be nested inside the first) will
    # designate the value of the tag for the statistic. If no second capture
    # group is provided, the first will also be used to set the value of the tag.
    # All other capture groups will be ignored. Example 1. a stat name
    # ``cluster.foo_cluster.upstream_rq_timeout`` and one tag specifier: .. code-
    # block:: json   {     "tag_name": "envoy.cluster_name",     "regex":
    # "^cluster\\.((.+?)\\.)"   } Note that the regex will remove
    # ``foo_cluster.`` making the tag extracted name
    # ``cluster.upstream_rq_timeout`` and the tag value for
    # ``envoy.cluster_name`` will be ``foo_cluster`` (note: there will be no
    # ``.`` character because of the second capture group). Example 2. a stat
    # name ``http.connection_manager_1.user_agent.ios.downstream_cx_total`` and
    # two tag specifiers: .. code-block:: json   [     {       "tag_name":
    # "envoy.http_user_agent",       "regex":
    # "^http(?=\\.).*?\\.user_agent\\.((.+?)\\.)\\w+?$"     },     {
    # "tag_name": "envoy.http_conn_manager_prefix",       "regex":
    # "^http\\.((.*?)\\.)"     }   ] The two regexes of the specifiers will be
    # processed in the definition order. The first regex will remove ``ios.``,
    # leaving the tag extracted name
    # ``http.connection_manager_1.user_agent.downstream_cx_total``. The tag
    # ``envoy.http_user_agent`` will be added with tag value ``ios``. The second
    # regex will remove ``connection_manager_1.`` from the tag extracted name
    # produced by the first regex
    # ``http.connection_manager_1.user_agent.downstream_cx_total``, leaving
    # ``http.user_agent.downstream_cx_total`` as the tag extracted name. The tag
    # ``envoy.http_conn_manager_prefix`` will be added with the tag value
    # ``connection_manager_1``.
    regex: str = betterproto.string_field(2, group="tag_value")
    # Specifies a fixed tag value for the ``tag_name``.
    fixed_value: str = betterproto.string_field(3, group="tag_value")


@dataclass(eq=False, repr=False)
class HistogramBucketSettings(betterproto.Message):
    """
    Specifies a matcher for stats and the buckets that matching stats should
    use.
    """

    # The stats that this rule applies to. The match is applied to the original
    # stat name before tag-extraction, for example
    # `cluster.exampleclustername.upstream_cx_length_ms`.
    match: "___type_matcher_v3__.StringMatcher" = betterproto.message_field(1)
    # Each value is the upper bound of a bucket. Each bucket must be greater than
    # 0 and unique. The order of the buckets does not matter.
    buckets: List[float] = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class StatsdSink(betterproto.Message):
    """
    Stats configuration proto schema for built-in *envoy.stat_sinks.statsd*
    sink. This sink does not support tagged metrics. [#extension:
    envoy.stat_sinks.statsd]
    """

    # The UDP address of a running `statsd <https://github.com/etsy/statsd>`_
    # compliant listener. If specified, statistics will be flushed to this
    # address.
    address: "__core_v3__.Address" = betterproto.message_field(
        1, group="statsd_specifier"
    )
    # The name of a cluster that is running a TCP `statsd
    # <https://github.com/etsy/statsd>`_ compliant listener. If specified, Envoy
    # will connect to this cluster to flush statistics.
    tcp_cluster_name: str = betterproto.string_field(2, group="statsd_specifier")
    # Optional custom prefix for StatsdSink. If specified, this will override the
    # default prefix. For example: .. code-block:: json   {     "prefix" :
    # "envoy-prod"   } will change emitted stats to .. code-block:: cpp   envoy-
    # prod.test_counter:1|c   envoy-prod.test_timer:5|ms Note that the default
    # prefix, "envoy", will be used if a prefix is not specified. Stats with
    # default prefix: .. code-block:: cpp   envoy.test_counter:1|c
    # envoy.test_timer:5|ms
    prefix: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class DogStatsdSink(betterproto.Message):
    """
    Stats configuration proto schema for built-in *envoy.stat_sinks.dog_statsd*
    sink. The sink emits stats with `DogStatsD
    <https://docs.datadoghq.com/guides/dogstatsd/>`_ compatible tags. Tags are
    configurable via :ref:`StatsConfig
    <envoy_api_msg_config.metrics.v3.StatsConfig>`. [#extension:
    envoy.stat_sinks.dog_statsd]
    """

    # The UDP address of a running DogStatsD compliant listener. If specified,
    # statistics will be flushed to this address.
    address: "__core_v3__.Address" = betterproto.message_field(
        1, group="dog_statsd_specifier"
    )
    # Optional custom metric name prefix. See :ref:`StatsdSink's prefix field
    # <envoy_api_field_config.metrics.v3.StatsdSink.prefix>` for more details.
    prefix: str = betterproto.string_field(3)
    # Optional max datagram size to use when sending UDP messages. By default
    # Envoy will emit one metric per datagram. By specifying a max-size larger
    # than a single metric, Envoy will emit multiple, new-line separated metrics.
    # The max datagram size should not exceed your network's MTU. Note that this
    # value may not be respected if smaller than a single metric.
    max_bytes_per_datagram: Optional[int] = betterproto.message_field(
        4, wraps=betterproto.TYPE_UINT64
    )


@dataclass(eq=False, repr=False)
class HystrixSink(betterproto.Message):
    """
    Stats configuration proto schema for built-in *envoy.stat_sinks.hystrix*
    sink. The sink emits stats in `text/event-stream
    <https://developer.mozilla.org/en-US/docs/Web/API/Server-
    sent_events/Using_server-sent_events>`_ formatted stream for use by
    `Hystrix dashboard <https://github.com/Netflix-Skunkworks/hystrix-
    dashboard/wiki>`_. Note that only a single HystrixSink should be
    configured. Streaming is started through an admin endpoint
    :http:get:`/hystrix_event_stream`. [#extension: envoy.stat_sinks.hystrix]
    """

    # The number of buckets the rolling statistical window is divided into. Each
    # time the sink is flushed, all relevant Envoy statistics are sampled and
    # added to the rolling window (removing the oldest samples in the window in
    # the process). The sink then outputs the aggregate statistics across the
    # current rolling window to the event stream(s). rolling_window(ms) =
    # stats_flush_interval(ms) * num_of_buckets More detailed explanation can be
    # found in `Hystrix wiki <https://github.com/Netflix/Hystrix/wiki/Metrics-
    # and-Monitoring#hystrixrollingnumber>`_.
    num_buckets: int = betterproto.int64_field(1)


@dataclass(eq=False, repr=False)
class MetricsServiceConfig(betterproto.Message):
    """
    Metrics Service is configured as a built-in
    *envoy.stat_sinks.metrics_service* :ref:`StatsSink
    <envoy_api_msg_config.metrics.v3.StatsSink>`. This opaque configuration
    will be used to create Metrics Service. [#extension:
    envoy.stat_sinks.metrics_service]
    """

    # The upstream gRPC cluster that hosts the metrics service.
    grpc_service: "__core_v3__.GrpcService" = betterproto.message_field(1)
    # API version for metric service transport protocol. This describes the
    # metric service gRPC endpoint and version of messages used on the wire.
    transport_api_version: "__core_v3__.ApiVersion" = betterproto.enum_field(3)
    # If true, counters are reported as the delta between flushing intervals.
    # Otherwise, the current counter value is reported. Defaults to false.
    # Eventually (https://github.com/envoyproxy/envoy/issues/10968) if this value
    # is not set, the sink will take updates from the :ref:`MetricsResponse
    # <envoy_api_msg_service.metrics.v3.StreamMetricsResponse>`.
    report_counters_as_deltas: Optional[bool] = betterproto.message_field(
        2, wraps=betterproto.TYPE_BOOL
    )


from ....type.matcher import v3 as ___type_matcher_v3__
from ...core import v3 as __core_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf