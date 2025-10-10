# TMPS - Lab 0



## 1. Introduction

This report presents a small Python project that demonstrates three SOLID principles:

- SRP — Single Responsibility Principle
- OCP — Open/Closed Principle
- DIP — Dependency Inversion Principle

The example models a minimal order processing flow for a shop: creating an order with products, applying a discount strategy, charging a payment gateway, and generating an invoice.

## 2. Project Goals

- Provide a clear and runnable example for three SOLID principles.
- Keep the codebase simple, modular, and easy to extend.
- Use English for code, comments, and documentation.

## 3. Repository Structure

```
lab-0/
  main.py                 # Entry point: wires everything for a demo run
  order_system/
    __init__.py
    models.py             # Domain entities: Product, OrderItem, Order (SRP)
    discounts.py          # Discount abstraction and strategies (OCP)
    payments.py           # PaymentGateway abstraction + FakePaymentGateway (DIP)
    invoice.py            # InvoiceGenerator (SRP)
    processor.py          # OrderProcessor coordinates the flow (SRP + DIP)
```

## 4. Architecture Overview

The code is split into small modules, each with a single focus:

- models.py: domain data models and basic operations on orders.
- invoice.py: rendering an invoice summary string for a given order and discount.
- discounts.py: Discount abstraction plus several strategy implementations.
- payments.py: Payment gateway abstraction and a fake implementation.
- processor.py: application service that orchestrates discounting, charging, and invoice generation.

The `main.py` module composes these pieces and runs a short demo.

## 5. SOLID Principles Applied

### 5.1 SRP — Single Responsibility Principle

- Order: stores and manages order content (items, totals). It does not handle payments or presentation.
- InvoiceGenerator: produces a textual invoice; no business logic about discounts or charging.
- OrderProcessor: coordinates the workflow (compute total after discount, charge gateway, return invoice).

Why it matters: each class changes for one reason only (e.g., formatting invoice vs. computing totals), reducing coupling and making tests focused.

### 5.2 OCP — Open/Closed Principle

- Discount is an abstract base class.
- New strategies (e.g., PercentageDiscount, BulkItemDiscount) can be added without changing OrderProcessor or Order.

Why it matters: extension over modification makes the system safer and more maintainable when business rules change.

### 5.3 DIP — Dependency Inversion Principle

- OrderProcessor depends on the PaymentGateway abstraction, not a concrete class.
- At runtime we inject FakePaymentGateway, but any real gateway can be plugged in without changes to OrderProcessor.

Why it matters: decouples high-level policy (process an order) from low-level details (how to charge), enabling easy substitution and testing.


## 6. Example Output

```
INVOICE
Order ID: <uuid>
------------------------------
Mouse x2 @ 25.00 = 50.00
Keyboard x1 @ 45.00 = 45.00
Monitor x1 @ 150.00 = 150.00
------------------------------
Subtotal: 245.00
Discount: -24.50
Total: 220.50
```

Note: Exact order ID and totals depend on the selected discount strategy and items.

## 7. Conclusion

This project shows how SRP, OCP, and DIP can be applied in a compact Python codebase. The separation of concerns and clear abstractions make the system easier to understand, extend, and test.
