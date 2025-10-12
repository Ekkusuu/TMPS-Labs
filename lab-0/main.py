# Simple ID generator
_COUNTER = 0

def _next_id(prefix: str = "loan") -> str:
    global _COUNTER
    _COUNTER += 1
    return f"{prefix}-{_COUNTER}"


# Domain (SRP): books, loan, and totals using plain dicts
def create_book(id: str, title: str, daily_late_fee: float) -> dict:
    return {"id": id, "title": title, "daily_late_fee": float(daily_late_fee)}


def new_loan() -> dict:
    return {"id": _next_id("loan"), "items": []}


def add_loan_item(loan: dict, book: dict, days_overdue: int, quantity: int = 1) -> None:
    if quantity <= 0:
        raise ValueError("quantity must be > 0")
    if days_overdue < 0:
        raise ValueError("days_overdue must be >= 0")
    loan["items"].append({
        "book": book,
        "days_overdue": int(days_overdue),
        "quantity": int(quantity),
    })


def loan_subtotal(loan: dict) -> float:
    return sum(
        it["book"]["daily_late_fee"] * it["days_overdue"] * it["quantity"]
        for it in loan["items"]
    )


# Presentation (SRP): receipt
def generate_receipt(loan: dict, reduction_amount: float) -> str:
    lines = ["FINE RECEIPT", f"Loan ID: {loan['id']}", "-" * 30]
    for it in loan["items"]:
        item_total = it["book"]["daily_late_fee"] * it["days_overdue"] * it["quantity"]
        lines.append(
            f"{it['book']['title']} x{it['quantity']} {it['days_overdue']}d @ {it['book']['daily_late_fee']:.2f}/day = {item_total:.2f}"
        )
    subtotal = loan_subtotal(loan)
    lines.append("-" * 30)
    lines.append(f"Subtotal fees: {subtotal:.2f}")
    lines.append(f"Reduction: -{reduction_amount:.2f}")
    lines.append(f"Total due: {subtotal - reduction_amount:.2f}")
    return "\n".join(lines)


# Reductions (OCP): higher-order functions returning strategies
def no_reduction():
    def calc(loan: dict) -> float:
        return 0.0
    return calc


def percentage_reduction(percent: float):
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")

    def calc(loan: dict) -> float:
        return loan_subtotal(loan) * (percent / 100.0)
    return calc


def bulk_item_reduction(min_total_items: int, reduction_amount: float):
    def calc(loan: dict) -> float:
        total_items = sum(it["quantity"] for it in loan["items"])
        if total_items >= min_total_items:
            return min(reduction_amount, loan_subtotal(loan))
        return 0.0
    return calc


# Payments (DIP): inject a charge function
def fake_charge(amount: float):
    if amount <= 0:
        return False, "Amount must be > 0"
    return True, f"Charged {amount:.2f} successfully (fake)."


# Application service (SRP + DIP): process fine using injected strategy and charger
def process_fine(loan: dict, reduction_fn, charge_fn) -> str:
    subtotal = loan_subtotal(loan)
    reduction_amount = float(reduction_fn(loan))
    total = max(subtotal - reduction_amount, 0.0)

    ok, msg = charge_fn(total)
    if not ok:
        return f"Payment failed: {msg}"
    return generate_receipt(loan, reduction_amount)


def demo() -> None:
    # books
    b1 = create_book("b1", "Clean Code", 0.50)
    b2 = create_book("b2", "Design Patterns", 0.75)
    b3 = create_book("b3", "Refactoring", 1.50)

    # loan
    loan = new_loan()
    add_loan_item(loan, b1, days_overdue=3, quantity=2)  # 2 copies, 3 days overdue
    add_loan_item(loan, b2, days_overdue=1, quantity=1)
    add_loan_item(loan, b3, days_overdue=5, quantity=1)

    # choose reduction strategy (OCP)
    reduction = percentage_reduction(10)
    # reduction = no_reduction()
    # reduction = bulk_item_reduction(min_total_items=4, reduction_amount=2.0)

    # inject charge function (DIP)
    charge = fake_charge

    receipt = process_fine(loan, reduction_fn=reduction, charge_fn=charge)
    print(receipt)


if __name__ == "__main__":
    demo()
