"""Simple Book model for lab2 (kept minimal)."""


class Book:
    """Domain model: Book (plain object)."""

    def __init__(self, title: str, author: str, pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self) -> str:
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"
