from __future__ import annotations

import importlib
import inspect

from ..core.base_scanner import Scanner
from ..core.metadata import NodeMetadata
from ..core.node import Node
from ..core.node_kind import NodeKind
from .classifier import PythonClassifier


class PythonScanner(Scanner):
    """Scans Python modules and builds a tree of Node objects."""

    def __init__(self):
        self._visited: set[int] = set()
        self.max_depth = 2

    def scan(self, target: str, max_depth: int = 2) -> Node:
        """
        Scan a Python module.

        Args:
            target: Module name.
            max_depth: Maximum recursion depth.

        Returns:
            Root node.
        """

        self._visited.clear()
        self.max_depth = max_depth

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

        self._scan(module, root, depth=0)

        return root

    def _scan(self, obj, parent: Node, depth: int) -> None:
        """
        Recursively scan an object.
        """

        if depth >= self.max_depth:
            return

        object_id = id(obj)

        if object_id in self._visited:
            return

        self._visited.add(object_id)

        for name, member in inspect.getmembers(obj):

            # Skip private members
            if name.startswith("_"):
                continue

            node = self._create_node(name, member)

            if node is None:
                continue

            parent.add_child(node)

            # Only recurse into modules and classes
            if node.kind in (NodeKind.MODULE, NodeKind.CLASS):
                self._scan(member, node, depth + 1)

    def _create_node(self, name: str, obj) -> Node | None:
        """
        Create a Node from a Python object.
        """

        kind = PythonClassifier.classify(obj)

        metadata = NodeMetadata(
            module=getattr(obj, "__module__", None),
            qualified_name=getattr(obj, "__qualname__", None),
            documentation=inspect.getdoc(obj),
        )

        return Node(
            uid=self._make_uid(name, obj),
            name=name,
            kind=kind,
            metadata=metadata,
        )

    @staticmethod
    def _make_uid(name: str, obj) -> str:
        """
        Generate a unique identifier for a node.
        """

        module = getattr(obj, "__module__", "")

        qualname = getattr(obj, "__qualname__", name)

        if module:
            return f"{module}.{qualname}"

        return name