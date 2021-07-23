# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/endpoint/v3/endpoint.proto, envoy/config/endpoint/v3/endpoint_components.proto, envoy/config/endpoint/v3/load_report.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta
from typing import Dict, List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Endpoint(betterproto.Message):
    """Upstream host identifier."""

    # The upstream host address. .. attention::   The form of host address
    # depends on the given cluster type. For STATIC or EDS,   it is expected to
    # be a direct IP address (or something resolvable by the   specified
    # :ref:`resolver
    # <envoy_api_field_config.core.v3.SocketAddress.resolver_name>`   in the
    # Address). For LOGICAL or STRICT DNS, it is expected to be hostname,   and
    # will be resolved via DNS.
    address: "__core_v3__.Address" = betterproto.message_field(1)
    # The optional health check configuration is used as configuration for the
    # health checker to contact the health checked host. .. attention::   This
    # takes into effect only for upstream clusters with   :ref:`active health
    # checking <arch_overview_health_checking>` enabled.
    health_check_config: "EndpointHealthCheckConfig" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class EndpointHealthCheckConfig(betterproto.Message):
    """The optional health check configuration."""

    # Optional alternative health check port value. By default the health check
    # address port of an upstream host is the same as the host's serving address
    # port. This provides an alternative health check port. Setting this with a
    # non-zero value allows an upstream host to have different health check
    # address port.
    port_value: int = betterproto.uint32_field(1)


@dataclass(eq=False, repr=False)
class LbEndpoint(betterproto.Message):
    """An Endpoint that Envoy can route traffic to. [#next-free-field: 6]"""

    endpoint: "Endpoint" = betterproto.message_field(1, group="host_identifier")
    # [#not-implemented-hide:]
    endpoint_name: str = betterproto.string_field(5, group="host_identifier")
    # Optional health status when known and supplied by EDS server.
    health_status: "__core_v3__.HealthStatus" = betterproto.enum_field(2)
    # The endpoint metadata specifies values that may be used by the load
    # balancer to select endpoints in a cluster for a given request. The filter
    # name should be specified as *envoy.lb*. An example boolean key-value pair
    # is *canary*, providing the optional canary status of the upstream host.
    # This may be matched against in a route's :ref:`RouteAction
    # <envoy_api_msg_config.route.v3.RouteAction>` metadata_match field to subset
    # the endpoints considered in cluster load balancing.
    metadata: "__core_v3__.Metadata" = betterproto.message_field(3)
    # The optional load balancing weight of the upstream host; at least 1. Envoy
    # uses the load balancing weight in some of the built in load balancers. The
    # load balancing weight for an endpoint is divided by the sum of the weights
    # of all endpoints in the endpoint's locality to produce a percentage of
    # traffic for the endpoint. This percentage is then further weighted by the
    # endpoint's locality's load balancing weight from LocalityLbEndpoints. If
    # unspecified, each host is presumed to have equal weight in a locality.
    load_balancing_weight: Optional[int] = betterproto.message_field(
        4, wraps=betterproto.TYPE_UINT32
    )


@dataclass(eq=False, repr=False)
class LocalityLbEndpoints(betterproto.Message):
    """
    A group of endpoints belonging to a Locality. One can have multiple
    LocalityLbEndpoints for a locality, but this is generally only done if the
    different groups need to have different load balancing weights or different
    priorities. [#next-free-field: 7]
    """

    # Identifies location of where the upstream hosts run.
    locality: "__core_v3__.Locality" = betterproto.message_field(1)
    # The group of endpoints belonging to the locality specified.
    lb_endpoints: List["LbEndpoint"] = betterproto.message_field(2)
    # Optional: Per priority/region/zone/sub_zone weight; at least 1. The load
    # balancing weight for a locality is divided by the sum of the weights of all
    # localities  at the same priority level to produce the effective percentage
    # of traffic for the locality. Locality weights are only considered when
    # :ref:`locality weighted load balancing
    # <arch_overview_load_balancing_locality_weighted_lb>` is configured. These
    # weights are ignored otherwise. If no weights are specified when locality
    # weighted load balancing is enabled, the locality is assigned no load.
    load_balancing_weight: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT32
    )
    # Optional: the priority for this LocalityLbEndpoints. If unspecified this
    # will default to the highest priority (0). Under usual circumstances, Envoy
    # will only select endpoints for the highest priority (0). In the event all
    # endpoints for a particular priority are unavailable/unhealthy, Envoy will
    # fail over to selecting endpoints for the next highest priority group.
    # Priorities should range from 0 (highest) to N (lowest) without skipping.
    priority: int = betterproto.uint32_field(5)
    # Optional: Per locality proximity value which indicates how close this
    # locality is from the source locality. This value only provides ordering
    # information (lower the value, closer it is to the source locality). This
    # will be consumed by load balancing schemes that need proximity order to
    # determine where to route the requests. [#not-implemented-hide:]
    proximity: Optional[int] = betterproto.message_field(
        6, wraps=betterproto.TYPE_UINT32
    )


