# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: validate/validate.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


class KnownRegex(betterproto.Enum):
    """WellKnownRegex contain some well-known patterns."""

    UNKNOWN = 0
    # HTTP header name as defined by RFC 7230.
    HTTP_HEADER_NAME = 1
    # HTTP header value as defined by RFC 7230.
    HTTP_HEADER_VALUE = 2


@dataclass(eq=False, repr=False)
class FieldRules(betterproto.Message):
    """
    FieldRules encapsulates the rules for each type of field. Depending on the
    field, the correct set should be used to ensure proper validations.
    """

    message: "MessageRules" = betterproto.message_field(17)
    # Scalar Field Types
    float: "FloatRules" = betterproto.message_field(1, group="type")
    double: "DoubleRules" = betterproto.message_field(2, group="type")
    int32: "Int32Rules" = betterproto.message_field(3, group="type")
    int64: "Int64Rules" = betterproto.message_field(4, group="type")
    uint32: "UInt32Rules" = betterproto.message_field(5, group="type")
    uint64: "UInt64Rules" = betterproto.message_field(6, group="type")
    sint32: "SInt32Rules" = betterproto.message_field(7, group="type")
    sint64: "SInt64Rules" = betterproto.message_field(8, group="type")
    fixed32: "Fixed32Rules" = betterproto.message_field(9, group="type")
    fixed64: "Fixed64Rules" = betterproto.message_field(10, group="type")
    sfixed32: "SFixed32Rules" = betterproto.message_field(11, group="type")
    sfixed64: "SFixed64Rules" = betterproto.message_field(12, group="type")
    bool: "BoolRules" = betterproto.message_field(13, group="type")
    string: "StringRules" = betterproto.message_field(14, group="type")
    bytes: "BytesRules" = betterproto.message_field(15, group="type")
    # Complex Field Types
    enum: "EnumRules" = betterproto.message_field(16, group="type")
    repeated: "RepeatedRules" = betterproto.message_field(18, group="type")
    map: "MapRules" = betterproto.message_field(19, group="type")
    # Well-Known Field Types
    any: "AnyRules" = betterproto.message_field(20, group="type")
    duration: "DurationRules" = betterproto.message_field(21, group="type")
    timestamp: "TimestampRules" = betterproto.message_field(22, group="type")


@dataclass(eq=False, repr=False)
class FloatRules(betterproto.Message):
    """FloatRules describes the constraints applied to `float` values"""

    # Const specifies that this field must be exactly the specified value
    const: float = betterproto.float_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: float = betterproto.float_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: float = betterproto.float_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: float = betterproto.float_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: float = betterproto.float_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[float] = betterproto.float_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[float] = betterproto.float_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class DoubleRules(betterproto.Message):
    """DoubleRules describes the constraints applied to `double` values"""

    # Const specifies that this field must be exactly the specified value
    const: float = betterproto.double_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: float = betterproto.double_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: float = betterproto.double_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: float = betterproto.double_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: float = betterproto.double_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[float] = betterproto.double_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[float] = betterproto.double_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class Int32Rules(betterproto.Message):
    """Int32Rules describes the constraints applied to `int32` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.int32_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.int32_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.int32_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.int32_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.int32_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.int32_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.int32_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class Int64Rules(betterproto.Message):
    """Int64Rules describes the constraints applied to `int64` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.int64_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.int64_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.int64_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.int64_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.int64_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.int64_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.int64_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class UInt32Rules(betterproto.Message):
    """UInt32Rules describes the constraints applied to `uint32` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.uint32_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.uint32_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.uint32_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.uint32_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.uint32_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.uint32_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.uint32_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class UInt64Rules(betterproto.Message):
    """UInt64Rules describes the constraints applied to `uint64` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.uint64_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.uint64_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.uint64_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.uint64_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.uint64_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.uint64_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.uint64_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class SInt32Rules(betterproto.Message):
    """SInt32Rules describes the constraints applied to `sint32` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.sint32_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.sint32_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.sint32_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.sint32_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.sint32_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.sint32_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.sint32_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class SInt64Rules(betterproto.Message):
    """SInt64Rules describes the constraints applied to `sint64` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.sint64_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.sint64_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.sint64_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.sint64_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.sint64_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.sint64_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.sint64_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class Fixed32Rules(betterproto.Message):
    """Fixed32Rules describes the constraints applied to `fixed32` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.fixed32_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.fixed32_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.fixed32_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.fixed32_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.fixed32_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.fixed32_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.fixed32_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class Fixed64Rules(betterproto.Message):
    """Fixed64Rules describes the constraints applied to `fixed64` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.fixed64_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.fixed64_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.fixed64_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.fixed64_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.fixed64_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.fixed64_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.fixed64_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class SFixed32Rules(betterproto.Message):
    """SFixed32Rules describes the constraints applied to `sfixed32` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.sfixed32_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.sfixed32_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.sfixed32_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.sfixed32_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.sfixed32_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.sfixed32_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.sfixed32_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class SFixed64Rules(betterproto.Message):
    """SFixed64Rules describes the constraints applied to `sfixed64` values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.sfixed64_field(1)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: int = betterproto.sfixed64_field(2)
    # Lte specifies that this field must be less than or equal to the specified
    # value, inclusive
    lte: int = betterproto.sfixed64_field(3)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive. If the value of Gt is larger than a specified Lt or Lte, the
    # range is reversed.
    gt: int = betterproto.sfixed64_field(4)
    # Gte specifies that this field must be greater than or equal to the
    # specified value, inclusive. If the value of Gte is larger than a specified
    # Lt or Lte, the range is reversed.
    gte: int = betterproto.sfixed64_field(5)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.sfixed64_field(6)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.sfixed64_field(7)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class BoolRules(betterproto.Message):
    """BoolRules describes the constraints applied to `bool` values"""

    # Const specifies that this field must be exactly the specified value
    const: bool = betterproto.bool_field(1)


