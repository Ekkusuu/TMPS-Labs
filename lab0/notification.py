from abc import ABC, abstractmethod

# no runtime import needed
Member = "Member"

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
