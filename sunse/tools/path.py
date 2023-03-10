"""
File path manipulation functions.
"""

import os.path

from sunse import tools


def expand(path: str) -> str:
    """
    Return a file path with expanded variables.
    """

    path = os.path.expanduser(path)
    return os.path.expandvars(path)


def ext(path: str) -> str:
    """
    Return a file path's extension with a leading dot.
    """

    return os.path.splitext(path)[-1]


def join(*elems: str) -> str:
    """
    Return a clean joined file path.
    """

    return os.path.join(*elems)


def name(path: str) -> str:
    """
    Return a file path's base name without extension.
    """

    base = os.path.basename(path)
    return os.path.splitext(base)[0]
