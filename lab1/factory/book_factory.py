from lab1.models.book import Ebook, PaperBook


# Pattern: Factory Method — creates concrete Book types from a kind string
class BookFactory:
    """Factory Method for creating books based on type string."""

    @staticmethod
    def create_book(kind: str, title: str, author: str, pages: int = 0, **kwargs):
        kind = (kind or "").lower()
        if kind == "ebook":
            return Ebook(title, author, pages, file_format=kwargs.get("file_format", "epub"))
        elif kind == "paper":
            return PaperBook(title, author, pages, hardcover=kwargs.get("hardcover", False))
        else:
            # default to PaperBook
            return PaperBook(title, author, pages)
