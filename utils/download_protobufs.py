import os
import zipfile
import requests
import structlog
from pathlib import Path
from grpc_tools import protoc

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
        with open(archive, 'wb+') as f:
            f.write(requests.get(repo_url).content)

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
                logger.msg(f'Extracting {file[len(extracted_name)+1:]}')
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


logger.msg('Removing Streaming/Services from protocol buffers')
for root, folders, files in os.walk('.'):
    rootdir = Path(root)

    for file in files:
        if not file.endswith('.proto') \
                or 'envoy' not in root \
                or 'api' not in root:
            continue

        protocol_buffer = rootdir.joinpath(Path(file))

        with open(protocol_buffer) as f:
            try:
                content = f.read()
                f.seek(0)
                lines = f.readlines()
            except UnicodeDecodeError:
                continue

            if '\nservice ' not in content:
                continue

            while '\nservice ' in content:
                start, end = 0, 0
                for index, line in enumerate(lines):
                    stripped_line = line.strip()
                    if stripped_line.startswith('service ') and stripped_line.endswith('{'):
                        start = index
                    elif start != 0 and start < index and line == '}\n':
                        end = index
                        break

                marked_for_deletion = list(reversed(range(start, end+1)))

                for index in marked_for_deletion:
                    del lines[index]

                content = ''.join(lines)

        with open(protocol_buffer, 'w+') as f:
            f.write(content)


output = Path('../src/envoy_data_plane')
envoy = Path('./envoy')
envoy_api = Path('./envoy/api')
envoy_api_v2 = Path('./envoy/api/v2')

proto_paths = [
    str(envoy_api_v2.joinpath(Path(f'{discovery_type}.proto')))
    for discovery_type in ['cds', 'lds', 'rds', 'eds', 'srds']
]
args = [
    __file__,
    f'--proto_path=.',
    f'--proto_path={envoy}',
    f'--proto_path={envoy_api}',
    f'--proto_path={envoy_api_v2}',
    f'--proto_path={proto_include}',
    f'--python_betterproto_out={output}',
]
logger.msg('Running GRPC tools to generate python code from protocol buffers')
protoc.main(args + proto_paths)


for root, folders, files in os.walk('../src'):
    rootdir = Path(root)

    for file in files:
        folder_name = file.replace('.py', '')
        filepath = rootdir.joinpath(file)
        folder_init = rootdir.joinpath(Path(folder_name)).joinpath('__init__.py')
        if folder_name in folders:
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
            with open(folder_init, 'w+', encoding='utf-8') as f:
                f.write(content)

    for file in files:
        filepath = rootdir.joinpath(file)

        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        content = content.replace('from .', 'from envoy_data_plane.')

        with open(filepath, 'w+', encoding='utf-8') as f:
            f.write(content)


any_proto = '''
from dataclasses import dataclass
import betterproto


@dataclass
class Any(betterproto.Message):
    type_url: str = betterproto.string_field(1)
    value: bytes = betterproto.bytes_field(2)
    
    
@dataclass
class Struct(betterproto.Message):
    fields: betterproto.Dict[str, "Value"] = betterproto.map_field(
        1, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )


@dataclass
class Value(betterproto.Message):
    null_value: "NullValue" = betterproto.enum_field(1, group="kind")
    number_value: float = betterproto.double_field(2, group="kind")
    string_value: str = betterproto.string_field(3, group="kind")
    bool_value: bool = betterproto.bool_field(4, group="kind")
    struct_value: "Struct" = betterproto.message_field(5, group="kind")
    list_value: "ListValue" = betterproto.message_field(6, group="kind")


@dataclass
class ListValue(betterproto.Message):
    values: betterproto.List["Value"] = betterproto.message_field(1)
    

@dataclass
class Empty(betterproto.Message):
    pass


class NullValue(betterproto.Enum):
    NULL_VALUE = 0
'''

with open(Path('../src/envoy_data_plane/google/protobuf.py'), 'w+') as f:
    f.write(any_proto)

    
# Found a bit of a bug, TODO: get this fixed or looked into with the betterproto folks
with open(Path('../src/envoy_data_plane/envoy/api/v2/__init__.py') as f:
    content = f.read()

with open(Path('../src/envoy_data_plane/envoy/api/v2/__init__.py'), 'w+') as f:
    weird_class_name = 'ClusterLoadAssignmentClusterLoadAssignmentPolicyDropOverload'
    content = content.replace(weird_class_name, 'ClusterLoadAssignmentPolicyDropOverload')
    f.write(content)