@dataclass(eq=False, repr=False)
class StringRules(betterproto.Message):
    """StringRules describe the constraints applied to `string` values"""

    # Const specifies that this field must be exactly the specified value
    const: str = betterproto.string_field(1)
    # Len specifies that this field must be the specified number of characters
    # (Unicode code points). Note that the number of characters may differ from
    # the number of bytes in the string.
    len: int = betterproto.uint64_field(19)
    # MinLen specifies that this field must be the specified number of characters
    # (Unicode code points) at a minimum. Note that the number of characters may
    # differ from the number of bytes in the string.
    min_len: int = betterproto.uint64_field(2)
    # MaxLen specifies that this field must be the specified number of characters
    # (Unicode code points) at a maximum. Note that the number of characters may
    # differ from the number of bytes in the string.
    max_len: int = betterproto.uint64_field(3)
    # LenBytes specifies that this field must be the specified number of bytes
    len_bytes: int = betterproto.uint64_field(20)
    # MinBytes specifies that this field must be the specified number of bytes at
    # a minimum
    min_bytes: int = betterproto.uint64_field(4)
    # MaxBytes specifies that this field must be the specified number of bytes at
    # a maximum
    max_bytes: int = betterproto.uint64_field(5)
    # Pattern specifes that this field must match against the specified regular
    # expression (RE2 syntax). The included expression should elide any
    # delimiters.
    pattern: str = betterproto.string_field(6)
    # Prefix specifies that this field must have the specified substring at the
    # beginning of the string.
    prefix: str = betterproto.string_field(7)
    # Suffix specifies that this field must have the specified substring at the
    # end of the string.
    suffix: str = betterproto.string_field(8)
    # Contains specifies that this field must have the specified substring
    # anywhere in the string.
    contains: str = betterproto.string_field(9)
    # NotContains specifies that this field cannot have the specified substring
    # anywhere in the string.
    not_contains: str = betterproto.string_field(23)
    # In specifies that this field must be equal to one of the specified values
    in_: List[str] = betterproto.string_field(10)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[str] = betterproto.string_field(11)
    # Email specifies that the field must be a valid email address as defined by
    # RFC 5322
    email: bool = betterproto.bool_field(12, group="well_known")
    # Hostname specifies that the field must be a valid hostname as defined by
    # RFC 1034. This constraint does not support internationalized domain names
    # (IDNs).
    hostname: bool = betterproto.bool_field(13, group="well_known")
    # Ip specifies that the field must be a valid IP (v4 or v6) address. Valid
    # IPv6 addresses should not include surrounding square brackets.
    ip: bool = betterproto.bool_field(14, group="well_known")
    # Ipv4 specifies that the field must be a valid IPv4 address.
    ipv4: bool = betterproto.bool_field(15, group="well_known")
    # Ipv6 specifies that the field must be a valid IPv6 address. Valid IPv6
    # addresses should not include surrounding square brackets.
    ipv6: bool = betterproto.bool_field(16, group="well_known")
    # Uri specifies that the field must be a valid, absolute URI as defined by
    # RFC 3986
    uri: bool = betterproto.bool_field(17, group="well_known")
    # UriRef specifies that the field must be a valid URI as defined by RFC 3986
    # and may be relative or absolute.
    uri_ref: bool = betterproto.bool_field(18, group="well_known")
    # Address specifies that the field must be either a valid hostname as defined
    # by RFC 1034 (which does not support internationalized domain names or
    # IDNs), or it can be a valid IP (v4 or v6).
    address: bool = betterproto.bool_field(21, group="well_known")
    # Uuid specifies that the field must be a valid UUID as defined by RFC 4122
    uuid: bool = betterproto.bool_field(22, group="well_known")
    # WellKnownRegex specifies a common well known pattern defined as a regex.
    well_known_regex: "KnownRegex" = betterproto.enum_field(24, group="well_known")
    # This applies to regexes HTTP_HEADER_NAME and HTTP_HEADER_VALUE to enable
    # strict header validation. By default, this is true, and HTTP header
    # validations are RFC-compliant. Setting to false will enable a looser
    # validations that only disallows \r\n\0 characters, which can be used to
    # bypass header matching rules.
    strict: bool = betterproto.bool_field(25)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(26)


