# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/config/common/matcher/v3/matcher.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class Matcher(betterproto.Message):
    """
    A matcher, which may traverse a matching tree in order to result in a match
    action. During matching, the tree will be traversed until a match is found,
    or if no match is found the action specified by the most specific
    on_no_match will be evaluated. As an on_no_match might result in another
    matching tree being evaluated, this process might repeat several times
    until the final OnMatch (or no match) is decided.
    """

    # A linear list of matchers to evaluate.
    matcher_list: "MatcherMatcherList" = betterproto.message_field(
        1, group="matcher_type"
    )
    # A match tree to evaluate.
    matcher_tree: "MatcherMatcherTree" = betterproto.message_field(
        2, group="matcher_type"
    )
    # Optional OnMatch to use if the matcher failed. If specified, the OnMatch is
    # used, and the matcher is considered to have matched. If not specified, the
    # matcher is considered not to have matched.
    on_no_match: "MatcherOnMatch" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class MatcherOnMatch(betterproto.Message):
    """What to do if a match is successful."""

    # Nested matcher to evaluate. If the nested matcher does not match and does
    # not specify on_no_match, then this matcher is considered not to have
    # matched, even if a predicate at this level or above returned true.
    matcher: "Matcher" = betterproto.message_field(1, group="on_match")
    # Protocol-specific action to take.
    action: "___core_v3__.TypedExtensionConfig" = betterproto.message_field(
        2, group="on_match"
    )


