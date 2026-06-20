from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class NodeMetadata:
    """Additional information about a scanned object."""

    module: str | None = None
    qualified_name: str | None = None

    signature: str | None = None
    documentation: str | None = None

    source_file: str | None = None
    source_line: int | None = None
