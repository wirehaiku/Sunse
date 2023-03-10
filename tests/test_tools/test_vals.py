"""
Tests for 'sunse.tools.vals'.
"""

from sunse.tools import vals


def test_body():
    # success
    assert vals.body("\talpha   \n\tbravo   \n") == "\talpha\n\tbravo"


def test_name():
    # success
    assert vals.name("\tALPHA Bravo!\n") == "alpha_bravo"
