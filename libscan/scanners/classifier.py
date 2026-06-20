from __future__ import annotations

import inspect

from ..core.node_kind import NodeKind


class PythonClassifier:

    @staticmethod
    def classify(obj) -> NodeKind:

        if inspect.ismodule(obj):
            return NodeKind.MODULE

        if inspect.isclass(obj):
            return NodeKind.CLASS

        if (
            inspect.isfunction(obj)
            or inspect.isbuiltin(obj)
            or inspect.ismethod(obj)
            or inspect.ismethoddescriptor(obj)
            or inspect.isroutine(obj)
        ):
            return NodeKind.FUNCTION

        if isinstance(obj, property):
            return NodeKind.PROPERTY

        if isinstance(obj, (int, float, complex, str, bool, bytes)):
            return NodeKind.CONSTANT

        return NodeKind.VARIABLE