# Lab 3 — Behavioral Design Patterns: Book Library

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


## Overview

This lab demonstrates three behavioral design patterns applied to a simple book library domain: **Observer**, **Command**, and **Strategy**. The goal is to decouple responsibilities for notifications, encapsulate operations as objects that can be executed/undone, and provide interchangeable sorting algorithms for listing books.

**Author:** <Your Name> — replace with your actual name.


## Implemented patterns

- **Observer** — `Library` acts as a subject and notifies registered observers when books are added or removed. Concrete observers in this lab: `ConsoleNotifier`, `FileNotifier`.
- **Command** — operations (`AddBookCommand`, `RemoveBookCommand`) wrap library actions; `CommandManager` executes commands and supports undo.
- **Strategy** — interchangeable sorting strategies for presenting `Library` contents: `SortByTitle`, `SortByAuthor`, `SortByYear`.


## Domain & models

Core entity: `Book` (simple dataclass containing `title`, `author`, `year`). The domain `Library` stores a list of books and exposes `add_book`, `remove_book`, and `list_books`.

Informal class map:

```
Book
Library (subject)
Observers: ConsoleNotifier, FileNotifier
Commands: AddBookCommand, RemoveBookCommand, CommandManager
Strategies: SortByTitle, SortByAuthor, SortByYear
```


## Files and responsibilities

- `lab3/models/book.py` — `Book` dataclass.
- `lab3/domain/library.py` — `Library` subject and `Observer` protocol; notification logic lives here.
- `lab3/utilities/notifier.py` — concrete observers: `ConsoleNotifier`, `FileNotifier`.
- `lab3/patterns/command.py` — Command base class, `AddBookCommand`, `RemoveBookCommand`, and `CommandManager` (exec + undo history).
- `lab3/patterns/strategy.py` — `SortByTitle`, `SortByAuthor`, `SortByYear` strategies for listing books.
- `lab3/client.py` — single client/demo that wires the system: registers observers, executes commands, demonstrates strategy-based listings and undo.


## How to run

From the repository root you can run the demo in two equivalent ways.

Windows `cmd.exe`:

```cmd
python -m lab3.client
```
or
```cmd
python lab3\client.py
```

What the demo does:
1. Creates a `Library` and registers `ConsoleNotifier` and `FileNotifier` as observers.
2. Uses `CommandManager` to execute `AddBookCommand` instances to add several books (observers are notified).
3. Lists books using three sorting `Strategy` implementations.
4. Executes a `RemoveBookCommand` and demonstrates undo by calling `CommandManager.undo_last()`.


## Example output

Example console output when running the demo (timestamps omitted for brevity):

```
[ConsoleNotifier] Book added: The Pragmatic Programmer by Andrew Hunt (1999)
[ConsoleNotifier] Book added: Clean Code by Robert C. Martin (2008)
[ConsoleNotifier] Book added: Refactoring by Martin Fowler (1999)

List sorted by title:
 - Clean Code by Robert C. Martin (2008)
 - Refactoring by Martin Fowler (1999)
 - The Pragmatic Programmer by Andrew Hunt (1999)

List sorted by author:
 - The Pragmatic Programmer by Andrew Hunt (1999)
 - Refactoring by Martin Fowler (1999)
 - Clean Code by Robert C. Martin (2008)

List sorted by year:
 - The Pragmatic Programmer by Andrew Hunt (1999)
 - Refactoring by Martin Fowler (1999)
 - Clean Code by Robert C. Martin (2008)

Removing a book via Command and then undoing it (observers notified):
[ConsoleNotifier] Book removed: Refactoring by Martin Fowler (1999)

Undo last command (restore removed book):
[ConsoleNotifier] Book added: Refactoring by Martin Fowler (1999)
```

`lab3/library.log` will contain timestamped lines written by `FileNotifier` if present.


## Pattern design notes & rationale

- Observer
    - Purpose: keep the `Library` focused on core domain operations while allowing multiple independent reactions to changes (logging, UI updates, remote notifications).
    - Implementation: `Library` stores a list of observers and calls `update(event, book)` on each in `_notify()`.

- Command
    - Purpose: encapsulate library operations as objects so they can be executed, queued, logged, and undone.
    - Implementation: each command implements `execute()` and optionally `undo()`. `CommandManager` keeps a history stack to support `undo_last()`.

- Strategy
    - Purpose: allow swapping sorting algorithms at runtime without changing `Library` or client code.
    - Implementation: each strategy implements `sort(books)` and can be used by the client to format the `list_books()` output.


## Testing & verification suggestions

Suggested tests (pytest):

- Library / Observer
    - Register a test observer (callable or small object capturing calls), add/remove a book and assert `update` was called with correct event and book.

- Command
    - Execute `AddBookCommand` and assert the book appears in the library; call `undo()` and assert the book is removed.

- Strategy
    - Given an unsorted list of `Book` objects, assert each `SortBy*` produces the expected ordering.

Quick test sketch (pytest):

```python
from lab3.domain.library import Library
from lab3.models.book import Book

def test_add_notifies(monkeypatch):
        lib = Library()
        called = []

        class T:
                def update(self, event, book):
                        called.append((event, book.title))

        t = T()
        lib.register_observer(t)
        b = Book('T', 'A', 10)
        lib.add_book(b)
        assert called and called[0][0] == 'added'
```


## Next steps

- Add more concrete observers (e.g., JSON logger, email notifier stub) to demonstrate extension without modifying `Library`.
- Add unit tests and run them via `pytest` for automated verification.
- Implement additional behavioral patterns (e.g., `Iterator` to provide a custom traversal, or `State` for checkout workflow) if required by the assignment.

---
Replace the author line with your name and expand with screenshots or additional tests if needed for submission.
