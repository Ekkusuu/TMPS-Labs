"""Single client for Lab2 demonstrating Adapter, Decorator and Facade patterns."""

from lab2.domain.library import Library
from lab2.adapter.legacy_notifier import LegacyNotifier
from lab2.adapter.notifier_adapter import NotifierAdapter
from lab2.decorator.library_decorator import LibraryLoggerDecorator
from lab2.facade.library_facade import LibraryFacade


def main():
    # Core library
    core_lib = Library()

    # Decorate library to add logging behaviour (Decorator pattern)
    decorated = LibraryLoggerDecorator(core_lib)

    # Legacy notifier (third-party code) + Adapter
    legacy = LegacyNotifier()
    adapter = NotifierAdapter(legacy, default_recipient="lab2@local")

    # Facade composes the library and notifier and exposes a tiny API
    facade = LibraryFacade(decorated, adapter)

    # Use facade: add books (which triggers adapter notify) and list them
    facade.add_book_and_notify("Patterns for Humans", "C. Designer", 220)
    facade.add_book_and_notify("Structural Patterns", "D. Architect", 150, notify_recipient="team@local")

    print("\nBooks in library:")
    for b in facade.list_books():
        print(" -", b)


if __name__ == "__main__":
    main()
