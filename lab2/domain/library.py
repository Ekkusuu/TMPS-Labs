from typing import List
from lab2.models.book import Book


class Library:
    """Core library managing books.

    Responsibilities: add/list/find books. No notification responsibilities here.
    """

    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def list_books(self) -> List[Book]:
        return list(self._books)

    def find_by_title(self, title: str) -> List[Book]:
        title_lower = (title or "").lower()
        return [b for b in self._books if title_lower in b.title.lower()]