@dataclass(eq=False, repr=False)
class ClusterLoadAssignment(betterproto.Message):
    """
    Each route from RDS will map to a single cluster or traffic split across
    clusters using weights expressed in the RDS WeightedCluster. With EDS, each
    cluster is treated independently from a LB perspective, with LB taking
    place between the Localities within a cluster and at a finer granularity
    between the hosts within a locality. The percentage of traffic for each
    endpoint is determined by both its load_balancing_weight, and the
    load_balancing_weight of its locality. First, a locality will be selected,
    then an endpoint within that locality will be chose based on its weight.
    [#next-free-field: 6]
    """

    # Name of the cluster. This will be the :ref:`service_name
    # <envoy_api_field_config.cluster.v3.Cluster.EdsClusterConfig.service_name>`
    # value if specified in the cluster :ref:`EdsClusterConfig
    # <envoy_api_msg_config.cluster.v3.Cluster.EdsClusterConfig>`.
    cluster_name: str = betterproto.string_field(1)
    # List of endpoints to load balance to.
    endpoints: List["LocalityLbEndpoints"] = betterproto.message_field(2)
    # Map of named endpoints that can be referenced in LocalityLbEndpoints.
    # [#not-implemented-hide:]
    named_endpoints: Dict[str, "Endpoint"] = betterproto.map_field(
        5, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    # Load balancing policy settings.
    policy: "ClusterLoadAssignmentPolicy" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ClusterLoadAssignmentPolicy(betterproto.Message):
    """Load balancing policy settings. [#next-free-field: 6]"""

    # Action to trim the overall incoming traffic to protect the upstream hosts.
    # This action allows protection in case the hosts are unable to recover from
    # an outage, or unable to autoscale or unable to handle incoming traffic
    # volume for any reason. At the client each category is applied one after the
    # other to generate the 'actual' drop percentage on all outgoing traffic. For
    # example: .. code-block:: json  { "drop_overloads": [      { "category":
    # "throttle", "drop_percentage": 60 }      { "category": "lb",
    # "drop_percentage": 50 }  ]} The actual drop percentages applied to the
    # traffic at the clients will be    "throttle"_drop = 60%    "lb"_drop = 20%
    # // 50% of the remaining 'actual' load, which is 40%.
    # actual_outgoing_load = 20% // remaining after applying all categories.
    drop_overloads: List[
        "ClusterLoadAssignmentPolicyDropOverload"
    ] = betterproto.message_field(2)
    # Priority levels and localities are considered overprovisioned with this
    # factor (in percentage). This means that we don't consider a priority level
    # or locality unhealthy until the percentage of healthy hosts multiplied by
    # the overprovisioning factor drops below 100. With the default value
    # 140(1.4), Envoy doesn't consider a priority level or a locality unhealthy
    # until their percentage of healthy hosts drops below 72%. For example: ..
    # code-block:: json  { "overprovisioning_factor": 100 } Read more at
    # :ref:`priority levels <arch_overview_load_balancing_priority_levels>` and
    # :ref:`localities <arch_overview_load_balancing_locality_weighted_lb>`.
    overprovisioning_factor: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT32
    )
    # The max time until which the endpoints from this assignment can be used. If
    # no new assignments are received before this time expires the endpoints are
    # considered stale and should be marked unhealthy. Defaults to 0 which means
    # endpoints never go stale.
    endpoint_stale_after: timedelta = betterproto.message_field(4)
    # The flag to disable overprovisioning. If it is set to true,
    # :ref:`overprovisioning factor
    # <arch_overview_load_balancing_overprovisioning_factor>` will be ignored and
    # Envoy will not perform graceful failover between priority levels or
    # localities as endpoints become unhealthy. Otherwise Envoy will perform
    # graceful failover as :ref:`overprovisioning factor
    # <arch_overview_load_balancing_overprovisioning_factor>` suggests. [#next-
    # major-version: Unify with overprovisioning config as a single message.]
    # [#not-implemented-hide:]
    disable_overprovisioning: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class ClusterLoadAssignmentPolicyDropOverload(betterproto.Message):
    # Identifier for the policy specifying the drop.
    category: str = betterproto.string_field(1)
    # Percentage of traffic that should be dropped for the category.
    drop_percentage: "___type_v3__.FractionalPercent" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class UpstreamLocalityStats(betterproto.Message):
    """
    These are stats Envoy reports to GLB every so often. Report frequency is
    defined by :ref:`LoadStatsResponse.load_reporting_interval<envoy_api_field_
    service.load_stats.v3.LoadStatsResponse.load_reporting_interval>`. Stats
    per upstream region/zone and optionally per subzone. [#not-implemented-
    hide:] Not configuration. TBD how to doc proto APIs. [#next-free-field: 9]
    """

    # Name of zone, region and optionally endpoint group these metrics were
    # collected from. Zone and region names could be empty if unknown.
    locality: "__core_v3__.Locality" = betterproto.message_field(1)
    # The total number of requests successfully completed by the endpoints in the
    # locality.
    total_successful_requests: int = betterproto.uint64_field(2)
    # The total number of unfinished requests
    total_requests_in_progress: int = betterproto.uint64_field(3)
    # The total number of requests that failed due to errors at the endpoint,
    # aggregated over all endpoints in the locality.
    total_error_requests: int = betterproto.uint64_field(4)
    # The total number of requests that were issued by this Envoy since the last
    # report. This information is aggregated over all the upstream endpoints in
    # the locality.
    total_issued_requests: int = betterproto.uint64_field(8)
    # Stats for multi-dimensional load balancing.
    load_metric_stats: List["EndpointLoadMetricStats"] = betterproto.message_field(5)
    # Endpoint granularity stats information for this locality. This information
    # is populated if the Server requests it by setting :ref:`LoadStatsResponse.r
    # eport_endpoint_granularity<envoy_api_field_service.load_stats.v3.LoadStatsR
    # esponse.report_endpoint_granularity>`.
    upstream_endpoint_stats: List["UpstreamEndpointStats"] = betterproto.message_field(
        7
    )
    # [#not-implemented-hide:] The priority of the endpoint group these metrics
    # were collected from.
    priority: int = betterproto.uint32_field(6)


