"""Small logging utility used by decorators and client."""

def logger(message: str) -> None:
    print(f"[LOG] {message}")
