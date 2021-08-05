# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/access_loggers/open_telemetry/v4alpha/logs_service.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class OpenTelemetryAccessLogConfig(betterproto.Message):
    """
    Configuration for the built-in *envoy.access_loggers.open_telemetry*
    :ref:`AccessLog <envoy_api_msg_config.accesslog.v4alpha.AccessLog>`. This
    configuration will populate `opentelemetry.proto.collector.v1.logs.ExportLo
    gsServiceRequest.resource_logs <https://github.com/open-
    telemetry/opentelemetry-proto/blob/main/opentelemetry/proto/collector/logs/
    v1/logs_service.proto>`_. OpenTelemetry `Resource <https://github.com/open-
    telemetry/opentelemetry-
    proto/blob/main/opentelemetry/proto/resource/v1/resource.proto>`_
    attributes are filled with Envoy node info. In addition, the request start
    time is set in the dedicated field. [#extension:
    envoy.access_loggers.open_telemetry] [#comment:TODO(itamarkam): allow
    configuration for resource attributes.]
    """

    # [#comment:TODO(itamarkam): add 'filter_state_objects_to_log' to logs.]
    common_config: "__grpc_v4_alpha__.CommonGrpcAccessLogConfig" = (
        betterproto.message_field(1)
    )
    # OpenTelemetry `LogResource <https://github.com/open-
    # telemetry/opentelemetry-
    # proto/blob/main/opentelemetry/proto/logs/v1/logs.proto>`_ fields, following
    # `Envoy access logging formatting <https://www.envoyproxy.io/docs/envoy/late
    # st/configuration/observability/access_log/usage>`_. See 'body' in the
    # LogResource proto for more details. Example: ``body { string_value:
    # "%PROTOCOL%" }``.
    body: "_____opentelemetry_proto_common_v1__.AnyValue" = betterproto.message_field(2)
    # See 'attributes' in the LogResource proto for more details. Example:
    # ``attributes { values { key: "user_agent" value { string_value: "%REQ(USER-
    # AGENT)%" } } }``.
    attributes: "_____opentelemetry_proto_common_v1__.KeyValueList" = (
        betterproto.message_field(3)
    )


from ......opentelemetry.proto.common import v1 as _____opentelemetry_proto_common_v1__
from ...grpc import v4alpha as __grpc_v4_alpha__
