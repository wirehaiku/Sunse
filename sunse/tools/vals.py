"""
Value sanitisation functions.
"""

import os.path
import string

NAME_CHARS = string.ascii_lowercase + string.digits + "-_"


def body(text: str) -> str:
    """
    Return a clean note body string.
    """

    return "\n".join(line.rstrip() for line in text.splitlines()).rstrip()


def ext(text: str) -> str:
    """
    Return a clean file extension string.
    """

    return "." + text.lower().strip().lstrip(".")


def name(text: str) -> str:
    """
    Return a clean note name string.
    """

    text = text.lower().strip().replace(" ", "_")
    return "".join(char for char in text if char in NAME_CHARS).strip()


def path(text: str) -> str:
    """
    Return a clean file path string.
    """

    return os.path.normpath(text.strip())
