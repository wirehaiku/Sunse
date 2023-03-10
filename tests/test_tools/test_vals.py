"""
Tests for 'sunse.tools.vals'.
"""

from sunse.tools import vals


def test_body():
    # success
    assert vals.body("\talpha   \n\tbravo   \n") == "\talpha\n\tbravo"


def test_ext():
    # success
    assert vals.ext("\text\n") == ".ext"


def test_name():
    # success
    assert vals.name("\tALPHA Bravo!\n") == "alpha_bravo"


def test_path():
    # success
    assert vals.path("\t/dire/././file.ext\n") == "/dire/file.ext"
