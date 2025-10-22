# envoy_data_plane

A conversion of envoyproxy/data-plane-api protocol buffers into Python dataclasses using betterproto

## Intended usage

This is a helper library that allows importing every type available in the envoy API.

One use-case might be generating Envoy configuration using a Python script.

In my case, I will use this library in my custom built control-plane, 
so that I have autocompletion in my IDE, and a basic form of validation.

In future, this may also help with building an idiomatic GRPC control-plane in Python.

## Installation

This package is published to PyPI:

```shell script
python -m pip install envoy_data_plane
```

## Installing specific XDS revisions

I used to maintain branches with compiled python protobuf files for each
version, but I haven't heard from anyone needing them to be updated or anything
like that, so I've stopped this effort.

If you need a specific version just call out in the issues, otherwise I will
keep publishing the latest release to match the current envoy release.

## Examples

See the scenarios directory for example usages
