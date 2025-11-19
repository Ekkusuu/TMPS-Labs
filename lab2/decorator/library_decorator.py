from typing import List, Any

from lab2.domain.library import Library
from lab2.utilities.logger import logger
from lab2.models.book import Book


class LibraryDecorator(Library):
    """Base decorator that forwards attribute access and calls to the wrapped library.

    Inheriting from `Library` keeps the decorator compatible with code that
    expects a `Library` instance. The decorator implements the main API
    (add_book, list_books, find_by_title) by delegating to the wrapped object
    but also provides `__getattr__` to forward any additional attributes.
    """

    def __init__(self, wrapped: Library):
        self._wrapped = wrapped

    def add_book(self, book: Book) -> None:
        return self._wrapped.add_book(book)

    def list_books(self) -> List[Book]:
        return self._wrapped.list_books()

    def find_by_title(self, title: str) -> List[Book]:
        return self._wrapped.find_by_title(title)

    def __getattr__(self, item: str) -> Any:
        # Forward any other attribute or method to the wrapped object.
        return getattr(self._wrapped, item)


class LoggingLibraryDecorator(LibraryDecorator):
    """Decorator that logs calls to the wrapped `Library` operations.

    Use this decorator when you want transparent logging around library
    operations without modifying the core `Library` implementation.
    """

    def add_book(self, book: Book) -> None:
        logger(f"add_book: adding {book}")
        result = super().add_book(book)
        logger(f"add_book: done")
        return result


    def list_books(self) -> List[Book]:
        logger("list_books: retrieving list")
        books = super().list_books()
        logger(f"list_books: found {len(books)} books")
        return books

    def find_by_title(self, title: str) -> List[Book]:
        logger(f"find_by_title: searching for '{title}'")
        result = super().find_by_title(title)
        logger(f"find_by_title: found {len(result)} matches")
        return result


# Backwards compatibility: previous name used in client code
LibraryLoggerDecorator = LoggingLibraryDecorator
