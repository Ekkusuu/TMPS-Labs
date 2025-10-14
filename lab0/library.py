"""
 - Member: user data + borrowed titles list.
 - Library: orchestrates inventory (plain dict) & uses Notifier abstraction (DIP).

Inventory structure: { title: { 'author': str, 'copies': int } }
"""

from typing import Dict, List, Optional
from notification import Notifier

class Member:
    """SRP: Stores member contact and borrowed titles."""
    def __init__(self, name: str, email: str, phone: str):
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed: List[str] = []

class Library:
    """SRP: Orchestrates borrow/return actions.
    DIP: Depends on Notifier abstraction only.
    OCP: New notification behavior via new Notifier subclasses; no Library change.
    """
    def __init__(self, notifier: Notifier):
        self._inventory: Dict[str, Dict[str, object]] = {}
        self._members: Dict[str, Member] = {}
        self._notifier = notifier

    # Registration
    def add_book(self, title: str, author: str, copies: int = 1) -> None:
        book = self._inventory.get(title)
        if book:
            book['copies'] = int(book['copies']) + copies
        else:
            self._inventory[title] = { 'author': author, 'copies': copies }

    def add_member(self, member: Member) -> None:
        self._members[member.name] = member

    # Operations
    def borrow_book(self, member_name: str, title: str) -> bool:
        member = self._members.get(member_name)
        book = self._inventory.get(title)
        if not member or not book:
            return False
        if book['copies'] <= 0:
            self._notifier.notify(member, f"'{title}' unavailable")
            return False
        book['copies'] -= 1
        member.borrowed.append(title)
        self._notifier.notify(member, f"Borrowed '{title}'")
        return True

    def return_book(self, member_name: str, title: str) -> bool:
        member = self._members.get(member_name)
        book = self._inventory.get(title)
        if not member or not book or title not in member.borrowed:
            return False
        book['copies'] += 1
        member.borrowed.remove(title)
        self._notifier.notify(member, f"Returned '{title}'")
        return True

    # Query
    def available_titles(self) -> List[str]:
        return [t for t, b in self._inventory.items() if b['copies'] > 0]
