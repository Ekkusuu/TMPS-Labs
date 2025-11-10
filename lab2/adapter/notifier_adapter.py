"""Adapter that makes a LegacyNotifier conform to a simple Notifier interface.

Pattern: Adapter
"""

from typing import Optional
from lab2.adapter.legacy_notifier import LegacyNotifier


class NotifierAdapter:
    """Adapter: expose `notify(message: str)` while delegating to legacy `send(recipient, body)`.

    The adapter is configured with a default recipient; the facade can override it if needed.
    """

    def __init__(self, legacy: LegacyNotifier, default_recipient: Optional[str] = "library@local"):
        self._legacy = legacy
        self._recipient = default_recipient

    def notify(self, message: str, recipient: Optional[str] = None) -> None:
        r = recipient or self._recipient
        self._legacy.send(r, message)
