"""
Tests for 'sunse.comms.list'.
"""

import click
from sunse.comms.list import list_


def test_list(book, run):
    # success
    code, outs = run(book, "list")
    assert code == 0
    assert outs == "alpha\nbravo\ncharlie\n"
