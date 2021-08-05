# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/service/auth/v4alpha/attribute_context.proto, envoy/service/auth/v4alpha/external_auth.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase
import grpclib


@dataclass(eq=False, repr=False)
class AttributeContext(betterproto.Message):
    """
    An attribute is a piece of metadata that describes an activity on a
    network. For example, the size of an HTTP request, or the status code of an
    HTTP response. Each attribute has a type and a name, which is logically
    defined as a proto message field of the `AttributeContext`. The
    `AttributeContext` is a collection of individual attributes supported by
    Envoy authorization system. [#comment: The following items are left out of
    this proto Request.Auth field for jwt tokens Request.Api for api management
    Origin peer that originated the request Caching Protocol request_context
    return values to inject back into the filter chain peer.claims -- from
    X.509 extensions Configuration - field mask to send - which return values
    from request_context are copied back - which return values are copied into
    request_headers] [#next-free-field: 12]
    """

    # The source of a network activity, such as starting a TCP connection. In a
    # multi hop network activity, the source represents the sender of the last
    # hop.
    source: "AttributeContextPeer" = betterproto.message_field(1)
    # The destination of a network activity, such as accepting a TCP connection.
    # In a multi hop network activity, the destination represents the receiver of
    # the last hop.
    destination: "AttributeContextPeer" = betterproto.message_field(2)
    # Represents a network request, such as an HTTP request.
    request: "AttributeContextRequest" = betterproto.message_field(4)
    # This is analogous to http_request.headers, however these contents will not
    # be sent to the upstream server. Context_extensions provide an extension
    # mechanism for sending additional information to the auth server without
    # modifying the proto definition. It maps to the internal opaque context in
    # the filter chain.
    context_extensions: Dict[str, str] = betterproto.map_field(
        10, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    # Dynamic metadata associated with the request.
    metadata_context: "___config_core_v4_alpha__.Metadata" = betterproto.message_field(
        11
    )


@dataclass(eq=False, repr=False)
class AttributeContextPeer(betterproto.Message):
    """
    This message defines attributes for a node that handles a network request.
    The node can be either a service or an application that sends, forwards, or
    receives the request. Service peers should fill in the `service`,
    `principal`, and `labels` as appropriate. [#next-free-field: 6]
    """

    # The address of the peer, this is typically the IP address. It can also be
    # UDS path, or others.
    address: "___config_core_v4_alpha__.Address" = betterproto.message_field(1)
    # The canonical service name of the peer. It should be set to :ref:`the HTTP
    # x-envoy-downstream-service-cluster
    # <config_http_conn_man_headers_downstream-service-cluster>` If a more
    # trusted source of the service name is available through mTLS/secure naming,
    # it should be used.
    service: str = betterproto.string_field(2)
    # The labels associated with the peer. These could be pod labels for
    # Kubernetes or tags for VMs. The source of the labels could be an X.509
    # certificate or other configuration.
    labels: Dict[str, str] = betterproto.map_field(
        3, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    # The authenticated identity of this peer. For example, the identity
    # associated with the workload such as a service account. If an X.509
    # certificate is used to assert the identity this field should be sourced
    # from `URI Subject Alternative Names`, `DNS Subject Alternate Names` or
    # `Subject` in that order. The primary identity should be the principal. The
    # principal format is issuer specific. Example: *    SPIFFE format is
    # `spiffe://trust-domain/path` *    Google account format is
    # `https://accounts.google.com/{userid}`
    principal: str = betterproto.string_field(4)
    # The X.509 certificate used to authenticate the identify of this peer. When
    # present, the certificate contents are encoded in URL and PEM format.
    certificate: str = betterproto.string_field(5)


@dataclass(eq=False, repr=False)
class AttributeContextRequest(betterproto.Message):
    """Represents a network request, such as an HTTP request."""

    # The timestamp when the proxy receives the first byte of the request.
    time: datetime = betterproto.message_field(1)
    # Represents an HTTP request or an HTTP-like request.
    http: "AttributeContextHttpRequest" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class AttributeContextHttpRequest(betterproto.Message):
    """
    This message defines attributes for an HTTP request. HTTP/1.x, HTTP/2, gRPC
    are all considered as HTTP requests. [#next-free-field: 13]
    """

    # The unique ID for a request, which can be propagated to downstream systems.
    # The ID should have low probability of collision within a single day for a
    # specific service. For HTTP requests, it should be X-Request-ID or
    # equivalent.
    id: str = betterproto.string_field(1)
    # The HTTP request method, such as `GET`, `POST`.
    method: str = betterproto.string_field(2)
    # The HTTP request headers. If multiple headers share the same key, they must
    # be merged according to the HTTP spec. All header keys must be lower-cased,
    # because HTTP header keys are case-insensitive.
    headers: Dict[str, str] = betterproto.map_field(
        3, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    # The request target, as it appears in the first line of the HTTP request.
    # This includes the URL path and query-string. No decoding is performed.
    path: str = betterproto.string_field(4)
    # The HTTP request `Host` or 'Authority` header value.
    host: str = betterproto.string_field(5)
    # The HTTP URL scheme, such as `http` and `https`.
    scheme: str = betterproto.string_field(6)
    # This field is always empty, and exists for compatibility reasons. The HTTP
    # URL query is included in `path` field.
    query: str = betterproto.string_field(7)
    # This field is always empty, and exists for compatibility reasons. The URL
    # fragment is not submitted as part of HTTP requests; it is unknowable.
    fragment: str = betterproto.string_field(8)
    # The HTTP request size in bytes. If unknown, it must be -1.
    size: int = betterproto.int64_field(9)
    # The network protocol used with the request, such as "HTTP/1.0", "HTTP/1.1",
    # or "HTTP/2". See :repo:`headers.h:ProtocolStrings
    # <source/common/http/headers.h>` for a list of all possible values.
    protocol: str = betterproto.string_field(10)
    # The HTTP request body.
    body: str = betterproto.string_field(11)
    # The HTTP request body in bytes. This is used instead of :ref:`body
    # <envoy_v3_api_field_service.auth.v3.AttributeContext.HttpRequest.body>`
    # when :ref:`pack_as_bytes <envoy_v3_api_field_extensions.filters.http.ext_au
    # thz.v3.BufferSettings.pack_as_bytes>` is set to true.
    raw_body: bytes = betterproto.bytes_field(12)


@dataclass(eq=False, repr=False)
class CheckRequest(betterproto.Message):
    # The request attributes.
    attributes: "AttributeContext" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class DeniedHttpResponse(betterproto.Message):
    """HTTP attributes for a denied response."""

    # This field allows the authorization service to send a HTTP response status
    # code to the downstream client other than 403 (Forbidden).
    status: "___type_v3__.HttpStatus" = betterproto.message_field(1)
    # This field allows the authorization service to send HTTP response headers
    # to the downstream client. Note that the :ref:`append field in
    # HeaderValueOption
    # <envoy_v3_api_field_config.core.v3.HeaderValueOption.append>` defaults to
    # false when used in this message.
    headers: List[
        "___config_core_v4_alpha__.HeaderValueOption"
    ] = betterproto.message_field(2)
    # This field allows the authorization service to send a response body data to
    # the downstream client.
    body: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class OkHttpResponse(betterproto.Message):
    """HTTP attributes for an OK response. [#next-free-field: 7]"""

    # HTTP entity headers in addition to the original request headers. This
    # allows the authorization service to append, to add or to override headers
    # from the original request before dispatching it to the upstream. Note that
    # the :ref:`append field in HeaderValueOption
    # <envoy_v3_api_field_config.core.v3.HeaderValueOption.append>` defaults to
    # false when used in this message. By setting the `append` field to `true`,
    # the filter will append the correspondent header value to the matched
    # request header. By leaving `append` as false, the filter will either add a
    # new header, or override an existing one if there is a match.
    headers: List[
        "___config_core_v4_alpha__.HeaderValueOption"
    ] = betterproto.message_field(2)
    # HTTP entity headers to remove from the original request before dispatching
    # it to the upstream. This allows the authorization service to act on auth
    # related headers (like `Authorization`), process them, and consume them.
    # Under this model, the upstream will either receive the request (if it's
    # authorized) or not receive it (if it's not), but will not see headers
    # containing authorization credentials. Pseudo headers (such as `:authority`,
    # `:method`, `:path` etc), as well as the header `Host`, may not be removed
    # as that would make the request malformed. If mentioned in
    # `headers_to_remove` these special headers will be ignored. When using the
    # HTTP service this must instead be set by the HTTP authorization service as
    # a comma separated list like so: ``x-envoy-auth-headers-to-remove: one-auth-
    # header, another-auth-header``.
    headers_to_remove: List[str] = betterproto.string_field(5)
    # This field allows the authorization service to send HTTP response headers
    # to the downstream client on success. Note that the :ref:`append field in
    # HeaderValueOption
    # <envoy_v3_api_field_config.core.v3.HeaderValueOption.append>` defaults to
    # false when used in this message.
    response_headers_to_add: List[
        "___config_core_v4_alpha__.HeaderValueOption"
    ] = betterproto.message_field(6)


@dataclass(eq=False, repr=False)
class CheckResponse(betterproto.Message):
    """Intended for gRPC and Network Authorization servers `only`."""

    # Status `OK` allows the request. Any other status indicates the request
    # should be denied.
    status: "____google_rpc__.Status" = betterproto.message_field(1)
    # Supplies http attributes for a denied response.
    denied_response: "DeniedHttpResponse" = betterproto.message_field(
        2, group="http_response"
    )
    # Supplies http attributes for an ok response.
    ok_response: "OkHttpResponse" = betterproto.message_field(3, group="http_response")
    # Optional response metadata that will be emitted as dynamic metadata to be
    # consumed by the next filter. This metadata lives in a namespace specified
    # by the canonical name of extension filter that requires it: -
    # :ref:`envoy.filters.http.ext_authz
    # <config_http_filters_ext_authz_dynamic_metadata>` for HTTP filter. -
    # :ref:`envoy.filters.network.ext_authz
    # <config_network_filters_ext_authz_dynamic_metadata>` for network filter.
    dynamic_metadata: "betterproto_lib_google_protobuf.Struct" = (
        betterproto.message_field(4)
    )


class AuthorizationStub(betterproto.ServiceStub):
    async def check(self, *, attributes: "AttributeContext" = None) -> "CheckResponse":

        request = CheckRequest()
        if attributes is not None:
            request.attributes = attributes

        return await self._unary_unary(
            "/envoy.service.auth.v4alpha.Authorization/Check", request, CheckResponse
        )


class AuthorizationBase(ServiceBase):
    async def check(self, attributes: "AttributeContext") -> "CheckResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_check(self, stream: grpclib.server.Stream) -> None:
        request = await stream.recv_message()

        request_kwargs = {
            "attributes": request.attributes,
        }

        response = await self.check(**request_kwargs)
        await stream.send_message(response)

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/envoy.service.auth.v4alpha.Authorization/Check": grpclib.const.Handler(
                self.__rpc_check,
                grpclib.const.Cardinality.UNARY_UNARY,
                CheckRequest,
                CheckResponse,
            ),
        }


from .....google import rpc as ____google_rpc__
from ....config.core import v4alpha as ___config_core_v4_alpha__
from ....type import v3 as ___type_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
