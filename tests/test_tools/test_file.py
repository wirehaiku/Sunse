"""
Tests for 'sunse.tools.file'.
"""

import pytest
from sunse.tools import file


def test_create(tmp_path):
    # setup
    path = tmp_path / "file.ext"

    # success
    file.create(str(path), "body")
    assert path.read_text() == "body"


def test_ensure(tmp_path):
    # setup
    dir = tmp_path / "dir"
    path = dir / "file.ext"

    # success
    file.ensure(path)
    assert dir.exists()


def test_glob(tmp_path):
    # setup
    for name in ["alpha", "bravo", "charlie"]:
        tmp_path.joinpath(f"{name}.ext").write_text("")

    # success
    assert file.glob(str(tmp_path), "*.ext") == [
        str(tmp_path / "alpha.ext"),
        str(tmp_path / "bravo.ext"),
        str(tmp_path / "charlie.ext"),
    ]


def test_read(tmp_path):
    # setup
    path = tmp_path / "file.ext"
    path.write_text("body")

    # success
    assert file.read(str(path)) == "body"


def test_write(tmp_path):
    # setup
    path = tmp_path / "file.ext"

    # success
    file.write(str(path), "body")
    assert path.read_text() == "body"
