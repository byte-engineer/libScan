from __future__ import annotations

from ..scanners.python_scanner import PythonScanner
from .node import Node


class Explorer:
    """High-level interface for scanning libraries."""

    def __init__(self):
        self._scanner = PythonScanner()

    def scan(self, module_name: str, max_depth: int = 2) -> Node:
        """Scan a Python module."""

        return self._scanner.scan(module_name, max_depth=max_depth)