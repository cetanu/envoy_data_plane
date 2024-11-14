import os
import shutil
import zipfile
import requests
import structlog
from dataclasses import dataclass
from copy import deepcopy
from pathlib import Path
from grpc_tools import protoc

ENVOY_VERSION = "1.32.0"

structlog.configure()
logger = structlog.get_logger()


@dataclass
class Package:
    url: str
    name: str
    directory: str
    namespace: str

    @property
    def archive(self):
        return Path(f"{self.name}.zip")

    @property
    def root(self):
        return Path(self.directory) / Path(self.namespace)

    @property
    def absolute_path(self):
        return Path(self.name).absolute()

    @property
    def exists(self) -> bool:
        ret = Path(self.name).exists()
        if ret:
            logger.msg(f"{self.absolute_path} exists")
        else:
            logger.msg(f"{self.absolute_path} does not exist")
        return ret

    def download(self):
        logger.msg(f"Downloading {self.name} protocol buffers from Github")
        with open(self.archive, "wb+") as zf:
            logger.msg(f"Writing {self.archive} to disk")
            zf.write(requests.get(self.url).content)

    def extract(self):
        logger.msg(f"Extracting {self.name} archive")
        with zipfile.ZipFile(self.archive, "r") as zipref:
            protos = [
                member for member in zipref.namelist() if member.endswith(".proto")
            ]
            for file in protos:
                logger.msg(f"Extracting {file}")
                zipref.extract(member=file, path=".")

        logger.msg(f"Copying {self.root} over the top of {self.name}")
        shutil.copytree(self.root, self.name)


packages = {
    Package(
        url=f"https://github.com/envoyproxy/envoy/archive/refs/tags/v{ENVOY_VERSION}.zip",
        name="envoy",
        namespace="envoy",
        directory=f"envoy-{ENVOY_VERSION}/api",
    ),
    Package(
        url=f"https://github.com/envoyproxy/envoy/archive/refs/tags/v{ENVOY_VERSION}.zip",
        name="envoy",
        namespace=".",
        directory=f"envoy-{ENVOY_VERSION}/contrib",
    ),
    Package(
        url="https://github.com/cncf/xds/archive/refs/heads/main.zip",
        name="xds",
        namespace=".",
        directory="xds-main",
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
        url="https://github.com/open-telemetry/opentelemetry-proto/archive/refs/tags/v0.9.0.zip",
        name="opentelemetry",
        namespace="opentelemetry",
        directory="opentelemetry-proto-0.9.0",
    ),
    Package(
        url="https://github.com/prometheus/client_model/archive/refs/heads/master.zip",
        name="prometheus",
        namespace=".",
        directory="client_model-master",
    ),
}


def compile_all():
    proto_include = protoc.resources.path("grpc_tools", "_proto")
    envoy = Path("./envoy")
    envoy_api = Path("./envoy/api")
    envoy_api_v2 = Path("./envoy/api/v2")
    output = Path("../src/envoy_data_plane")
    proto_args = [
        __file__,
        "--proto_path=.",
        f"--proto_path={envoy}",
        f"--proto_path={envoy_api}",
        f"--proto_path={envoy_api_v2}",
        f"--proto_path={proto_include}",
    ]
    logger.msg("Running GRPC tools to generate python code from protocol buffers")
    proto_files = [str(file) for file in envoy.glob("**/*") if file.suffix == ".proto"]
    proto_paths = [
        f"--proto_path={folder}" for folder in Path(".").glob("**/*") if folder.is_dir()
    ]
    args = deepcopy(proto_args)
    args += proto_paths
    args += [f"--python_betterproto_out={output}"]
    protoc.main((*args, *proto_files))


def main():
    build_directory = Path("BUILD")
    if not build_directory.exists():
        logger.msg("Creating BUILD directory")
        build_directory.mkdir()
    os.chdir(build_directory)

    for pkg in packages:
        if not pkg.archive.exists():
            pkg.download()

        if not pkg.exists:
            pkg.extract()

    compile_all()


if __name__ == "__main__":
    main()
