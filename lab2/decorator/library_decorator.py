"""Decorator for Library to add cross-cutting behavior (logging).

Pattern: Decorator
"""

from lab2.domain.library import Library
from lab2.utilities.logger import logger
from typing import List
from lab2.models.book import Book


class LibraryLoggerDecorator:
    """Wrap a Library instance and log calls to its API."""

    def __init__(self, wrapped: Library):
        self._wrapped = wrapped

    def add_book(self, book: Book) -> None:
        logger(f"Adding book: {book}")
        self._wrapped.add_book(book)

    def list_books(self) -> List[Book]:
        books = self._wrapped.list_books()
        logger(f"Listing {len(books)} books")
        return books

    def find_by_title(self, title: str) -> List[Book]:
        logger(f"Searching for title containing: {title}")
        return self._wrapped.find_by_title(title)
