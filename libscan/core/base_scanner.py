from __future__ import annotations

from abc import ABC, abstractmethod

from .node import Node


class Scanner(ABC):
    """Abstract scanner interface."""

    @abstractmethod
    def scan(self, target) -> Node:
        """Scan an object and return the root node."""
        raise NotImplementedError
