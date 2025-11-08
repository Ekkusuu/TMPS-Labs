from abc import ABC, abstractmethod
from lab1.models.book import Ebook, PaperBook, Book


class BookFactory(ABC):
    """Abstract Creator declaring the factory method."""

    @abstractmethod
    def create_book(self, title: str, author: str, pages: int = 0, **kwargs) -> Book:
        """Create and return a concrete Book product."""
        raise NotImplementedError


class EbookFactory(BookFactory):
    """Concrete Creator for `Ebook` objects."""

    def __init__(self, default_format: str = "epub"):
        self.default_format = default_format

    def create_book(self, title: str, author: str, pages: int = 0, **kwargs) -> Ebook:
        file_format = kwargs.get("file_format", self.default_format)
        return Ebook(title, author, pages, file_format=file_format)


class PaperBookFactory(BookFactory):
    """Concrete Creator for `PaperBook` objects."""

    def __init__(self, default_hardcover: bool = False):
        self.default_hardcover = default_hardcover

    def create_book(self, title: str, author: str, pages: int = 0, **kwargs) -> PaperBook:
        hardcover = kwargs.get("hardcover", self.default_hardcover)
        return PaperBook(title, author, pages, hardcover=hardcover)


__all__ = [
    "BookFactory",
    "EbookFactory",
    "PaperBookFactory",
]
