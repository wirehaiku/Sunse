"""
File I/O functions.
"""

import glob as glob_
import os


def create(path: str, body: str):
    """
    Create and write a string to a new file.
    """

    with open(path, "x", encoding="utf-8") as fobj:
        fobj.write(body)


def ensure(path: str):
    """
    Create a file path's parent directory if it does not exist.
    """

    dire = os.path.dirname(path)
    if not os.path.isdir(dire):
        os.makedirs(dire)


def glob(dire: str, ptrn: str) -> list[str]:
    """
    Return a list of all file paths in a directory matching a glob pattern.
    """

    path = os.path.join(dire, ptrn)
    return sorted(glob_.glob(path))


def read(path: str) -> str:
    """
    Return the contents of a file as a string.
    """

    with open(path, "r", encoding="utf-8") as fobj:
        return fobj.read()


def write(path: str, body: str):
    """
    Write a string to a new or existing file.
    """

    with open(path, "w", encoding="utf-8") as fobj:
        fobj.write(body)
