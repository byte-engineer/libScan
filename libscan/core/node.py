from __future__ import annotations

from dataclasses import dataclass, field

from .metadata import NodeMetadata
from .node_kind import NodeKind


@dataclass(slots=True)
class Node:
    """Represents a node in the library tree."""

    uid: str
    name: str
    kind: NodeKind

    metadata: NodeMetadata = field(default_factory=NodeMetadata)

    parent: "Node | None" = None
    children: list["Node"] = field(default_factory=list)

    def add_child(self, child: "Node") -> None:
        """Add a child node."""

        child.parent = self
        self.children.append(child)

    @property
    def is_root(self) -> bool:
        return self.parent is None

    @property
    def child_count(self) -> int:
        return len(self.children)

    def walk(self):
        """Depth-first traversal."""

        yield self

        for child in self.children:
            yield from child.walk()

    def __repr__(self) -> str:
        return f"<{self.kind.name}: {self.name}>"