@dataclass(eq=False, repr=False)
class BytesRules(betterproto.Message):
    """BytesRules describe the constraints applied to `bytes` values"""

    # Const specifies that this field must be exactly the specified value
    const: bytes = betterproto.bytes_field(1)
    # Len specifies that this field must be the specified number of bytes
    len: int = betterproto.uint64_field(13)
    # MinLen specifies that this field must be the specified number of bytes at a
    # minimum
    min_len: int = betterproto.uint64_field(2)
    # MaxLen specifies that this field must be the specified number of bytes at a
    # maximum
    max_len: int = betterproto.uint64_field(3)
    # Pattern specifes that this field must match against the specified regular
    # expression (RE2 syntax). The included expression should elide any
    # delimiters.
    pattern: str = betterproto.string_field(4)
    # Prefix specifies that this field must have the specified bytes at the
    # beginning of the string.
    prefix: bytes = betterproto.bytes_field(5)
    # Suffix specifies that this field must have the specified bytes at the end
    # of the string.
    suffix: bytes = betterproto.bytes_field(6)
    # Contains specifies that this field must have the specified bytes anywhere
    # in the string.
    contains: bytes = betterproto.bytes_field(7)
    # In specifies that this field must be equal to one of the specified values
    in_: List[bytes] = betterproto.bytes_field(8)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[bytes] = betterproto.bytes_field(9)
    # Ip specifies that the field must be a valid IP (v4 or v6) address in byte
    # format
    ip: bool = betterproto.bool_field(10, group="well_known")
    # Ipv4 specifies that the field must be a valid IPv4 address in byte format
    ipv4: bool = betterproto.bool_field(11, group="well_known")
    # Ipv6 specifies that the field must be a valid IPv6 address in byte format
    ipv6: bool = betterproto.bool_field(12, group="well_known")
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(14)


@dataclass(eq=False, repr=False)
class EnumRules(betterproto.Message):
    """EnumRules describe the constraints applied to enum values"""

    # Const specifies that this field must be exactly the specified value
    const: int = betterproto.int32_field(1)
    # DefinedOnly specifies that this field must be only one of the defined
    # values for this enum, failing on any undefined value.
    defined_only: bool = betterproto.bool_field(2)
    # In specifies that this field must be equal to one of the specified values
    in_: List[int] = betterproto.int32_field(3)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[int] = betterproto.int32_field(4)


