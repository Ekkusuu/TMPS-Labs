"""Facade providing a simplified API to the library system.

Pattern: Facade
"""

from typing import List, Optional
from lab2.models.book import Book
from lab2.domain.library import Library
from lab2.adapter.notifier_adapter import NotifierAdapter


class LibraryFacade:
    """Simplified interface combining a Library and a Notifier.

    The client uses this single façade to interact with the system.
    """

    def __init__(self, library: Library, notifier: NotifierAdapter):
        self._library = library
        self._notifier = notifier

    def add_book_and_notify(self, title: str, author: str, pages: int = 0, notify_recipient: Optional[str] = None) -> Book:
        book = Book(title, author, pages)
        self._library.add_book(book)
        msg = f"New book added: {book.title} by {book.author}"
        self._notifier.notify(msg, recipient=notify_recipient)
        return book

    def list_books(self) -> List[Book]:
        return self._library.list_books()

    def find(self, title: str) -> List[Book]:
        return self._library.find_by_title(title)
