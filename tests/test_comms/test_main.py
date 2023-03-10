"""
Tests for 'sunse.comms.main'.
"""
import click
from sunse.comms.main import group


def test_group(book, run):
    # setup
    @group.command()
    @click.pass_obj
    def mock(book):
        for note in book:
            click.echo(note.name)

    # success
    code, outs = run(book, "mock")
    assert code == 0
    assert outs == "alpha\nbravo\ncharlie\n"
