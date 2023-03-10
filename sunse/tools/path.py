"""
File path manipulation functions.
"""

import os.path


def clean(path: str) -> str:
    """
    Return a clean normalised file path.
    """

    return os.path.normpath(path)


def expand(path: str) -> str:
    """
    Return a file path with expanded variables.
    """

    path = os.path.expanduser(path)
    path = os.path.expandvars(path)
    return os.path.normpath(path)


def ext(path: str) -> str:
    """
    Return a file path's extension with a leading dot.
    """

    ext = os.path.splitext(path)[-1]
    return "." + ext.lstrip(".")


def join(*elems: str) -> str:
    """
    Return a clean joined file path.
    """

    path = os.path.join(*elems)
    return os.path.normpath(path)


def name(path: str) -> str:
    """
    Return a file path's base name without extension.
    """

    base = os.path.basename(path)
    return os.path.splitext(base)[0]
