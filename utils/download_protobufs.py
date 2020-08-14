import os
import zipfile
import requests
import structlog
from copy import deepcopy
from pathlib import Path
from grpc_tools import protoc

utf8 = 'utf-8'

proto_include = protoc.pkg_resources.resource_filename('grpc_tools', '_proto')

structlog.configure()
logger = structlog.get_logger()

archives_to_unpack = (
    ('envoy', 'https://github.com/envoyproxy/data-plane-api/archive/master.zip', 'data-plane-api'),
    ('google', 'https://github.com/googleapis/googleapis/archive/master.zip', 'googleapis'),
    ('udpa', 'https://github.com/cncf/udpa/archive/master.zip', 'udpa'),
    ('validate', 'https://github.com/envoyproxy/protoc-gen-validate/archive/master.zip', 'protoc-gen-validate'),
    ('protobuf', 'https://github.com/protocolbuffers/protobuf/archive/master.zip', 'protobuf'),
)

build_directory = Path('BUILD')
if not build_directory.exists():
    logger.msg('Creating BUILD directory')
    build_directory.mkdir()
os.chdir(build_directory)

protobuf_files = Path('github_files')

for name, repo_url, repo_name in archives_to_unpack:
    namespace = Path(name)
    archive = Path(f'{repo_name}.zip')
    extracted_name = f'{repo_name}-master'

    if not archive.exists():
        logger.msg(f'Downloading {name} protocol buffers from Github')
        with open(archive, 'wb+') as zf:
            zf.write(requests.get(repo_url).content)

    if str(namespace) == 'protobuf' and Path('google').joinpath(namespace).exists():
        continue

    if not namespace.exists():
        logger.msg(f'Extracting {namespace} archive')
        with zipfile.ZipFile(archive, 'r') as zipref:
            protos = [
                member
                for member in zipref.namelist()
                if member.endswith('.proto')
            ]
            for file in protos:
                logger.msg(f'Extracting {file[len(extracted_name) + 1:]}')
                zipref.extract(
                    member=file,
                    path=protobuf_files
                )

        extracted_files_root = protobuf_files.joinpath(Path(extracted_name))
        if str(namespace) == 'protobuf':
            protocol_buffers = extracted_files_root.joinpath(Path(f'src/google/{namespace}'))
            google_protos = Path(f'./google/{namespace}')
            protocol_buffers.replace(google_protos)
            logger.msg(f'Moving {protocol_buffers} -> {google_protos.absolute()}')
        else:
            protocol_buffers = extracted_files_root.joinpath(namespace)
            protocol_buffers.replace(namespace)
            logger.msg(f'Moving {protocol_buffers} -> {namespace.absolute()}')
    else:
        logger.msg(f'{namespace.absolute()} exists')

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
