# TMPS - Lab 0

Implementing 3 SOLID principles (SRP, OCP, DIP) in a small book-library example.

## 1. Introduction

This report describes a compact, multi-file example that demonstrates three SOLID principles:

- SRP — Single Responsibility Principle
- OCP — Open/Closed Principle
- DIP — Dependency Inversion Principle

Scenario: a member borrows and returns books; the system notifies them through one or more channels. We separate: data (`Member`), orchestration (`Library`), and infrastructure (`Notifier` + concrete channels). Inventory is a plain dictionary to keep the model minimal.

## 2. Project Goals

- Provide a clear, runnable class-based example for SRP, OCP, DIP.
- Keep code minimal (only stdlib + `abc`).
- Show how composition + abstraction support extension.

## 3. Architecture Overview (3 files)

Files:

1. `notification.py` – `Notifier` ABC + two concrete channels (`EmailNotifier`, `SMSNotifier`).
2. `library.py` – `Member` class + `Library` orchestrator and in-memory inventory dict.
3. `main.py` – Demo / presentation only (SRP) assembling everything and running a scenario. Includes a tiny `DualNotifier` example combining two channels without modifying `Library`.

### 3.1 `notification.py`
- `Notifier` (ABC) (DIP/OCP): Abstraction used by `Library`.
- `EmailNotifier`, `SMSNotifier` (SRP): Each prints a message for its channel.

### 3.2 `library.py`
- `Member` (SRP): Only identity + borrowed titles list.
- `Library` (SRP orchestrator): Manages borrowing/returning using a dict inventory: `{ title: { 'author': str, 'copies': int } }`. Depends only on `Notifier` abstraction (DIP).

### 3.3 `main.py`
- Builds concrete notifier(s), injects into `Library`, performs sample operations, prints results.

### 3.4 Data Flow
1. Create concrete notifier(s).
2. Construct `Library` with notifier (inversion of dependency).
3. Add books & member.
4. Borrow / return attempts trigger channel notifications.
5. Query remaining available titles.

## 4. SOLID Principles Applied

### 4.1 SRP — Single Responsibility Principle
- `Member`: Stores user data, nothing else.
- `Library`: Coordinates inventory + member interactions only (no channel specifics).
- Each notifier subclass: Prints a message in exactly one way.
- `main.py`: Demo / wiring only.

Each piece has one reason to change (data structure, orchestration rule, output formatting, or demo flow).

### 4.2 OCP — Open/Closed Principle
- Add a new channel by subclassing `Notifier` (e.g., `class PushNotifier(Notifier): ...`). `Library` remains untouched.
- Combine behaviors (e.g., the demo `DualNotifier`) without altering existing classes.

### 4.3 DIP — Dependency Inversion Principle
- `Library` (high-level policy) depends on `Notifier` abstraction, never imports concrete implementations.
- `main.py` chooses which concrete notifier to pass in.
- Swapping strategies (Email only, SMS only, combined) requires no changes inside `Library`.

## 5. Example Run

Run the demo:

```
python main.py
```

Sample output (your order may vary):

```
[Email] alice@example.com: Borrowed 'Clean Code'
[SMS] 111-222: Borrowed 'Clean Code'
[Email] alice@example.com: 'Clean Code' unavailable
[SMS] 111-222: 'Clean Code' unavailable
[Email] alice@example.com: Borrowed 'Domain-Driven Design'
[SMS] 111-222: Borrowed 'Domain-Driven Design'
[Email] alice@example.com: Returned 'Clean Code'
[SMS] 111-222: Returned 'Clean Code'
Available titles: ['Clean Code']
```

## 6. Conclusion

With only four tiny classes total (`Notifier` + 2 channels + `Library` + simple `Member`), the example shows:

- SRP: Each class has exactly one concern.
- OCP: Add new notifier subclasses without modifying existing orchestrator code.
- DIP: `Library` depends on an abstraction injected from outside.

The design stays extremely small while still illustrating the principles clearly.
