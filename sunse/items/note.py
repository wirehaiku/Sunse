"""
Class definition for 'Note'.
"""

from typing import Any, Iterator

from sunse import tools


class Note:
    """
    A single plaintext note file in a Book.
    """

    def __init__(self, path: str):
        """
        Initialise the Note.
        """

        self.path = tools.vals.path(path)
        self.name = tools.vals.name(tools.path.name(self.path))

    def __eq__(self, note: Any) -> bool:
        """
        Return True if the Note is equal to another Note.
        """

        if not isinstance(note, Note):
            return NotImplemented

        return self.path == getattr(note, "path", None)

    def __hash__(self) -> int:
        """
        Return the Note's unique hash code.
        """

        return hash(self.__repr__())

    def __iter__(self) -> Iterator[str]:
        """
        Yield each line in the Note's body.
        """

        yield from self.read().splitlines()

    def __len__(self) -> int:
        """
        Return the length of the Note's body.
        """

        return len(self.read())

    def __repr__(self) -> str:
        """
        Return the Note as a code-representative string.
        """

        return f"Note({self.path!r})"

    def read(self) -> str:
        """
        Return the Note's body as a string.
        """

        return tools.vals.body(tools.file.read(self.path))

    def write(self, body: str):
        """
        Overwrite the Note's body with a string.
        """

        tools.file.write(self.path, tools.vals.body(body))
