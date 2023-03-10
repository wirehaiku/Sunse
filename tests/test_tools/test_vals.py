"""
Tests for 'sunse.tools.vals'.
"""

from sunse.tools import vals


def test_body():
    # success
    body = vals.body("\talpha   \n\tbravo   \n")
    assert body == "\talpha\n\tbravo"


def test_name():
    # success
    name = vals.name("\tALPHA Bravo!\n")
    assert name == "alpha_bravo"
