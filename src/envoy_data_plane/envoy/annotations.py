# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/annotations/resource.proto, envoy/annotations/deprecation.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ResourceAnnotation(betterproto.Message):
    # Annotation for xDS services that indicates the fully-qualified Protobuf
    # type for the resource type.
    type: str = betterproto.string_field(1)
