"""
Tests for 'sunse.tools.path'.
"""

import os

from sunse.tools import path


def test_expand():
    # setup
    os.environ["HOME"] = "/home/test"
    os.environ["TEST"] = "file.ext"

    # success
    assert path.expand("~/$TEST") == "/home/test/file.ext"


def test_ext():
    # success
    assert path.ext("/dir/file.ext") == ".ext"


def test_join():
    # success
    assert path.join("/dir", "file.ext") == "/dir/file.ext"


def test_name():
    # success
    assert path.name("/dir/file.ext") == "file"
