"""Collection helpers."""


def is_empty_collection(value):
    """Treat None and empty values as empty collections."""
    return value is None or (hasattr(value, "__len__") and len(value) == 0)
