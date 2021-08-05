# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/filters/http/squash/v3/squash.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import timedelta

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Squash(betterproto.Message):
    """[#next-free-field: 6]"""

    # The name of the cluster that hosts the Squash server.
    cluster: str = betterproto.string_field(1)
    # When the filter requests the Squash server to create a DebugAttachment, it
    # will use this structure as template for the body of the request. It can
    # contain reference to environment variables in the form of '{{ ENV_VAR_NAME
    # }}'. These can be used to provide the Squash server with more information
    # to find the process to attach the debugger to. For example, in a Istio/k8s
    # environment, this will contain information on the pod: .. code-block:: json
    # {    "spec": {      "attachment": {        "pod": "{{ POD_NAME }}",
    # "namespace": "{{ POD_NAMESPACE }}"      },      "match_request": true    }
    # } (where POD_NAME, POD_NAMESPACE are configured in the pod via the Downward
    # API)
    attachment_template: "betterproto_lib_google_protobuf.Struct" = (
        betterproto.message_field(2)
    )
    # The timeout for individual requests sent to the Squash cluster. Defaults to
    # 1 second.
    request_timeout: timedelta = betterproto.message_field(3)
    # The total timeout Squash will delay a request and wait for it to be
    # attached. Defaults to 60 seconds.
    attachment_timeout: timedelta = betterproto.message_field(4)
    # Amount of time to poll for the status of the attachment object in the
    # Squash server (to check if has been attached). Defaults to 1 second.
    attachment_poll_period: timedelta = betterproto.message_field(5)


import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
