from __future__ import annotations

import importlib
import inspect

from ..core.base_scanner import Scanner
from ..core.node import Node
from ..core.node_kind import NodeKind
from ..core.metadata import NodeMetadata


class PythonScanner(Scanner):
    """Scans Python modules."""

    def scan(self, target: str) -> Node:
        module = importlib.import_module(target)

        root = Node(
            uid=module.__name__,
            name=module.__name__,
            kind=NodeKind.MODULE,
            metadata=NodeMetadata(
                module=module.__name__,
                qualified_name=module.__name__,
                documentation=inspect.getdoc(module),
            ),
        )

        self._scan_members(module, root)

        return root

    def _scan_members(self, obj, parent: Node) -> None:
        for name, member in inspect.getmembers(obj):

            if name.startswith("_"):
                continue

            node = self._create_node(name, member)

            if node is not None:
                parent.add_child(node)

    def _create_node(self, name: str, obj) -> Node | None:

        if inspect.ismodule(obj):
            kind = NodeKind.MODULE

        elif inspect.isclass(obj):
            kind = NodeKind.CLASS

        elif inspect.isfunction(obj):
            kind = NodeKind.FUNCTION

        elif inspect.ismethod(obj):
            kind = NodeKind.METHOD

        else:
            kind = NodeKind.VARIABLE

        return Node(
            uid=f"{obj.__module__}.{name}"
            if hasattr(obj, "__module__")
            else name,

            name=name,
            kind=kind,

            metadata=NodeMetadata(
                module=getattr(obj, "__module__", None),
                qualified_name=getattr(obj, "__qualname__", None),
                documentation=inspect.getdoc(obj),
            ),
        )