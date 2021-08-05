# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/internal_redirect/safe_cross_scheme/v3/safe_cross_scheme_config.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class SafeCrossSchemeConfig(betterproto.Message):
    """
    An internal redirect predicate that checks the scheme between the
    downstream url and the redirect target url and allows a) same scheme
    redirect and b) safe cross scheme redirect, which means if the downstream
    scheme is HTTPS, both HTTPS and HTTP redirect targets are allowed, but if
    the downstream scheme is HTTP, only HTTP redirect targets are allowed.
    [#extension: envoy.internal_redirect_predicates.safe_cross_scheme]
    """

    pass