@dataclass(eq=False, repr=False)
class UpstreamEndpointStats(betterproto.Message):
    """
    [#not-implemented-hide:] Not configuration. TBD how to doc proto APIs.
    [#next-free-field: 8]
    """

    # Upstream host address.
    address: "__core_v3__.Address" = betterproto.message_field(1)
    # Opaque and implementation dependent metadata of the endpoint. Envoy will
    # pass this directly to the management server.
    metadata: "betterproto_lib_google_protobuf.Struct" = betterproto.message_field(6)
    # The total number of requests successfully completed by the endpoints in the
    # locality. These include non-5xx responses for HTTP, where errors originate
    # at the client and the endpoint responded successfully. For gRPC, the grpc-
    # status values are those not covered by total_error_requests below.
    total_successful_requests: int = betterproto.uint64_field(2)
    # The total number of unfinished requests for this endpoint.
    total_requests_in_progress: int = betterproto.uint64_field(3)
    # The total number of requests that failed due to errors at the endpoint. For
    # HTTP these are responses with 5xx status codes and for gRPC the grpc-status
    # values:   - DeadlineExceeded   - Unimplemented   - Internal   - Unavailable
    # - Unknown   - DataLoss
    total_error_requests: int = betterproto.uint64_field(4)
    # The total number of requests that were issued to this endpoint since the
    # last report. A single TCP connection, HTTP or gRPC request or stream is
    # counted as one request.
    total_issued_requests: int = betterproto.uint64_field(7)
    # Stats for multi-dimensional load balancing.
    load_metric_stats: List["EndpointLoadMetricStats"] = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class EndpointLoadMetricStats(betterproto.Message):
    """
    [#not-implemented-hide:] Not configuration. TBD how to doc proto APIs.
    """

    # Name of the metric; may be empty.
    metric_name: str = betterproto.string_field(1)
    # Number of calls that finished and included this metric.
    num_requests_finished_with_metric: int = betterproto.uint64_field(2)
    # Sum of metric values across all calls that finished with this metric for
    # load_reporting_interval.
    total_metric_value: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class ClusterStats(betterproto.Message):
    """
    Per cluster load stats. Envoy reports these stats a management server in a
    :ref:`LoadStatsRequest<envoy_api_msg_service.load_stats.v3.LoadStatsRequest
    >` [#not-implemented-hide:] Not configuration. TBD how to doc proto APIs.
    Next ID: 7 [#next-free-field: 7]
    """

    # The name of the cluster.
    cluster_name: str = betterproto.string_field(1)
    # The eds_cluster_config service_name of the cluster. It's possible that two
    # clusters send the same service_name to EDS, in that case, the management
    # server is supposed to do aggregation on the load reports.
    cluster_service_name: str = betterproto.string_field(6)
    # Need at least one.
    upstream_locality_stats: List["UpstreamLocalityStats"] = betterproto.message_field(
        2
    )
    # Cluster-level stats such as total_successful_requests may be computed by
    # summing upstream_locality_stats. In addition, below there are additional
    # cluster-wide stats. The total number of dropped requests. This covers
    # requests deliberately dropped by the drop_overload policy and circuit
    # breaking.
    total_dropped_requests: int = betterproto.uint64_field(3)
    # Information about deliberately dropped requests for each category specified
    # in the DropOverload policy.
    dropped_requests: List["ClusterStatsDroppedRequests"] = betterproto.message_field(5)
    # Period over which the actual load report occurred. This will be guaranteed
    # to include every request reported. Due to system load and delays between
    # the *LoadStatsRequest* sent from Envoy and the *LoadStatsResponse* message
    # sent from the management server, this may be longer than the requested load
    # reporting interval in the *LoadStatsResponse*.
    load_report_interval: timedelta = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class ClusterStatsDroppedRequests(betterproto.Message):
    # Identifier for the policy specifying the drop.
    category: str = betterproto.string_field(1)
    # Total number of deliberately dropped requests for the category.
    dropped_count: int = betterproto.uint64_field(2)


from ....type import v3 as ___type_v3__
from ...core import v3 as __core_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
