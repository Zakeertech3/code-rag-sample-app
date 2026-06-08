from collections import defaultdict
from models import Expense
from storage import ExpenseStore


def total_spent(store: ExpenseStore) -> float:
    return sum(e.amount for e in store.all())


def totals_by_category(store: ExpenseStore) -> dict[str, float]:
    totals: dict[str, float] = defaultdict(float)
    for expense in store.all():
        totals[expense.category] += expense.amount
    return dict(totals)


def monthly_total(store: ExpenseStore, year: int, month: int) -> float:
    return sum(e.amount for e in store.by_month(year, month))


def top_category(store: ExpenseStore) -> str:
    totals = totals_by_category(store)
    if not totals:
        return "none"
    return max(totals, key=totals.get)

def average_expense(store: ExpenseStore) -> float:
    expenses = store.all()
    if not expenses:
        return 0.0
    return total_spent(store) / len(expenses)
