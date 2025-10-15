"""
SRP: This file only demonstrates usage / presentation.
DIP: Chooses concrete notifiers to inject into Library.
OCP: Add new notifier subclasses and list them here without changing library logic.
"""
from notification import EmailNotifier, SMSNotifier
from library import Library, Member

class DualNotifier(EmailNotifier):
    """Tiny example of extension: combine SMS + Email while reusing EmailNotifier.
    Shows OCP with minimal extra class
    """
    def __init__(self):
        self._email = EmailNotifier()
        self._sms = SMSNotifier()
    def notify(self, member: Member, message: str) -> None:  # type: ignore[override]
        self._email.notify(member, message)
        self._sms.notify(member, message)

def run_demo():
    notifier = DualNotifier()  
    lib = Library(notifier)

    lib.add_book("Clean Code", "Robert C. Martin", copies=1)
    lib.add_book("Domain-Driven Design", "Eric Evans", copies=1)

    alice = Member("Alice", "alice@example.com", "111-222")
    lib.add_member(alice)

    lib.borrow_book("Alice", "Clean Code")
    lib.borrow_book("Alice", "Clean Code") 
    lib.borrow_book("Alice", "Domain-Driven Design")
    lib.return_book("Alice", "Clean Code")

    print("Available titles:", lib.available_titles())

if __name__ == "__main__":
    run_demo()