@dataclass(eq=False, repr=False)
class MessageRules(betterproto.Message):
    """
    MessageRules describe the constraints applied to embedded message values.
    For message-type fields, validation is performed recursively.
    """

    # Skip specifies that the validation rules of this field should not be
    # evaluated
    skip: bool = betterproto.bool_field(1)
    # Required specifies that this field must be set
    required: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class RepeatedRules(betterproto.Message):
    """RepeatedRules describe the constraints applied to `repeated` values"""

    # MinItems specifies that this field must have the specified number of items
    # at a minimum
    min_items: int = betterproto.uint64_field(1)
    # MaxItems specifies that this field must have the specified number of items
    # at a maximum
    max_items: int = betterproto.uint64_field(2)
    # Unique specifies that all elements in this field must be unique. This
    # contraint is only applicable to scalar and enum types (messages are not
    # supported).
    unique: bool = betterproto.bool_field(3)
    # Items specifies the contraints to be applied to each item in the field.
    # Repeated message fields will still execute validation against each item
    # unless skip is specified here.
    items: "FieldRules" = betterproto.message_field(4)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class MapRules(betterproto.Message):
    """MapRules describe the constraints applied to `map` values"""

    # MinPairs specifies that this field must have the specified number of KVs at
    # a minimum
    min_pairs: int = betterproto.uint64_field(1)
    # MaxPairs specifies that this field must have the specified number of KVs at
    # a maximum
    max_pairs: int = betterproto.uint64_field(2)
    # NoSparse specifies values in this field cannot be unset. This only applies
    # to map's with message value types.
    no_sparse: bool = betterproto.bool_field(3)
    # Keys specifies the constraints to be applied to each key in the field.
    keys: "FieldRules" = betterproto.message_field(4)
    # Values specifies the constraints to be applied to the value of each key in
    # the field. Message values will still have their validations evaluated
    # unless skip is specified here.
    values: "FieldRules" = betterproto.message_field(5)
    # IgnoreEmpty specifies that the validation rules of this field should be
    # evaluated only if the field is not empty
    ignore_empty: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class AnyRules(betterproto.Message):
    """
    AnyRules describe constraints applied exclusively to the
    `google.protobuf.Any` well-known type
    """

    # Required specifies that this field must be set
    required: bool = betterproto.bool_field(1)
    # In specifies that this field's `type_url` must be equal to one of the
    # specified values.
    in_: List[str] = betterproto.string_field(2)
    # NotIn specifies that this field's `type_url` must not be equal to any of
    # the specified values.
    not_in: List[str] = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class DurationRules(betterproto.Message):
    """
    DurationRules describe the constraints applied exclusively to the
    `google.protobuf.Duration` well-known type
    """

    # Required specifies that this field must be set
    required: bool = betterproto.bool_field(1)
    # Const specifies that this field must be exactly the specified value
    const: timedelta = betterproto.message_field(2)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: timedelta = betterproto.message_field(3)
    # Lt specifies that this field must be less than the specified value,
    # inclusive
    lte: timedelta = betterproto.message_field(4)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive
    gt: timedelta = betterproto.message_field(5)
    # Gte specifies that this field must be greater than the specified value,
    # inclusive
    gte: timedelta = betterproto.message_field(6)
    # In specifies that this field must be equal to one of the specified values
    in_: List[timedelta] = betterproto.message_field(7)
    # NotIn specifies that this field cannot be equal to one of the specified
    # values
    not_in: List[timedelta] = betterproto.message_field(8)


@dataclass(eq=False, repr=False)
class TimestampRules(betterproto.Message):
    """
    TimestampRules describe the constraints applied exclusively to the
    `google.protobuf.Timestamp` well-known type
    """

    # Required specifies that this field must be set
    required: bool = betterproto.bool_field(1)
    # Const specifies that this field must be exactly the specified value
    const: datetime = betterproto.message_field(2)
    # Lt specifies that this field must be less than the specified value,
    # exclusive
    lt: datetime = betterproto.message_field(3)
    # Lte specifies that this field must be less than the specified value,
    # inclusive
    lte: datetime = betterproto.message_field(4)
    # Gt specifies that this field must be greater than the specified value,
    # exclusive
    gt: datetime = betterproto.message_field(5)
    # Gte specifies that this field must be greater than the specified value,
    # inclusive
    gte: datetime = betterproto.message_field(6)
    # LtNow specifies that this must be less than the current time. LtNow can
    # only be used with the Within rule.
    lt_now: bool = betterproto.bool_field(7)
    # GtNow specifies that this must be greater than the current time. GtNow can
    # only be used with the Within rule.
    gt_now: bool = betterproto.bool_field(8)
    # Within specifies that this field must be within this duration of the
    # current time. This constraint can be used alone or with the LtNow and GtNow
    # rules.
    within: timedelta = betterproto.message_field(9)
