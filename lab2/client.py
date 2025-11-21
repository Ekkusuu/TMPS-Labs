"""Single client for Lab2 demonstrating Adapter, Decorator and Facade patterns."""

from lab2.domain.library import Library
from lab2.adapter.legacy_notifier import LegacyNotifier
from lab2.adapter.notifier_adapter import NotifierAdapter
from lab2.decorator.library_decorator import LoggingDecorator, CountingDecorator
from lab2.facade.library_facade import LibraryFacade


def main():
    # Core library
    core_lib = Library()

    # Decorate library: count calls then add logging (two simple decorators)
    counted = CountingDecorator(core_lib)
    decorated = LoggingDecorator(counted)

    # Legacy notifier (third-party code) + Adapter
    legacy = LegacyNotifier()
    adapter = NotifierAdapter(legacy, default_recipient="lab2@local")

    # Facade composes the library and notifier and exposes a tiny API
    facade = LibraryFacade(decorated, adapter)

    # Use facade: add books (which triggers adapter notify) and list them
    facade.add_book_and_notify("Patterns for Humans", "C. Designer", 220)
    facade.add_book_and_notify("Structural Patterns", "D. Architect", 150, notify_recipient="team@local")

    # Example: search (this will exercise the `find` call and increment the counter)
    matches = facade.find("Patterns")
    print("\nSearch matches:")
    for m in matches:
        print(" -", m)

    print("\nBooks in library:")
    for b in facade.list_books():
        print(" -", b)

    # Show counts collected by the counting decorator
    print("\nOperation counts:")
    print(counted.counts)


if __name__ == "__main__":
    main()
