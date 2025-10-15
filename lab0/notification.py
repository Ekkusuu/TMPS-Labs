from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

# Only import for type checking to avoid runtime circular imports
if TYPE_CHECKING: 
    from library import Member

class Notifier(ABC):
    """DIP: Abstraction for notifications used by Library.
    OCP: Add new channels by subclassing without changing Library.
    """

    @abstractmethod
    def notify(self, member: Member, message: str) -> None:
        pass

class EmailNotifier(Notifier):
    """SRP: Only handles email notifications."""
    def notify(self, member: Member, message: str) -> None:
        print(f"[Email] {getattr(member, 'email', '?')}: {message}")

class SMSNotifier(Notifier):
    """SRP: Only handles SMS notifications."""
    def notify(self, member: Member, message: str) -> None:
        print(f"[SMS] {getattr(member, 'phone', '?')}: {message}")
