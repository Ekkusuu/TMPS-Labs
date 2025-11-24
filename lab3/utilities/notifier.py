from typing import Protocol
from datetime import datetime
from lab3.models.book import Book
import os


class Observer(Protocol):
    def update(self, event: str, book: Book) -> None:
        ...


class ConsoleNotifier:
    def update(self, event: str, book: Book) -> None:
        print(f"[ConsoleNotifier] Book {event}: {book}")


class FileNotifier:
    """A simple file-based notifier that appends events to `lab3/library.log`."""

    def __init__(self, log_path: str | None = None) -> None:
        if log_path:
            self.log_path = log_path
        else:
            # default location relative to this file
            base = os.path.dirname(__file__)
            self.log_path = os.path.join(base, '..', 'library.log')

    def update(self, event: str, book: Book) -> None:
        timestamp = datetime.now().isoformat()
        line = f"{timestamp} - Book {event}: {book}\n"
        try:
            with open(self.log_path, 'a', encoding='utf-8') as f:
                f.write(line)
        except Exception:
            # don't raise during notification
            pass
