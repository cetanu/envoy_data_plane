# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: envoy/extensions/wasm/v3/wasm.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto
from betterproto.grpc.grpclib_server import ServiceBase


@dataclass(eq=False, repr=False)
class VmConfig(betterproto.Message):
    """
    [[#not-implemented-hide:] Configuration for a Wasm VM. [#next-free-field:
    7]
    """

    # An ID which will be used along with a hash of the wasm code (or the name of
    # the registered Null VM plugin) to determine which VM will be used for the
    # plugin. All plugins which use the same *vm_id* and code will use the same
    # VM. May be left blank. Sharing a VM between plugins can reduce memory
    # utilization and make sharing of data easier which may have security
    # implications. See ref: "TODO: add ref" for details.
    vm_id: str = betterproto.string_field(1)
    # The Wasm runtime type (either "v8" or "null" for code compiled into Envoy).
    runtime: str = betterproto.string_field(2)
    # The Wasm code that Envoy will execute.
    code: "___config_core_v3__.AsyncDataSource" = betterproto.message_field(3)
    # The Wasm configuration used in initialization of a new VM (proxy_on_start).
    # `google.protobuf.Struct` is serialized as JSON before passing it to the
    # plugin. `google.protobuf.BytesValue` and `google.protobuf.StringValue` are
    # passed directly without the wrapper.
    configuration: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(4)
    # Allow the wasm file to include pre-compiled code on VMs which support it.
    # Warning: this should only be enable for trusted sources as the precompiled
    # code is not verified.
    allow_precompiled: bool = betterproto.bool_field(5)
    # If true and the code needs to be remotely fetched and it is not in the
    # cache then NACK the configuration update and do a background fetch to fill
    # the cache, otherwise fetch the code asynchronously and enter warming state.
    nack_on_code_cache_miss: bool = betterproto.bool_field(6)


@dataclass(eq=False, repr=False)
class PluginConfig(betterproto.Message):
    """
    [[#not-implemented-hide:] Base Configuration for Wasm Plugins e.g. filters
    and services. [#next-free-field: 6]
    """

    # A unique name for a filters/services in a VM for use in identifying the
    # filter/service if multiple filters/services are handled by the same *vm_id*
    # and *root_id* and for logging/debugging.
    name: str = betterproto.string_field(1)
    # A unique ID for a set of filters/services in a VM which will share a
    # RootContext and Contexts if applicable (e.g. an Wasm HttpFilter and an Wasm
    # AccessLog). If left blank, all filters/services with a blank root_id with
    # the same *vm_id* will share Context(s).
    root_id: str = betterproto.string_field(2)
    inline_vm_config: "VmConfig" = betterproto.message_field(3, group="vm_config")
    # Filter/service configuration used to configure or reconfigure a plugin
    # (proxy_on_configuration). `google.protobuf.Struct` is serialized as JSON
    # before passing it to the plugin. `google.protobuf.BytesValue` and
    # `google.protobuf.StringValue` are passed directly without the wrapper.
    configuration: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(4)
    # If there is a fatal error on the VM (e.g. exception, abort(), on_start or
    # on_configure return false), then all plugins associated with the VM will
    # either fail closed (by default), e.g. by returning an HTTP 503 error, or
    # fail open (if 'fail_open' is set to true) by bypassing the filter. Note:
    # when on_start or on_configure return false during xDS updates the xDS
    # configuration will be rejected and when on_start or on_configuration return
    # false on initial startup the proxy will not start.
    fail_open: bool = betterproto.bool_field(5)


@dataclass(eq=False, repr=False)
class WasmService(betterproto.Message):
    """
    [[#not-implemented-hide:] WasmService is configured as a built-in
    *envoy.wasm_service* :ref:`WasmService <config_wasm_service>` This opaque
    configuration will be used to create a Wasm Service.
    """

    # General plugin configuration.
    config: "PluginConfig" = betterproto.message_field(1)
    # If true, create a single VM rather than creating one VM per worker. Such a
    # singleton can not be used with filters.
    singleton: bool = betterproto.bool_field(2)


from ....config.core import v3 as ___config_core_v3__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
