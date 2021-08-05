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

There are branches available with compiled python protobuf files.  
To install them, you can use the following syntax:

```shell script
pip install git+https://github.com/cetanu/envoy_data_plane@<BRANCH NAME>
```

Examples:

```
pip install git+https://github.com/cetanu/envoy_data_plane@envoy_v1.13.7
pip install git+https://github.com/cetanu/envoy_data_plane@envoy_v1.16.2
pip install git+https://github.com/cetanu/envoy_data_plane@envoy_v1.17.2
pip install git+https://github.com/cetanu/envoy_data_plane@envoy_v1.18.2
pip install git+https://github.com/cetanu/envoy_data_plane@envoy_v1.19.0
```

Not all versions may be available. Raise an issue if you need another one added.

## Example

```python
import stringcase
import json
import envoy_data_plane.envoy.api.v2 as envoy

route_config = envoy.RouteConfiguration(
    name='MyRouteConfig',
    virtual_hosts=[
        envoy.route.VirtualHost(
            name='SomeWebsite',
            domains=['foobar.com'],
            routes=[
                envoy.route.Route(
                    name='catchall',
                    match=envoy.route.RouteMatch(
                        prefix='/'
                    ),
                    direct_response=envoy.route.DirectResponseAction(
                        status=200,
                        body=envoy.core.DataSource(
                            inline_string='Hello there'
                        )
                    )
                )
            ]
        )
    ]
)

response = envoy.DiscoveryResponse(
    version_info='0',
    resources=[
        route_config
    ],
)

print(
    json.dumps(response.to_dict(casing=stringcase.snakecase), indent=2)
)
```

Result:
```
{
  "version_info": "0",
  "resources": [
    {
      "name": "MyRouteConfig",
      "virtual_hosts": [
        {
          "name": "SomeWebsite",
          "domains": [
            "foobar.com"
          ],
          "routes": [
            {
              "name": "catchall",
              "match": {
                "prefix": "/",
                "headers": [],
                "query_parameters": []
              },
              "direct_response": {
                "status": 200,
                "body": {
                  "inline_string": "Hello there"
                }
              },
              "request_headers_to_add": [],
              "response_headers_to_add": []
            }
          ],
          "virtual_clusters": [],
          "rate_limits": [],
          "request_headers_to_add": [],
          "response_headers_to_add": []
        }
      ],
      "response_headers_to_add": [],
      "request_headers_to_add": []
    }
  ]
}

```
