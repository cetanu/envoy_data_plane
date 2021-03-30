import os
import shutil
import zipfile
import requests
import structlog
from collections import namedtuple
from copy import deepcopy
from pathlib import Path
from grpc_tools import protoc

structlog.configure()
logger = structlog.get_logger()

build_directory = Path('BUILD')
if not build_directory.exists():
    logger.msg('Creating BUILD directory')
    build_directory.mkdir()
os.chdir(build_directory)

utf8 = 'utf-8'

proto_include = protoc.pkg_resources.resource_filename('grpc_tools', '_proto')
output = Path('../src/envoy_data_plane')
envoy = Path('./envoy')
envoy_api = Path('./envoy/api')
envoy_api_v2 = Path('./envoy/api/v2')
proto_args = [
    __file__,
    f'--proto_path=.',
    f'--proto_path={envoy}',
    f'--proto_path={envoy_api}',
    f'--proto_path={envoy_api_v2}',
    f'--proto_path={proto_include}',
]

Package = namedtuple('Package', ['url', 'name', 'directory'])
packages = {
    Package(
        url='https://github.com/envoyproxy/envoy/archive/refs/tags/v1.16.2.zip',
        name='envoy',
        directory='envoy-1.16.2/api'
    ),
    Package(
        url='https://github.com/googleapis/googleapis/archive/master.zip',
        name='google',
        directory='googleapis-master'
    ),
    Package(
        url='https://github.com/cncf/udpa/archive/refs/tags/v0.0.1.zip',
        name='udpa',
        directory='udpa-0.0.1'
    ),
    Package(
        url='https://github.com/envoyproxy/protoc-gen-validate/archive/main.zip',
        name='validate',
        directory='protoc-gen-validate-main'
    ),
    Package(
        url='https://github.com/census-instrumentation/opencensus-proto/archive/refs/tags/v0.2.0.zip',
        name='opencensus',
        directory='opencensus-proto-0.2.0/src'
    )
}


for package in packages:
    namespace = Path(package.name)
    proto_root = Path(package.directory)
    archive = Path(f'{package.name}.zip')

    if not archive.exists():
        logger.msg(f'Downloading {package.name} protocol buffers from Github')
        with open(archive, 'wb+') as zf:
            zf.write(requests.get(package.url).content)

    if namespace.exists():
        logger.msg(f'{namespace.absolute()} exists')
    else:
        logger.msg(f'Extracting {namespace} archive')
        with zipfile.ZipFile(archive, 'r') as zipref:
            protos = [
                member
                for member in zipref.namelist()
                if member.endswith('.proto')
            ]
            for file in protos:
                logger.msg(f'Extracting {file}')
                zipref.extract(
                    member=file,
                    path='.'
                )
        shutil.copytree(
            proto_root/namespace,
            namespace
        )


def everything():
    proto_files = [
        str(file) for file in envoy.glob('**/*')
        if file.suffix == '.proto'
    ]
    proto_paths = [
        f'--proto_path={folder}'
        for folder in Path('.').glob('**/*')
        if folder.is_dir()
    ]
    args = deepcopy(proto_args)
    args += proto_paths
    args += [f'--python_betterproto_out={output}']
    logger.msg('Running GRPC tools to generate python code from protocol buffers')
    files = list()
    for f in proto_files:
        files.append(f)
        if len(files) >= 100:
            protoc.main(args + files)
            files.clear()
    protoc.main(args + files)


def xds():
    proto_paths = [
        str(envoy_api_v2.joinpath(Path(f'{discovery_type}.proto')))
        for discovery_type in ['cds', 'lds', 'rds', 'eds', 'srds']
    ]
    args = deepcopy(proto_args)
    args += proto_paths
    args += [f'--python_betterproto_out={output}']
    protoc.main(args)


everything()
xds()
