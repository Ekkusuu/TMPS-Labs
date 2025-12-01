from typing import List, Protocol
from lab3.models.book import Book


class SortingStrategy(Protocol):
    def sort(self, books: List[Book]) -> List[Book]:
        ...


class SortByTitle:
    def sort(self, books: List[Book]) -> List[Book]:
        return sorted(books, key=lambda b: (b.title or '').lower())


class SortByAuthor:
    def sort(self, books: List[Book]) -> List[Book]:
        return sorted(books, key=lambda b: (b.author or '').lower())


class SortByYear:
    def sort(self, books: List[Book]) -> List[Book]:
        return sorted(books, key=lambda b: b.year)


class SortingContext:

    def __init__(self, strategy: SortingStrategy) -> None:
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy) -> None:
        self._strategy = strategy

    def sort(self, books: List[Book]) -> List[Book]:
        return self._strategy.sort(books)
