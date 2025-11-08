from lab1.factory.book_factory import EbookFactory, PaperBookFactory
from lab1.builder.book_builder import BookBuilder
from lab1.domain.library_singleton import LibrarySingleton
from lab1.models.book import Ebook


def demo():
    lib = LibrarySingleton()
    lib.clear()

    # Factory Method (full version: abstract creator + concrete creators)
    ebook_factory = EbookFactory()
    paper_factory = PaperBookFactory()

    ebook = ebook_factory.create_book("Factory Patterns in Py", "A. Dev", 120, file_format="pdf")
    paper = paper_factory.create_book("Understanding Patterns", "B. Coder", 350, hardcover=True)

    lib.add_book(ebook)
    lib.add_book(paper)

    # Builder
    builder = BookBuilder()
    built = builder.title("Built Book").author("Builder Author").pages(200).build()
    lib.add_book(built)

    # Prototype
    clone_of_ebook = ebook.clone()
    # tweak clone
    if isinstance(clone_of_ebook, Ebook):
        clone_of_ebook.title = clone_of_ebook.title + " (clone)"
    lib.add_book(clone_of_ebook)

    return lib


if __name__ == "__main__":
    lib = demo()
    for b in lib.list_books():
        print(b)
