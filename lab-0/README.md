# TMPS - Lab 0

Implementing 3 SOLID principles (SRP, OCP, DIP) in a simple, library-themed Python project using a minimal, function-based design.

## 1. Introduction

This report describes a compact example that demonstrates three SOLID principles:

- SRP — Single Responsibility Principle
- OCP — Open/Closed Principle
- DIP — Dependency Inversion Principle

Scenario: manage late fees for a library—create a loan with overdue books, apply a fee reduction strategy, charge a payment gateway, and generate a fine receipt. The implementation is single-file and uses plain dicts and functions (no classes, no external libs).

## 2. Project Goals

- Provide a clear and runnable example for three SOLID principles.


## 3. Architecture Overview (single file)

- Domain (SRP): `create_book`, `new_loan`, `add_loan_item`, `loan_subtotal` (plain dict models and totals)
- Receipt (SRP): `generate_receipt(loan, reduction_amount)`
- Reductions (OCP): `no_reduction()`, `percentage_reduction(percent)`, `bulk_item_reduction(min_total_items, reduction_amount)` — each returns a strategy function `fn(loan) -> float`
- Payments (DIP): `fake_charge(amount) -> (ok: bool, message: str)`
- Processing (SRP + DIP): `process_fine(loan, reduction_fn, charge_fn)` orchestrates the flow

`demo()` constructs the data, selects a reduction function, injects a charge function, and prints the fine receipt.

## 4. SOLID Principles Applied

### 4.1 SRP — Single Responsibility Principle

- Loan-related functions manage data and totals only (`add_loan_item`, `loan_subtotal`).
- Presentation formats text only (`generate_receipt`).
- Orchestration coordinates the process only (`process_fine`).

Each unit has one reason to change (data, presentation, or orchestration), keeping concerns separated even in a single file.

### 4.2 OCP — Open/Closed Principle

- Strategy functions are the extension point. Add new reductions by writing a new function `def my_reduction(): return lambda loan: ...` without changing existing code.
- `process_fine` remains unchanged when adding strategies.

### 4.3 DIP — Dependency Inversion Principle

- `process_fine` depends on abstracted behavior via callables: `reduction_fn` and `charge_fn`.
- At runtime, we inject `fake_charge` and a chosen reduction function; swapping them requires no changes to `process_fine`.


## 5. Conclusion

This single-file implementation still cleanly demonstrates SRP, OCP, and DIP with minimal moving parts. Responsibilities are separated via small functions, extension points are explicit via strategy functions, and high-level orchestration depends on injected callables rather than concretions—making the code easy to extend and test.
