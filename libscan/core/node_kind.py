from enum import Enum, auto


class NodeKind(Enum):
    """Represents the type of a scanned object."""

    PACKAGE = auto()
    MODULE = auto()

    CLASS = auto()
    FUNCTION = auto()
    METHOD = auto()

    PROPERTY = auto()
    VARIABLE = auto()
    CONSTANT = auto()

    ENUM = auto()
    EXCEPTION = auto()

    UNKNOWN = auto()