@dataclass(eq=False, repr=False)
class MatcherMatcherList(betterproto.Message):
    """
    A linear list of field matchers. The field matchers are evaluated in order,
    and the first match wins.
    """

    # A list of matchers. First match wins.
    matchers: List["MatcherMatcherListFieldMatcher"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MatcherMatcherListPredicate(betterproto.Message):
    """Predicate to determine if a match is successful."""

    # A single predicate to evaluate.
    single_predicate: "MatcherMatcherListPredicateSinglePredicate" = (
        betterproto.message_field(1, group="match_type")
    )
    # A list of predicates to be OR-ed together.
    or_matcher: "MatcherMatcherListPredicatePredicateList" = betterproto.message_field(
        2, group="match_type"
    )
    # A list of predicates to be AND-ed together.
    and_matcher: "MatcherMatcherListPredicatePredicateList" = betterproto.message_field(
        3, group="match_type"
    )
    # The invert of a predicate
    not_matcher: "MatcherMatcherListPredicate" = betterproto.message_field(
        4, group="match_type"
    )


@dataclass(eq=False, repr=False)
class MatcherMatcherListPredicateSinglePredicate(betterproto.Message):
    """Predicate for a single input field."""

    # Protocol-specific specification of input field to match on. [#extension-
    # category: envoy.matching.common_inputs]
    input: "___core_v3__.TypedExtensionConfig" = betterproto.message_field(1)
    # Built-in string matcher.
    value_match: "____type_matcher_v3__.StringMatcher" = betterproto.message_field(
        2, group="matcher"
    )
    # Extension for custom matching logic. [#extension-category:
    # envoy.matching.input_matchers]
    custom_match: "___core_v3__.TypedExtensionConfig" = betterproto.message_field(
        3, group="matcher"
    )


@dataclass(eq=False, repr=False)
class MatcherMatcherListPredicatePredicateList(betterproto.Message):
    """
    A list of two or more matchers. Used to allow using a list within a oneof.
    """

    predicate: List["MatcherMatcherListPredicate"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class MatcherMatcherListFieldMatcher(betterproto.Message):
    """An individual matcher."""

    # Determines if the match succeeds.
    predicate: "MatcherMatcherListPredicate" = betterproto.message_field(1)
    # What to do if the match succeeds.
    on_match: "MatcherOnMatch" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MatcherMatcherTree(betterproto.Message):
    # Protocol-specific specification of input field to match on.
    input: "___core_v3__.TypedExtensionConfig" = betterproto.message_field(1)
    exact_match_map: "MatcherMatcherTreeMatchMap" = betterproto.message_field(
        2, group="tree_type"
    )
    # Longest matching prefix wins.
    prefix_match_map: "MatcherMatcherTreeMatchMap" = betterproto.message_field(
        3, group="tree_type"
    )
    # Extension for custom matching logic.
    custom_match: "___core_v3__.TypedExtensionConfig" = betterproto.message_field(
        4, group="tree_type"
    )


@dataclass(eq=False, repr=False)
class MatcherMatcherTreeMatchMap(betterproto.Message):
    """
    A map of configured matchers. Used to allow using a map within a oneof.
    """

    map: Dict[str, "MatcherOnMatch"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass(eq=False, repr=False)
class MatchPredicate(betterproto.Message):
    """
    Match configuration. This is a recursive structure which allows complex
    nested match configurations to be built using various logical operators.
    [#next-free-field: 11]
    """

    # A set that describes a logical OR. If any member of the set matches, the
    # match configuration matches.
    or_match: "MatchPredicateMatchSet" = betterproto.message_field(1, group="rule")
    # A set that describes a logical AND. If all members of the set match, the
    # match configuration matches.
    and_match: "MatchPredicateMatchSet" = betterproto.message_field(2, group="rule")
    # A negation match. The match configuration will match if the negated match
    # condition matches.
    not_match: "MatchPredicate" = betterproto.message_field(3, group="rule")
    # The match configuration will always match.
    any_match: bool = betterproto.bool_field(4, group="rule")
    # HTTP request headers match configuration.
    http_request_headers_match: "HttpHeadersMatch" = betterproto.message_field(
        5, group="rule"
    )
    # HTTP request trailers match configuration.
    http_request_trailers_match: "HttpHeadersMatch" = betterproto.message_field(
        6, group="rule"
    )
    # HTTP response headers match configuration.
    http_response_headers_match: "HttpHeadersMatch" = betterproto.message_field(
        7, group="rule"
    )
    # HTTP response trailers match configuration.
    http_response_trailers_match: "HttpHeadersMatch" = betterproto.message_field(
        8, group="rule"
    )
    # HTTP request generic body match configuration.
    http_request_generic_body_match: "HttpGenericBodyMatch" = betterproto.message_field(
        9, group="rule"
    )
    # HTTP response generic body match configuration.
    http_response_generic_body_match: "HttpGenericBodyMatch" = (
        betterproto.message_field(10, group="rule")
    )


@dataclass(eq=False, repr=False)
class MatchPredicateMatchSet(betterproto.Message):
    """A set of match configurations used for logical operations."""

    # The list of rules that make up the set.
    rules: List["MatchPredicate"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class HttpHeadersMatch(betterproto.Message):
    """HTTP headers match configuration."""

    # HTTP headers to match.
    headers: List["___route_v3__.HeaderMatcher"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class HttpGenericBodyMatch(betterproto.Message):
    """
    HTTP generic body match configuration. List of text strings and hex strings
    to be located in HTTP body. All specified strings must be found in the HTTP
    body for positive match. The search may be limited to specified number of
    bytes from the body start. .. attention::   Searching for patterns in HTTP
    body is potentially cpu intensive. For each specified pattern, http body is
    scanned byte by byte to find a match.   If multiple patterns are specified,
    the process is repeated for each pattern. If location of a pattern is
    known, ``bytes_limit`` should be specified   to scan only part of the http
    body.
    """

    # Limits search to specified number of bytes - default zero (no limit - match
    # entire captured buffer).
    bytes_limit: int = betterproto.uint32_field(1)
    # List of patterns to match.
    patterns: List["HttpGenericBodyMatchGenericTextMatch"] = betterproto.message_field(
        2
    )


@dataclass(eq=False, repr=False)
class HttpGenericBodyMatchGenericTextMatch(betterproto.Message):
    # Text string to be located in HTTP body.
    string_match: str = betterproto.string_field(1, group="rule")
    # Sequence of bytes to be located in HTTP body.
    binary_match: bytes = betterproto.bytes_field(2, group="rule")


from .....type.matcher import v3 as ____type_matcher_v3__
from ....core import v3 as ___core_v3__
from ....route import v3 as ___route_v3__
