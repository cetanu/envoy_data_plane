import os
import shutil
import zipfile
from copy import deepcopy
from pathlib import Path
from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor

import requests
import structlog
from grpc_tools import protoc

ENVOY_VERSION = "1.36.2"

structlog.configure()
logger = structlog.get_logger()


@dataclass(frozen=True)
class Package:
    url: str
    name: str
    source_root: str
    source_subdir: str
    target_root: str
    target_subdir: str | None = None

    @property
    def archive(self):
        return Path(f"{self.target_root}.zip")

    @property
    def source_protobufs(self):
        return Path(self.source_root) / Path(self.source_subdir)

    @property
    def target(self):
        if self.target_subdir is not None:
            return Path(self.target_root) / Path(self.target_subdir)
        return Path(self.target_root)

    @property
    def final_proto_root_absolute(self):
        return Path(self.target_root).absolute()

    @property
    def target_exists(self) -> bool:
        ret = self.target.exists()
        if ret:
            logger.msg(f"{self.target} exists")
        else:
            logger.msg(f"{self.target} does not exist")
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

        logger.msg(f"Copying {self.source_protobufs} over the top of {self.target}")
        shutil.copytree(self.source_protobufs, self.target, dirs_exist_ok=True)

    def execute(self):
        self.download()
        self.extract()


packages = {
    Package(
        url=f"https://github.com/envoyproxy/envoy/archive/refs/tags/v{ENVOY_VERSION}.zip",
        name="envoy",
        source_root=f"envoy-{ENVOY_VERSION}/api",
        source_subdir="envoy",
        target_root="envoy",
    ),
    Package(
        url=f"https://github.com/envoyproxy/envoy/archive/refs/tags/v{ENVOY_VERSION}.zip",
        name="envoy contrib",
        source_root=f"envoy-{ENVOY_VERSION}/contrib",
        source_subdir=".",
        target_root="envoy",
        target_subdir="contrib",
    ),
    Package(
        url="https://github.com/cncf/xds/archive/refs/heads/main.zip",
        name="xds",
        source_root="xds-main",
        source_subdir=".",
        target_root="xds",
    ),
    Package(
        url="https://github.com/googleapis/googleapis/archive/master.zip",
        name="google",
        source_root="googleapis-master",
        source_subdir="google",
        target_root="google",
    ),
    Package(
        url="https://github.com/cncf/udpa/archive/refs/tags/v0.0.1.zip",
        name="udpa",
        source_root="udpa-0.0.1",
        source_subdir="udpa",
        target_root="udpa",
    ),
    Package(
        url="https://github.com/envoyproxy/protoc-gen-validate/archive/main.zip",
        name="validate",
        source_root="protoc-gen-validate-main",
        source_subdir="validate",
        target_root="validate",
    ),
    Package(
        url="https://github.com/census-instrumentation/opencensus-proto/archive/refs/tags/v0.2.0.zip",
        name="opencensus",
        source_root="opencensus-proto-0.2.0/src",
        source_subdir="opencensus",
        target_root="opencensus",
    ),
    Package(
        url="https://github.com/open-telemetry/opentelemetry-proto/archive/refs/tags/v0.9.0.zip",
        name="opentelemetry",
        source_root="opentelemetry-proto-0.9.0",
        source_subdir="opentelemetry",
        target_root="opentelemetry",
    ),
    Package(
        url="https://github.com/prometheus/client_model/archive/refs/heads/master.zip",
        name="prometheus",
        source_root="client_model-master",
        source_subdir=".",
        target_root="prometheus",
    ),
    Package(
        url="https://github.com/google/cel-spec/archive/refs/tags/v0.24.0.zip",
        name="cel",
        source_root="cel-spec-0.24.0",
        source_subdir="proto",
        target_root="cel",
    ),
}


def compile_all():
    proto_include = protoc.resources.files("grpc_tools") / "_proto"
    envoy = Path("./envoy")
    envoy_api = Path("./envoy/api")
    envoy_api_v2 = Path("./envoy/api/v2")
    output = Path("../src/envoy_data_plane")
    output_pb2 = Path("../src/envoy_data_plane_pb2")
    for outdir in [output, output_pb2]:
        if not outdir.exists():
            logger.msg(f"Creating output directory ({outdir})")
            outdir.mkdir(parents=True)
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
    args += [f"--python_betterproto2_out={output}"]
    args += [f"--python_out=pyi_out:{output_pb2}"]
    args += [f"--grpc_python_out={output_pb2}"]
    args += ["--python_betterproto2_opt=client_generation=sync_async_no_default"]
    args += ["--python_betterproto2_opt=server_generation=async"]
    args += ["--python_betterproto2_opt=pydantic_dataclasses"]
    protoc.main((*args, *proto_files))


def main():
    build_directory = Path("BUILD")
    if not build_directory.exists():
        logger.msg("Creating BUILD directory")
        build_directory.mkdir()
    os.chdir(build_directory)

    with ThreadPoolExecutor() as executor:
        for pkg in packages:
            if not pkg.target_exists:
                executor.submit(pkg.execute)
            else:
                logger.msg(f"{pkg.target} already exists, skipping download")

    compile_all()


if __name__ == "__main__":
    main()
