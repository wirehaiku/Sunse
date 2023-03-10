"""
Click command function 'list'.
"""

import click
from sunse.comms.main import group


@group.command(name="list", short_help="List all notes.")
@click.pass_obj
def list_(book):
    """
    List all existing notes.
    """

    for note in book:
        click.echo(note.name)
