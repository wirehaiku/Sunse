"""
Tests for 'sunse.items.note'.
"""

import pytest
from sunse.items.note import Note


@pytest.fixture(scope="function")
def note(tmp_path):
    path = tmp_path / "alpha.txt"
    path.write_text("One.\nTwo.\nThree.\n")
    return Note(str(path))


def test_init(note):
    # success
    assert note.path.endswith("alpha.txt")
    assert note.name == "alpha"


def test_eq(note):
    # success
    assert note == Note(note.path)
    assert note != Note("/nope.txt")
    assert note != "not a Note"


def test_hash(note):
    # success
    assert hash(note)


def test_iter(note):
    # success
    assert list(note) == ["One.", "Two.", "Three."]


def test_len(note):
    # success
    assert len(note) == 16


def test_repr(note):
    # setup
    note.path = "alpha.txt"

    # success
    assert repr(note) == "Note('alpha.txt')"


def test_read(note):
    # success
    assert note.read() == "One.\nTwo.\nThree."


def test_write(note):
    # success
    note.write("test")
    assert open(note.path).read() == "test"
