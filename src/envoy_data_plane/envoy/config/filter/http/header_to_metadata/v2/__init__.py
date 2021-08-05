# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/filter/http/header_to_metadata/v2/header_to_metadata.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class ConfigValueType(betterproto.Enum):
    STRING = 0
    NUMBER = 1
    PROTOBUF_VALUE = 2


class ConfigValueEncode(betterproto.Enum):
    NONE = 0
    BASE64 = 1


@dataclass(eq=False, repr=False)
class Config(betterproto.Message):
    # The list of rules to apply to requests.
    request_rules: List["ConfigRule"] = betterproto.message_field(1)
    # The list of rules to apply to responses.
    response_rules: List["ConfigRule"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class ConfigKeyValuePair(betterproto.Message):
    """[#next-free-field: 6]"""

    # The namespace — if this is empty, the filter's namespace will be used.
    metadata_namespace: str = betterproto.string_field(1)
    # The key to use within the namespace.
    key: str = betterproto.string_field(2)
    # The value to pair with the given key. When used for a `on_header_present`
    # case, if value is non-empty it'll be used instead of the header value. If
    # both are empty, no metadata is added. When used for a `on_header_missing`
    # case, a non-empty value must be provided otherwise no metadata is added.
    value: str = betterproto.string_field(3)
    # The value's type — defaults to string.
    type: "ConfigValueType" = betterproto.enum_field(4)
    # How is the value encoded, default is NONE (not encoded). The value will be
    # decoded accordingly before storing to metadata.
    encode: "ConfigValueEncode" = betterproto.enum_field(5)


@dataclass(eq=False, repr=False)
class ConfigRule(betterproto.Message):
    """
    A Rule defines what metadata to apply when a header is present or missing.
    """

    # The header that triggers this rule — required.
    header: str = betterproto.string_field(1)
    # If the header is present, apply this metadata KeyValuePair. If the value in
    # the KeyValuePair is non-empty, it'll be used instead of the header value.
    on_header_present: "ConfigKeyValuePair" = betterproto.message_field(2)
    # If the header is not present, apply this metadata KeyValuePair. The value
    # in the KeyValuePair must be set, since it'll be used in lieu of the missing
    # header value.
    on_header_missing: "ConfigKeyValuePair" = betterproto.message_field(3)
    # Whether or not to remove the header after a rule is applied. This prevents
    # headers from leaking.
    remove: bool = betterproto.bool_field(4)