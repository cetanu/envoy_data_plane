# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/type/matcher/v3/http_inputs.proto, envoy/type/matcher/v3/metadata.proto, envoy/type/matcher/v3/node.proto, envoy/type/matcher/v3/number.proto, envoy/type/matcher/v3/path.proto, envoy/type/matcher/v3/regex.proto, envoy/type/matcher/v3/string.proto, envoy/type/matcher/v3/struct.proto, envoy/type/matcher/v3/value.proto
# plugin: python-betterproto
import warnings
from dataclasses import dataclass
from typing import List, Optional

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class RegexMatcher(betterproto.Message):
    """A regex matcher designed for safety when used with untrusted input."""

    # Google's RE2 regex engine.
    google_re2: "RegexMatcherGoogleRe2" = betterproto.message_field(
        1, group="engine_type"
    )
    # The regex match string. The string must be supported by the configured
    # engine.
    regex: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class RegexMatcherGoogleRe2(betterproto.Message):
    """
    Google's `RE2 <https://github.com/google/re2>`_ regex engine. The regex
    string must adhere to the documented `syntax
    <https://github.com/google/re2/wiki/Syntax>`_. The engine is designed to
    complete execution in linear time as well as limit the amount of memory
    used. Envoy supports program size checking via runtime. The runtime keys
    `re2.max_program_size.error_level` and `re2.max_program_size.warn_level`
    can be set to integers as the maximum program size or complexity that a
    compiled regex can have before an exception is thrown or a warning is
    logged, respectively. `re2.max_program_size.error_level` defaults to 100,
    and `re2.max_program_size.warn_level` has no default if unset (will not
    check/log a warning). Envoy emits two stats for tracking the program size
    of regexes: the histogram `re2.program_size`, which records the program
    size, and the counter `re2.exceeded_warn_level`, which is incremented each
    time the program size exceeds the warn level threshold.
    """

    # This field controls the RE2 "program size" which is a rough estimate of how
    # complex a compiled regex is to evaluate. A regex that has a program size
    # greater than the configured value will fail to compile. In this case, the
    # configured max program size can be increased or the regex can be
    # simplified. If not specified, the default is 100. This field is deprecated;
    # regexp validation should be performed on the management server instead of
    # being done by each individual client.
    max_program_size: Optional[int] = betterproto.message_field(
        1, wraps=betterproto.TYPE_UINT32
    )

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.max_program_size:
            warnings.warn(
                "RegexMatcherGoogleRe2.max_program_size is deprecated",
                DeprecationWarning,
            )


