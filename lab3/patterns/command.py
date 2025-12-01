from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
from lab3.domain.library import Library
from lab3.models.book import Book


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        ...

    def undo(self) -> None:
        # optional
        pass


class AddBookCommand(Command):
    def __init__(self, library: Library, book: Book) -> None:
        self.library = library
        self.book = book
        self._executed = False

    def execute(self) -> None:
        self.library.add_book(self.book)
        self._executed = True

    def undo(self) -> None:
        if self._executed:
            self.library.remove_book(self.book)
            self._executed = False


class RemoveBookCommand(Command):
    def __init__(self, library: Library, book: Book) -> None:
        self.library = library
        self.book = book
        self._executed = False

    def execute(self) -> None:
        self.library.remove_book(self.book)
        self._executed = True

    def undo(self) -> None:
        if self._executed:
            self.library.add_book(self.book)
            self._executed = False


class CommandManager:
    def __init__(self) -> None:
        self._history: List[Command] = []

    def execute(self, cmd: Command) -> None:
        cmd.execute()
        self._history.append(cmd)

    def undo_last(self) -> None:
        if not self._history:
            return
        cmd = self._history.pop()
        try:
            cmd.undo()
        except Exception:
            pass
