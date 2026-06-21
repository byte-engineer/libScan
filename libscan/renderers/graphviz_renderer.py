from __future__ import annotations

from graphviz import Digraph

from ..core.node import Node
from ..core.node_kind import NodeKind


class GraphvizRenderer:
    """Converts a Node tree into a Graphviz graph."""

    def __init__(self):
        self.graph = Digraph("libscan")
        self.graph.attr(rankdir="LR")  # left → right layout

    def render(
        self,
        root: Node,
        output_path: str = "output/libscan",
        format: str = "svg",
    ) -> str:

        self.graph.clear()

        self._add_node(root)
        self._walk(root)

        return self.graph.render(
            output_path,
            format=format,
            cleanup=True,
        )

    def _walk(self, node: Node) -> None:
        for child in node.children:
            self.graph.edge(node.uid, child.uid)
            self._add_node(child)
            self._walk(child)

    def _add_node(self, node: Node) -> None:
        self.graph.node(
            node.uid,
            label=node.name,
            shape=self._shape(node.kind),
            style="filled",
            fillcolor=self._color(node.kind),
        )

    def _shape(self, kind: NodeKind) -> str:
        return {
            NodeKind.MODULE: "folder",
            NodeKind.CLASS: "box",
            NodeKind.FUNCTION: "ellipse",
            NodeKind.METHOD: "ellipse",
            NodeKind.PROPERTY: "note",
            NodeKind.VARIABLE: "plaintext",
            NodeKind.CONSTANT: "plaintext",
        }.get(kind, "box")

    def _color(self, kind: NodeKind) -> str:
        return {
            NodeKind.MODULE: "lightblue",
            NodeKind.CLASS: "orange",
            NodeKind.FUNCTION: "lightgreen",
            NodeKind.METHOD: "green",
            NodeKind.PROPERTY: "yellow",
            NodeKind.VARIABLE: "white",
            NodeKind.CONSTANT: "gray",
        }.get(kind, "white")