@dataclass(eq=False, repr=False)
class RegexMatchAndSubstitute(betterproto.Message):
    """
    Describes how to match a string and then produce a new string using a
    regular expression and a substitution string.
    """

    # The regular expression used to find portions of a string (hereafter called
    # the "subject string") that should be replaced. When a new string is
    # produced during the substitution operation, the new string is initially the
    # same as the subject string, but then all matches in the subject string are
    # replaced by the substitution string. If replacing all matches isn't
    # desired, regular expression anchors can be used to ensure a single match,
    # so as to replace just one occurrence of a pattern. Capture groups can be
    # used in the pattern to extract portions of the subject string, and then
    # referenced in the substitution string.
    pattern: "RegexMatcher" = betterproto.message_field(1)
    # The string that should be substituted into matching portions of the subject
    # string during a substitution operation to produce a new string. Capture
    # groups in the pattern can be referenced in the substitution string. Note,
    # however, that the syntax for referring to capture groups is defined by the
    # chosen regular expression engine. Google's `RE2
    # <https://github.com/google/re2>`_ regular expression engine uses a
    # backslash followed by the capture group number to denote a numbered capture
    # group. E.g., ``\1`` refers to capture group 1, and ``\2`` refers to capture
    # group 2.
    substitution: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class StringMatcher(betterproto.Message):
    """Specifies the way to match a string. [#next-free-field: 8]"""

    # The input string must match exactly the string specified here. Examples: *
    # *abc* only matches the value *abc*.
    exact: str = betterproto.string_field(1, group="match_pattern")
    # The input string must have the prefix specified here. Note: empty prefix is
    # not allowed, please use regex instead. Examples: * *abc* matches the value
    # *abc.xyz*
    prefix: str = betterproto.string_field(2, group="match_pattern")
    # The input string must have the suffix specified here. Note: empty prefix is
    # not allowed, please use regex instead. Examples: * *abc* matches the value
    # *xyz.abc*
    suffix: str = betterproto.string_field(3, group="match_pattern")
    # The input string must match the regular expression specified here.
    safe_regex: "RegexMatcher" = betterproto.message_field(5, group="match_pattern")
    # The input string must have the substring specified here. Note: empty
    # contains match is not allowed, please use regex instead. Examples: * *abc*
    # matches the value *xyz.abc.def*
    contains: str = betterproto.string_field(7, group="match_pattern")
    # If true, indicates the exact/prefix/suffix/contains matching should be case
    # insensitive. This has no effect for the safe_regex match. For example, the
    # matcher *data* will match both input string *Data* and *data* if set to
    # true.
    ignore_case: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class ListStringMatcher(betterproto.Message):
    """Specifies a list of ways to match a string."""

    patterns: List["StringMatcher"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DoubleMatcher(betterproto.Message):
    """Specifies the way to match a double value."""

    # If specified, the input double value must be in the range specified here.
    # Note: The range is using half-open interval semantics [start, end).
    range: "__v3__.DoubleRange" = betterproto.message_field(1, group="match_pattern")
    # If specified, the input double value must be equal to the value specified
    # here.
    exact: float = betterproto.double_field(2, group="match_pattern")


@dataclass(eq=False, repr=False)
class ValueMatcher(betterproto.Message):
    """
    Specifies the way to match a ProtobufWkt::Value. Primitive values and
    ListValue are supported. StructValue is not supported and is always not
    matched. [#next-free-field: 7]
    """

    # If specified, a match occurs if and only if the target value is a
    # NullValue.
    null_match: "ValueMatcherNullMatch" = betterproto.message_field(
        1, group="match_pattern"
    )
    # If specified, a match occurs if and only if the target value is a double
    # value and is matched to this field.
    double_match: "DoubleMatcher" = betterproto.message_field(2, group="match_pattern")
    # If specified, a match occurs if and only if the target value is a string
    # value and is matched to this field.
    string_match: "StringMatcher" = betterproto.message_field(3, group="match_pattern")
    # If specified, a match occurs if and only if the target value is a bool
    # value and is equal to this field.
    bool_match: bool = betterproto.bool_field(4, group="match_pattern")
    # If specified, value match will be performed based on whether the path is
    # referring to a valid primitive value in the metadata. If the path is
    # referring to a non-primitive value, the result is always not matched.
    present_match: bool = betterproto.bool_field(5, group="match_pattern")
    # If specified, a match occurs if and only if the target value is a list
    # value and is matched to this field.
    list_match: "ListMatcher" = betterproto.message_field(6, group="match_pattern")


@dataclass(eq=False, repr=False)
class ValueMatcherNullMatch(betterproto.Message):
    """NullMatch is an empty message to specify a null value."""

    pass


@dataclass(eq=False, repr=False)
class ListMatcher(betterproto.Message):
    """Specifies the way to match a list value."""

    # If specified, at least one of the values in the list must match the value
    # specified.
    one_of: "ValueMatcher" = betterproto.message_field(1, group="match_pattern")


@dataclass(eq=False, repr=False)
class MetadataMatcher(betterproto.Message):
    """[#next-major-version: MetadataMatcher should use StructMatcher]"""

    # The filter name to retrieve the Struct from the Metadata.
    filter: str = betterproto.string_field(1)
    # The path to retrieve the Value from the Struct.
    path: List["MetadataMatcherPathSegment"] = betterproto.message_field(2)
    # The MetadataMatcher is matched if the value retrieved by path is matched to
    # this value.
    value: "ValueMatcher" = betterproto.message_field(3)
    # If true, the match result will be inverted.
    invert: bool = betterproto.bool_field(4)


@dataclass(eq=False, repr=False)
class MetadataMatcherPathSegment(betterproto.Message):
    """
    Specifies the segment in a path to retrieve value from Metadata. Note:
    Currently it's not supported to retrieve a value from a list in Metadata.
    This means that if the segment key refers to a list, it has to be the last
    segment in a path.
    """

    # If specified, use the key to retrieve the value in a Struct.
    key: str = betterproto.string_field(1, group="segment")


@dataclass(eq=False, repr=False)
class PathMatcher(betterproto.Message):
    """Specifies the way to match a path on HTTP request."""

    # The `path` must match the URL path portion of the :path header. The query
    # and fragment string (if present) are removed in the URL path portion. For
    # example, the path */data* will match the *:path* header
    # */data#fragment?param=value*.
    path: "StringMatcher" = betterproto.message_field(1, group="rule")


@dataclass(eq=False, repr=False)
class StructMatcher(betterproto.Message):
    """
    StructMatcher provides a general interface to check if a given value is
    matched in google.protobuf.Struct. It uses `path` to retrieve the value
    from the struct and then check if it's matched to the specified value. For
    example, for the following Struct: .. code-block:: yaml        fields:
    a:            struct_value:              fields:                b:
    struct_value:                    fields:                      c:
    string_value: pro                t:                  list_value:
    values:                      - string_value: m                      -
    string_value: n The following MetadataMatcher is matched as the path [a, b,
    c] will retrieve a string value "pro" from the Metadata which is matched to
    the specified prefix match. .. code-block:: yaml    path:    - key: a    -
    key: b    - key: c    value:      string_match:        prefix: pr The
    following StructMatcher is matched as the code will match one of the string
    values in the list at the path [a, t]. .. code-block:: yaml    path:    -
    key: a    - key: t    value:      list_match:        one_of:
    string_match:            exact: m An example use of StructMatcher is to
    match metadata in envoy.v*.core.Node.
    """

    # The path to retrieve the Value from the Struct.
    path: List["StructMatcherPathSegment"] = betterproto.message_field(2)
    # The StructMatcher is matched if the value retrieved by path is matched to
    # this value.
    value: "ValueMatcher" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class StructMatcherPathSegment(betterproto.Message):
    """Specifies the segment in a path to retrieve value from Struct."""

    # If specified, use the key to retrieve the value in a Struct.
    key: str = betterproto.string_field(1, group="segment")


@dataclass(eq=False, repr=False)
class NodeMatcher(betterproto.Message):
    """Specifies the way to match a Node. The match follows AND semantics."""

    # Specifies match criteria on the node id.
    node_id: "StringMatcher" = betterproto.message_field(1)
    # Specifies match criteria on the node metadata.
    node_metadatas: List["StructMatcher"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class HttpRequestHeaderMatchInput(betterproto.Message):
    """
    Match input indicates that matching should be done on a specific request
    header. The resulting input string will be all headers for the given key
    joined by a comma, e.g. if the request contains two 'foo' headers with
    value 'bar' and 'baz', the input string will be 'bar,baz'.
    [#comment:TODO(snowp): Link to unified matching docs.]
    """

    # The request header to match on.
    header_name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class HttpRequestTrailerMatchInput(betterproto.Message):
    """
    Match input indicates that matching should be done on a specific request
    trailer. The resulting input string will be all headers for the given key
    joined by a comma, e.g. if the request contains two 'foo' headers with
    value 'bar' and 'baz', the input string will be 'bar,baz'.
    [#comment:TODO(snowp): Link to unified matching docs.]
    """

    # The request trailer to match on.
    header_name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class HttpResponseHeaderMatchInput(betterproto.Message):
    """
    Match input indicating that matching should be done on a specific response
    header. The resulting input string will be all headers for the given key
    joined by a comma, e.g. if the response contains two 'foo' headers with
    value 'bar' and 'baz', the input string will be 'bar,baz'.
    [#comment:TODO(snowp): Link to unified matching docs.]
    """

    # The response header to match on.
    header_name: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class HttpResponseTrailerMatchInput(betterproto.Message):
    """
    Match input indicates that matching should be done on a specific response
    trailer. The resulting input string will be all headers for the given key
    joined by a comma, e.g. if the request contains two 'foo' headers with
    value 'bar' and 'baz', the input string will be 'bar,baz'.
    [#comment:TODO(snowp): Link to unified matching docs.]
    """

    # The response trailer to match on.
    header_name: str = betterproto.string_field(1)


from ... import v3 as __v3__
