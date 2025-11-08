from lab1.models.book import Book


# Pattern: Builder — fluent API for constructing Book instances
class BookBuilder:
    """Simple Builder for Book objects."""

    def __init__(self):
        self.reset()

    def reset(self):
        self._title = ""
        self._author = ""
        self._pages = 0
        return self

    def title(self, title: str):
        self._title = title
        return self

    def author(self, author: str):
        self._author = author
        return self

    def pages(self, pages: int):
        self._pages = pages
        return self

    def build(self) -> Book:
        book = Book(self._title, self._author, self._pages)
        self.reset()
        return book
