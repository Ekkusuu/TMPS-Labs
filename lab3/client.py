"""Client for lab3 demonstrating the Observer pattern in a book library."""
from lab3.domain.library import Library
from lab3.models.book import Book
from lab3.utilities.notifier import ConsoleNotifier, FileNotifier
from lab3.patterns.command import CommandManager, AddBookCommand, RemoveBookCommand
from lab3.patterns.strategy import SortByTitle, SortByAuthor, SortByYear, SortingContext


def main() -> None:
    lib = Library()

    # Observers
    console = ConsoleNotifier()
    file_notifier = FileNotifier()
    lib.register_observer(console)
    lib.register_observer(file_notifier)

    # Command manager
    cm = CommandManager()

    # create books
    b1 = Book("The Pragmatic Programmer", "Andrew Hunt", 1999)
    b2 = Book("Clean Code", "Robert C. Martin", 2008)
    b3 = Book("Refactoring", "Martin Fowler", 1999)

    # Use Command pattern to add books
    cm.execute(AddBookCommand(lib, b1))
    cm.execute(AddBookCommand(lib, b2))
    cm.execute(AddBookCommand(lib, b3))

    # Use Strategy pattern via a SortingContext to list books in different orders
    ctx = SortingContext(SortByTitle())
    print("\nList sorted by title:")
    for book in ctx.sort(lib.list_books()):
        print(" -", book)

    ctx.set_strategy(SortByAuthor())
    print("\nList sorted by author:")
    for book in ctx.sort(lib.list_books()):
        print(" -", book)

    ctx.set_strategy(SortByYear())
    print("\nList sorted by year:")
    for book in ctx.sort(lib.list_books()):
        print(" -", book)

    # Demonstrate undo: remove last added book and then undo
    print("\nRemoving a book via Command and then undoing it (observers notified):")
    rm_cmd = RemoveBookCommand(lib, b3)
    cm.execute(rm_cmd)

    print("\nUndo last command (restore removed book):")
    cm.undo_last()


if __name__ == '__main__':
    main()
