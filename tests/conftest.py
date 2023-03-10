"""
Global unit-testing fixtures.
"""

import os

import click
import pytest
from click import testing
from sunse.comms.main import group
from sunse.items.book import Book


@pytest.fixture(scope="function")
def book(tmp_path):
    """
    Return a mock Book populated with test Notes.
    """

    for name in ["alpha", "bravo", "charlie"]:
        tmp_path.joinpath(f"{name}.ext").write_text(f"Note {name}.")

    return Book(str(tmp_path), ".ext")


@pytest.fixture(scope="function")
def run():
    """
    Return a function that returns the status code and output of a Click command.
    """

    def func(book: Book, args: str) -> tuple[int, str]:
        os.environ.update({"SUNSE_DIR": book.dire, "SUNSE_EXT": book.ext})
        runner = click.testing.CliRunner()
        result = runner.invoke(group, args.split())
        if result.exception:
            raise result.exception

        return result.exit_code, result.output

    return func
