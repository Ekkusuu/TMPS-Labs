"""Simple decorators for `Library`.

This module provides two small, easy-to-understand decorators:

- `LoggingDecorator` — logs operations around calls.
- `CountingDecorator` — counts how many times operations are invoked.

Both are thin wrappers around a `Library` instance and keep the API
intentionally small so the behaviour is obvious.
"""

from typing import List

from lab2.domain.library import Library
from lab2.utilities.logger import logger
from lab2.models.book import Book


class LoggingDecorator:
    """Decorator that logs calls to the wrapped library."""

    def __init__(self, wrapped: Library):
        self._wrapped = wrapped

    def add_book(self, book: Book) -> None:
        logger(f"Adding book: {book}")
        self._wrapped.add_book(book)
        logger("Added book")

    def list_books(self) -> List[Book]:
        logger("Listing books")
        books = self._wrapped.list_books()
        logger(f"Found {len(books)} books")
        return books

    def find_by_title(self, title: str) -> List[Book]:
        logger(f"Searching for: {title}")
        return self._wrapped.find_by_title(title)


class CountingDecorator:
    """Decorator that counts calls to the wrapped library."""

    def __init__(self, wrapped: Library):
        self._wrapped = wrapped
        self.counts = {"add": 0, "list": 0, "find": 0}

    def add_book(self, book: Book) -> None:
        self.counts["add"] += 1
        return self._wrapped.add_book(book)

    def list_books(self) -> List[Book]:
        self.counts["list"] += 1
        return self._wrapped.list_books()

    def find_by_title(self, title: str) -> List[Book]:
        self.counts["find"] += 1
        return self._wrapped.find_by_title(title)


# Backwards compatibility: old demos used this name
LibraryLoggerDecorator = LoggingDecorator
