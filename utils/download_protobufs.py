import os
import zipfile
import requests
import structlog
from typing import List
from copy import deepcopy
from pathlib import Path
from collections import namedtuple
from grpc_tools import protoc

utf8 = 'utf-8'

proto_include = protoc.pkg_resources.resource_filename('grpc_tools', '_proto')

structlog.configure()
logger = structlog.get_logger()

Archive = namedtuple('Archive', ['repo_name', 'download_url', 'directory', 'suffix'])

archives_to_unpack = (
    Archive('envoy', 'https://github.com/envoyproxy/data-plane-api/archive/master.zip', 'data-plane-api', 'master'),
    Archive('google', 'https://github.com/googleapis/googleapis/archive/master.zip', 'googleapis', 'master'),
    Archive('udpa', 'https://github.com/cncf/udpa/archive/master.zip', 'udpa', 'master'),
    Archive('validate', 'https://github.com/envoyproxy/protoc-gen-validate/archive/v0.4.1.zip', 'protoc-gen-validate', '0.4.1'),
    Archive('protobuf', 'https://github.com/protocolbuffers/protobuf/releases/download/v3.14.0/protobuf-python-3.14.0.zip', 'protobuf', '3.14.0'),
)

build_directory = Path('BUILD')
if not build_directory.exists():
    logger.msg('Creating BUILD directory')
    build_directory.mkdir()
os.chdir(build_directory)

protobuf_files = Path('github_files')

for archive in archives_to_unpack:
    namespace = Path(archive.repo_name)
    zip_archive = Path(f'{archive.directory}.zip')
    extracted_name = f'{archive.directory}-{archive.suffix}'

    if not zip_archive.exists():
        logger.msg(f'Downloading {archive.repo_name} protocol buffers from Github')
        with open(zip_archive, 'wb+') as zf:
            zf.write(requests.get(archive.download_url).content)

    if str(namespace) == 'protobuf' and Path('google').joinpath(namespace).exists():
        continue

    if namespace.exists():
        logger.msg(f'{namespace.absolute()} exists')
    else:
        logger.msg(f'Extracting {namespace} archive')
        with zipfile.ZipFile(zip_archive, 'r') as zipref:
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

output = Path('../src/envoy_data_plane')
envoy = Path('./envoy')
udpa = Path('./udpa')
google = Path('./google')
validate = Path('./validate')
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


def glob_proto_files(path: Path) -> List[str]:
    return [
        str(file) for file in path.glob('**/*')
        if file.suffix == '.proto'
    ]


def everything():
    proto_files = list()
    for path in [envoy, udpa, validate, google]:
        proto_files.extend(glob_proto_files(path))
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
        package_parent = Path('../src/envoy_data_plane').joinpath(Path(f).parent)
        init_file = package_parent.joinpath(Path('__init__.py'))
        if not init_file.exists():
            logger.msg(f'Creating {package_parent}')
            package_parent.mkdir(parents=True, exist_ok=True)
            logger.msg(f'Creating {init_file}')
            init_file.touch(exist_ok=True)
        files.append(f)
        # if len(files) >= 100:
        #     protoc.main(args + files)
        #     files.clear()
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
