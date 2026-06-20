from __future__ import annotations

from ..python.scanner import PythonScanner

class Explorer:
    """High-level interface for scanning libraries."""

    def __init__(self):
        self._scanner = PythonScanner()

    def scan(self, module_name: str):
        return self._scanner.scan(module_name)
