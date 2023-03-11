"""
Tests for 'sunse.items.book'.
"""

import pytest
from sunse.items.book import Book
from sunse.items.note import Note


def test_init(book):
    # success
    assert book.dir
    assert book.ext == ".ext"


def test_eq(book):
    # success
    assert book == Book(book.dir, ".ext")
    assert book != Book("/nope", ".nope")
    assert book != "not a Book"


def test_hash(book):
    # success
    assert hash(book)


def test_iter(book):
    # success
    assert [note.name for note in list(book)] == ["alpha", "bravo", "charlie"]


def test_len(book):
    # success
    assert len(book) == 3


def test_repr(book):
    # setup
    book.dir = "/dir"

    # success
    assert repr(book) == "Book('/dir', '.ext')"


def test_create(book):
    # success
    note = book.create("test", "Test.")
    assert note.path == book.dir + "/test.ext"
    assert note.read() == "Test."


def test_read(book):
    # success
    assert book.read() == {
        "alpha": Note(book.dir + "/alpha.ext"),
        "bravo": Note(book.dir + "/bravo.ext"),
        "charlie": Note(book.dir + "/charlie.ext"),
    }
