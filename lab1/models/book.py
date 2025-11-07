from copy import deepcopy


class Book:
    """Base Book model."""

    def __init__(self, title: str, author: str, pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def clone(self):
        """Prototype: return a deep copy of this book."""
        return deepcopy(self)


class Ebook(Book):
    def __init__(self, title: str, author: str, pages: int = 0, file_format: str = "epub"):
        super().__init__(title, author, pages)
        self.file_format = file_format

    def __repr__(self):
        return (
            f"Ebook(title={self.title!r}, author={self.author!r}, pages={self.pages}, "
            f"format={self.file_format!r})"
        )


class PaperBook(Book):
    def __init__(self, title: str, author: str, pages: int = 0, hardcover: bool = False):
        super().__init__(title, author, pages)
        self.hardcover = hardcover

    def __repr__(self):
        return (
            f"PaperBook(title={self.title!r}, author={self.author!r}, pages={self.pages}, "
            f"hardcover={self.hardcover})"
        )
