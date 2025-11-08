from typing import List


# Pattern: Singleton — single shared library instance
class LibrarySingleton:
    """A minimal Singleton library storing books."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._books = []
        return cls._instance

    def add_book(self, book):
        self._books.append(book)

    def list_books(self) -> List:
        return list(self._books)

    def clear(self):
        self._books.clear()
