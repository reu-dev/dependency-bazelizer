from typing import Set
from pathlib import Path
import dataclasses


@dataclasses.dataclass(frozen=True)
class PackageMetadata:
    name: str
    arch: str
    version: str


@dataclasses.dataclass(frozen=True)
class PackageFile:
    """File class that contains path of the file and whether or not it is ELF"""

    path: Path
    is_elf: bool


@dataclasses.dataclass()
class Package:
    """package info object contains name, version and architecture of a (Debian) Package"""

    name: str = ""
    arch: str = ""
    version: str = ""
    pinned_name: str = ""
    prefix: str = ""
    compatibility_level: int = 0
    package_dir: Path = Path()
    deps: Set[PackageMetadata] = dataclasses.field(default_factory=set)
    files: Set[PackageFile] = dataclasses.field(default_factory=set)
    elf_files: Set[Path] = dataclasses.field(default_factory=set)
    nonelf_files: Set[Path] = dataclasses.field(default_factory=set)
    rpaths: Set[str] = dataclasses.field(default_factory=set)