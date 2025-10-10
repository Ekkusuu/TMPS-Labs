"""Single-file SOLID demo (SRP, OCP, DIP).
Run with: python3 main.py
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Protocol
import uuid


# Domain models (SRP)
@dataclass
class Product:
    id: str
    name: str
    price: float


@dataclass
class OrderItem:
    product: Product
    quantity: int


@dataclass
class Order:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    items: List[OrderItem] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be > 0")
        self.items.append(OrderItem(product=product, quantity=quantity))

    def total_without_discount(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)


class InvoiceGenerator:
    """Render invoice text for an order."""

    @staticmethod
    def generate(order: Order, discount_amount: float) -> str:
        lines = ["INVOICE", f"Order ID: {order.id}", "-" * 30]
        for item in order.items:
            lines.append(
                f"{item.product.name} x{item.quantity} @ {item.product.price:.2f} = {item.product.price * item.quantity:.2f}"
            )
        subtotal = order.total_without_discount()
        lines.append("-" * 30)
        lines.append(f"Subtotal: {subtotal:.2f}")
        lines.append(f"Discount: -{discount_amount:.2f}")
        lines.append(f"Total: {subtotal - discount_amount:.2f}")
        return "\n".join(lines)


# Discounts (OCP)
class Discount:
    def calculate(self, order: Order) -> float:  # interface-like
        raise NotImplementedError


class NoDiscount(Discount):
    def calculate(self, order: Order) -> float:
        return 0.0


class PercentageDiscount(Discount):
    def __init__(self, percent: float):
        if percent < 0 or percent > 100:
            raise ValueError("percent must be between 0 and 100")
        self.percent = percent

    def calculate(self, order: Order) -> float:
        return order.total_without_discount() * (self.percent / 100.0)


class BulkItemDiscount(Discount):
    def __init__(self, min_total_items: int, discount_amount: float):
        self.min_total_items = min_total_items
        self.discount_amount = discount_amount

    def calculate(self, order: Order) -> float:
        total_items = sum(item.quantity for item in order.items)
        if total_items >= self.min_total_items:
            return min(self.discount_amount, order.total_without_discount())
        return 0.0


# Payments (DIP)
class PaymentResult:
    def __init__(self, success: bool, message: str = ""):
        self.success = success
        self.message = message


class PaymentGateway(Protocol):
    def charge(self, amount: float, **kwargs) -> PaymentResult:
        ...


class FakePaymentGateway:
    def charge(self, amount: float, **kwargs) -> PaymentResult:
        if amount <= 0:
            return PaymentResult(False, "Amount must be > 0")
        return PaymentResult(True, f"Charged {amount:.2f} successfully (fake gateway).")


# Application service (SRP + DIP)
class OrderProcessor:
    def __init__(self, payment_gateway: PaymentGateway, discount_strategy: Discount):
        self.payment_gateway = payment_gateway
        self.discount_strategy = discount_strategy

    def process(self, order: Order) -> str:
        subtotal = order.total_without_discount()
        discount_amount = self.discount_strategy.calculate(order)
        total = max(subtotal - discount_amount, 0.0)

        payment_result = self.payment_gateway.charge(total)
        if not payment_result.success:
            return f"Payment failed: {payment_result.message}"

        return InvoiceGenerator.generate(order, discount_amount)


def demo() -> None:
    # products
    p1 = Product(id="p1", name="Mouse", price=25.0)
    p2 = Product(id="p2", name="Keyboard", price=45.0)
    p3 = Product(id="p3", name="Monitor", price=150.0)

    # order
    order = Order()
    order.add_item(p1, quantity=2)
    order.add_item(p2, quantity=1)
    order.add_item(p3, quantity=1)

    # choose discount strategy (OCP)
    discount = PercentageDiscount(10)
    # discount = NoDiscount()
    # discount = BulkItemDiscount(min_total_items=4, discount_amount=50.0)

    # inject payment gateway (DIP)
    gateway = FakePaymentGateway()

    processor = OrderProcessor(payment_gateway=gateway, discount_strategy=discount)
    invoice = processor.process(order)
    print(invoice)


if __name__ == "__main__":
    demo()
