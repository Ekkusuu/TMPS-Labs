from typing import List, Protocol
from lab3.models.book import Book


class Observer(Protocol):
    def update(self, event: str, book: Book) -> None:
        ...


class Library:
    """Subject in the Observer pattern. Maintains a collection of books and notifies observers on changes."""

    def __init__(self) -> None:
        self._books: List[Book] = []
        self._observers: List[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def _notify(self, event: str, book: Book) -> None:
        for obs in list(self._observers):
            try:
                obs.update(event, book)
            except Exception:
                # keep notifying others even if one fails
                pass

    def add_book(self, book: Book) -> None:
        self._books.append(book)
        self._notify('added', book)

    def remove_book(self, book: Book) -> None:
        if book in self._books:
            self._books.remove(book)
            self._notify('removed', book)

    def list_books(self) -> List[Book]:
        return list(self._books)
