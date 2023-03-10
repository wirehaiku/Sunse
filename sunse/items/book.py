"""
Class definition for 'Book'.
"""

import typing
from typing import Any, Callable, Iterator

from sunse import tools
from sunse.items.note import Note


class Book:
    """
    A single directory containing plaintext Books.
    """

    def __init__(self, dire: str, ext: str):
        """
        Initialise the Book.
        """

        self.dire = tools.vals.path(dire)
        self.ext = tools.vals.ext(ext)

    def __eq__(self, book: Any) -> bool:
        """
        Return True if the Book is equal to another Book.
        """

        if not isinstance(book, Book):
            return NotImplemented

        return all(
            [
                self.dire == getattr(book, "dire", None),
                self.ext == getattr(book, "ext", None),
            ]
        )

    def __getitem__(self, name: str) -> Note:
        """
        Return a Note from the Book.
        """

        return self.read()[name]

    def __hash__(self) -> int:
        """
        Return the Book's unique hash code.
        """

        return hash(self.__repr__())

    def __iter__(self) -> Iterator[Note]:
        """
        Yield each Note in the Book's directory in alphabetical order.
        """

        notes = self.read().values()
        yield from sorted(notes, key=lambda note: note.name)

    def __len__(self) -> int:
        """
        Return the number of Notes in the Book.
        """

        return len(list(self.__iter__()))

    def __repr__(self) -> str:
        """
        Return the Book as a code-representative string.
        """

        return f"Book({self.dire!r}, {self.ext!r})"

    def create(self, name: str, body: str) -> Note:
        """
        Create and return a new Note.
        """

        name = tools.vals.name(name)
        path = tools.path.join(self.dire, name + self.ext)
        note = Note(path)
        note.write(body)
        return note

    def read(self) -> dict[str, Note]:
        """
        Return a dict of all Notes in the Book.
        """

        paths = tools.file.glob(self.dire, "*" + self.ext)
        return {note.name: note for note in map(Note, paths)}
