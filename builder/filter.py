"""Filter requirements."""
from pathlib import Path

from builder.pip import write_requirement, parse_requirements

FILTERED = {"RPi.GPIO": ["amd64", "i386", "armhf"]}


def filter_requirements(requirement: Path, arch: str) -> None:
    """Filter requirements."""
    requirements = parse_requirements(requirement)

    for requitement in FILTERED:
        if arch in FILTERED[requitement]:
            for req in requirements:
                if req.startswith(requitement):
                    requirements.remove(req)

    write_requirement(requirement, requirements)
