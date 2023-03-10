"""
Value sanitisation functions.
"""

import string

NAME_CHARS = string.ascii_lowercase + string.digits + "-_"


def body(text: str) -> str:
    """
    Return a clean note body string.
    """

    return "\n".join(line.rstrip() for line in text.splitlines()).rstrip()


def name(text: str) -> str:
    """
    Return a clean note name string.
    """

    text = text.lower().strip().replace(" ", "_")
    return "".join(char for char in text if char in NAME_CHARS).strip()
