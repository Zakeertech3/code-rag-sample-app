from datetime import date
from models import Expense
from storage import ExpenseStore
from categorizer import categorize_all
from reports import total_spent, totals_by_category, monthly_total, top_category


def build_sample_store() -> ExpenseStore:
    expenses = [
        Expense(450.0, "grocery shopping", date(2026, 1, 5)),
        Expense(120.0, "uber to office", date(2026, 1, 7)),
        Expense(60.0, "coffee with team", date(2026, 1, 9)),
        Expense(1200.0, "electricity bill", date(2026, 2, 1)),
        Expense(300.0, "netflix and movie", date(2026, 2, 14)),
    ]
    categorize_all(expenses)
    store = ExpenseStore()
    for expense in expenses:
        store.add(expense)
    return store


def main() -> None:
    store = build_sample_store()
    print("total spent:", total_spent(store))
    print("by category:", totals_by_category(store))
    print("january total:", monthly_total(store, 2026, 1))
    print("top category:", top_category(store))


if __name__ == "__main__":
    main()