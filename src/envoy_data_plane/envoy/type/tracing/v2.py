# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/type/tracing/v2/custom_tag.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from envoy_data_plane.envoy.type.metadata import v2


@dataclass
class CustomTag(betterproto.Message):
    """Describes custom tags for the active span. [#next-free-field: 6]"""

    # Used to populate the tag name.
    tag: str = betterproto.string_field(1)
    # A literal custom tag.
    literal: "CustomTagLiteral" = betterproto.message_field(2, group="type")
    # An environment custom tag.
    environment: "CustomTagEnvironment" = betterproto.message_field(3, group="type")
    # A request header custom tag.
    request_header: "CustomTagHeader" = betterproto.message_field(4, group="type")
    # A custom tag to obtain tag value from the metadata.
    metadata: "CustomTagMetadata" = betterproto.message_field(5, group="type")


@dataclass
class CustomTagLiteral(betterproto.Message):
    """Literal type custom tag with static value for the tag value."""

    # Static literal value to populate the tag value.
    value: str = betterproto.string_field(1)


@dataclass
class CustomTagEnvironment(betterproto.Message):
    """Environment type custom tag with environment name and default value."""

    # Environment variable name to obtain the value to populate the tag value.
    name: str = betterproto.string_field(1)
    # When the environment variable is not found, the tag value will be populated
    # with this default value if specified, otherwise no tag will be populated.
    default_value: str = betterproto.string_field(2)


@dataclass
class CustomTagHeader(betterproto.Message):
    """Header type custom tag with header name and default value."""

    # Header name to obtain the value to populate the tag value.
    name: str = betterproto.string_field(1)
    # When the header does not exist, the tag value will be populated with this
    # default value if specified, otherwise no tag will be populated.
    default_value: str = betterproto.string_field(2)


@dataclass
class CustomTagMetadata(betterproto.Message):
    """
    Metadata type custom tag using :ref:`MetadataKey
    <envoy_api_msg_type.metadata.v2.MetadataKey>` to retrieve the protobuf
    value from :ref:`Metadata <envoy_api_msg_core.Metadata>`, and populate the
    tag value with `the canonical JSON <https://developers.google.com/protocol-
    buffers/docs/proto3#json>`_ representation of it.
    """

    # Specify what kind of metadata to obtain tag value from.
    kind: v2.MetadataKind = betterproto.message_field(1)
    # Metadata key to define the path to retrieve the tag value.
    metadata_key: v2.MetadataKey = betterproto.message_field(2)
    # When no valid metadata is found, the tag value would be populated with this
    # default value if specified, otherwise no tag would be populated.
    default_value: str = betterproto.string_field(3)