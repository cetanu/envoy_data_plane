# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: xds/annotations/v3/status.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class PackageVersionStatus(betterproto.Enum):
    # Unknown package version status.
    UNKNOWN = 0
    # This version of the package is frozen.
    FROZEN = 1
    # This version of the package is the active development version.
    ACTIVE = 2
    # This version of the package is the candidate for the next major version. It
    # is typically machine generated from the active development version.
    NEXT_MAJOR_VERSION_CANDIDATE = 3


@dataclass(eq=False, repr=False)
class FileStatusAnnotation(betterproto.Message):
    # The entity is work-in-progress and subject to breaking changes.
    work_in_progress: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class MessageStatusAnnotation(betterproto.Message):
    # The entity is work-in-progress and subject to breaking changes.
    work_in_progress: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class FieldStatusAnnotation(betterproto.Message):
    # The entity is work-in-progress and subject to breaking changes.
    work_in_progress: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class StatusAnnotation(betterproto.Message):
    # The entity is work-in-progress and subject to breaking changes.
    work_in_progress: bool = betterproto.bool_field(1)
    # The entity belongs to a package with the given version status.
    package_version_status: "PackageVersionStatus" = betterproto.enum_field(2)