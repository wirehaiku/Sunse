"""
Tests for 'sunse.tools.path'.
"""

import os

from sunse.tools import path


def test_clean():
    # success
    assert path.clean("/dire/././file.ext") == "/dire/file.ext"


def test_expand():
    # setup
    os.environ["HOME"] = "/home/test"
    os.environ["TEST"] = "file.ext"

    # success
    assert path.expand("~/$TEST") == "/home/test/file.ext"


def test_ext():
    # success
    assert path.ext("/dire/file.ext") == ".ext"


def test_join():
    # success
    assert path.join("/dire", "file.ext") == "/dire/file.ext"


def test_name():
    # success
    assert path.name("/dire/file.ext") == "file"
