"""Client for lab3 demonstrating the Observer pattern in a book library."""
from lab3.domain.library import Library
from lab3.models.book import Book
from lab3.utilities.notifier import ConsoleNotifier, FileNotifier


def main() -> None:
    lib = Library()

    console = ConsoleNotifier()
    file_notifier = FileNotifier()  # writes to lab3/library.log by default

    # register observers
    lib.register_observer(console)
    lib.register_observer(file_notifier)

    # create some books
    b1 = Book("The Pragmatic Programmer", "Andrew Hunt", 1999)
    b2 = Book("Clean Code", "Robert C. Martin", 2008)

    # add books -> observers get notified
    lib.add_book(b1)
    lib.add_book(b2)

    # list current books
    print("Current library:")
    for b in lib.list_books():
        print(" -", b)

    # remove a book -> observers get notified
    lib.remove_book(b1)


if __name__ == '__main__':
    main()
