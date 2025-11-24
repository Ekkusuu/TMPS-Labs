# Lab 3 — Behavioral Pattern: Observer (Book Library)

**Topic:** Implementing a behavioral design pattern (Observer) in a book library system.

**Author:** <Your Name>  
Replace this with your actual name.

## Introduction / Motivation

Behavioral design patterns define common communication patterns between objects. The Observer pattern lets a subject (here, the `Library`) notify multiple observers when its state changes (books are added or removed). This is useful for decoupling the core domain logic from cross-cutting concerns such as logging, UI updates or external notifications.

## Implementation & Explanation

- **Main idea:** The `Library` class (subject) maintains a list of `Observer` objects. When a book is added or removed, the `Library` calls `update(event, book)` on each registered observer. Observers decide how to react (e.g., print to console, append to a log file).

- **Files & locations:**
  - `lab3/domain/library.py` — `Library` (subject) and `Observer` protocol. The methods `register_observer`, `remove_observer`, `add_book`, `remove_book`, and internal `_notify` implement the pattern.
  - `lab3/models/book.py` — `Book` dataclass used by the domain.
  - `lab3/utilities/notifier.py` — two concrete observers: `ConsoleNotifier` (prints events) and `FileNotifier` (appends events to `lab3/library.log`).
  - `lab3/client.py` — a single client that demonstrates registering observers and performing operations on the library.

- **Why Observer here:** The library must inform interested parties about changes (for example, update UIs, send email notifications, or write logs). Observer decouples these concerns: `Library` doesn't need to know what observers do, only that it should notify them.

### Key code snippets

- `Library._notify` (in `lab3/domain/library.py`):

```
def _notify(self, event: str, book: Book) -> None:
    for obs in list(self._observers):
        try:
            obs.update(event, book)
        except Exception:
            pass
```

- `ConsoleNotifier.update` (in `lab3/utilities/notifier.py`):

```
def update(self, event: str, book: Book) -> None:
    print(f"[ConsoleNotifier] Book {event}: {book}")
```

## Results / How to run

From the repository root run (Windows `cmd.exe`):

```cmd
python lab3\client.py
```

Expected behavior:
- Console prints notifications for book additions and removals provided by `ConsoleNotifier`.
- `lab3/library.log` will contain a timestamped record of events (if `FileNotifier` is registered).

## Conclusions

The Observer pattern cleanly separates the library domain logic from notification concerns. New observers can be added without modifying `Library`. This makes the system easier to extend and maintain.

---
Replace the author line and expand the README with screenshots or further tests if required by your instructor.
