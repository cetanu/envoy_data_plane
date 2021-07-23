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

build_directory = Path("BUILD")
if not build_directory.exists():
    logger.msg("Creating BUILD directory")
    build_directory.mkdir()
os.chdir(build_directory)

utf8 = "utf-8"

ENVOY_VERSION = "1.13.7"

proto_include = protoc.pkg_resources.resource_filename("grpc_tools", "_proto")
envoy = Path("./envoy")
envoy_api = Path("./envoy/api")
envoy_api_v2 = Path("./envoy/api/v2")

Package = namedtuple("Package", ["url", "name", "directory", "namespace"])
packages = {
    Package(
        url=f"https://github.com/envoyproxy/envoy/archive/refs/tags/v{ENVOY_VERSION}.zip",
        name="envoy",
        namespace="envoy",
        directory=f"envoy-{ENVOY_VERSION}/api",
    ),
    Package(
        url="https://github.com/googleapis/googleapis/archive/master.zip",
        name="google",
        namespace="google",
        directory="googleapis-master",
    ),
    Package(
        url="https://github.com/cncf/udpa/archive/refs/tags/v0.0.1.zip",
        name="udpa",
        namespace="udpa",
        directory="udpa-0.0.1",
    ),
    Package(
        url="https://github.com/envoyproxy/protoc-gen-validate/archive/main.zip",
        name="validate",
        namespace="validate",
        directory="protoc-gen-validate-main",
    ),
    Package(
        url="https://github.com/census-instrumentation/opencensus-proto/archive/refs/tags/v0.2.0.zip",
        name="opencensus",
        namespace="opencensus",
        directory="opencensus-proto-0.2.0/src",
    ),
    Package(
        url="https://github.com/prometheus/client_model/archive/refs/tags/v0.2.0.zip",
        name="prometheus",
        namespace=".",
        directory="client_model-0.2.0",
    ),
}


for package in packages:
    name = Path(package.name)
    namespace = Path(package.namespace)
    proto_root = Path(package.directory)
    archive = Path(f"{package.name}.zip")

    if not archive.exists():
        logger.msg(f"Downloading {package.name} protocol buffers from Github")
        with open(archive, "wb+") as zf:
            zf.write(requests.get(package.url).content)

    if name.exists():
        logger.msg(f"{name.absolute()} exists")
    else:
        logger.msg(f"Extracting {name} archive")
        with zipfile.ZipFile(archive, "r") as zipref:
            protos = [
                member for member in zipref.namelist() if member.endswith(".proto")
            ]
            for file in protos:
                logger.msg(f"Extracting {file}")
                zipref.extract(member=file, path=".")
        shutil.copytree(proto_root / namespace, name)


output = Path("../src/envoy_data_plane")
proto_args = [
    __file__,
    f"--proto_path=.",
    f"--proto_path={envoy}",
    f"--proto_path={envoy_api}",
    f"--proto_path={envoy_api_v2}",
    f"--proto_path={proto_include}",
]


def compile_all():
    logger.msg("Running GRPC tools to generate python code from protocol buffers")
    proto_files = [str(file) for file in envoy.glob("**/*") if file.suffix == ".proto"]
    proto_paths = [
        f"--proto_path={folder}" for folder in Path(".").glob("**/*") if folder.is_dir()
    ]
    args = deepcopy(proto_args)
    args += proto_paths
    args += [f"--python_betterproto_out={output}"]
    protoc.main((*args, *proto_files))


compile_all()
