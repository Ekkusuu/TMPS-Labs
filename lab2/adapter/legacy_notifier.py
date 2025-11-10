"""A legacy notifier API that doesn't match our new Notifier interface.

This simulates third-party or legacy code that we cannot change.
"""


class LegacyNotifier:
    """Legacy class with a different method signature.

    Method: `send(recipient: str, body: str)`
    """

    def __init__(self):
        # In a real legacy system this might hold configuration/state
        pass

    def send(self, recipient: str, body: str) -> None:
        # Simulate sending a message the old way
        print(f"[Legacy->{recipient}] {body}")
