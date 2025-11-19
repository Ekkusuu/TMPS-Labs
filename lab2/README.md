# Lab 2 — Structural Design Patterns: Book Library

Table of contents

- [Overview](#overview)
- [Implemented patterns](#implemented-patterns)
- [Domain & models](#domain--models)
- [Files and responsibilities](#files-and-responsibilities)
- [How to run](#how-to-run)
- [Example output](#example-output)
- [Pattern design notes & rationale](#pattern-design-notes--rationale)
- [Testing & verification suggestions](#testing--verification-suggestions)
- [Next steps](#next-steps)


## Implemented patterns

- **Adapter** — adapt a legacy notifier API to the new notifier interface so the rest of the system can use a consistent API.
- **Decorator** — wrap `Library` operations with additional behavior (logging) without changing `Library` internals.
- **Facade** — provide a simple, high-level `LibraryFacade` API for the single client to use; it composes `Library`, notifier(s) and decorators internally.

These patterns were selected to highlight common structural concerns: adapting third-party interfaces, extending behavior at runtime, and simplifying the client interface.

## Domain & models

Core entity: `Book` (same domain as Lab 1)

- `Book` (base model)

Simple class diagram (informal)

```
Book  <-- models/book.py
Library <-- domain/library.py
LibraryDecorator <-- decorator/library_decorator.py
LegacyNotifier / NotifierAdapter <-- adapter/
LibraryFacade <-- facade/library_facade.py
```

## Files and responsibilities

- `lab2/models/book.py` — `Book` data model used by the library.
- `lab2/domain/library.py` — `Library` core operations (add, remove, list, find).
- `lab2/adapter/legacy_notifier.py` — Example legacy notification API with a different interface.
- `lab2/adapter/notifier_adapter.py` — Adapter that adapts the legacy API to the expected notifier interface.
- `lab2/decorator/library_decorator.py` — `LibraryDecorator` wraps a `Library` and adds logging around operations (Decorator pattern).
- `lab2/facade/library_facade.py` — `LibraryFacade` composes the decorated `Library` and configured notifiers and exposes higher-level methods like `add_book_and_notify(...)`.
- `lab2/utilities/logger.py` — Small logger utility used by the decorator and client.
- `lab2/client.py` — Single client entry-point that uses `LibraryFacade` to perform a small scenario.

## How to run

From the project root, run the lab2 client. Two equivalent ways:

```bash
python3 -m lab2.client
```

or

```bash
python3 lab2/client.py
```

The `client` demonstrates:

1. Using a `LibraryFacade` to add books, list books and notify users.
2. Using the `NotifierAdapter` to call a legacy notifier implementation through the same interface.
3. Using `LibraryDecorator` to log operations performed on the `Library`.

## Example output

Example output from running the demo (format may vary slightly):

```
[LOG] add_book: adding Book(title='Refactor', author='M. Fowler', pages=448)
[LEGACY] sending SMS to +1000000000: New book added: Refactor
[LOG] add_book: adding Book(title='Design Patterns', author='G. Gamma', pages=395)
Library contents:
 - Book(title='Refactor', author='M. Fowler', pages=448)
 - Book(title='Design Patterns', author='G. Gamma', pages=395)
```

## Pattern design notes & rationale

- Adapter
  - Purpose: integrate a legacy notifier without touching `Library` or the client.
  - Implementation: `NotifierAdapter` implements the expected `notify(recipient, message)` interface and delegates to the legacy class' API.

- Decorator
  - Purpose: add cross-cutting behavior (logging) to `Library` operations at runtime, preserving single-responsibility for the core `Library` class.
  - Implementation: `LibraryDecorator` implements the same public API as `Library` but forwards calls while adding logging before/after the operation.

- Facade
  - Purpose: provide a single, simple interface for the client to interact with the library system. The facade hides composition details, wiring of adapter/decorator, and notifier calls.
  - Implementation: `LibraryFacade` composes the decorated `Library` and configured notifiers and exposes higher-level methods like `add_book_and_notify(...)`.

## Testing & verification suggestions

Suggested tests (pytest):

- Adapter
  - Create a `LegacyNotifier` instance and a `NotifierAdapter` wrapping it. Call `notify()` through the adapter and assert that the legacy method was invoked (or patch it).

- Decorator
  - Wrap a `Library` with `LibraryDecorator`, call `add_book`/`remove_book`, assert that the underlying `Library` changed state and that log calls were emitted.

- Facade
  - Use the `LibraryFacade` to add books and notify; assert library state and, if possible, that the notifier was called.

Example quick test sketch:

```python
from lab2.domain.library import Library
from lab2.decorator.library_decorator import LibraryDecorator

def test_decorator_adds_logging(capfd):
    lib = Library()
    decorated = LibraryDecorator(lib)
    decorated.add_book(Book('T','A',10))
    captured = capfd.readouterr()
    assert 'add_book' in captured.out
```

