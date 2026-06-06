import json
from datetime import date
from models import Expense


class ExpenseStore:
    def __init__(self):
        self._expenses: list[Expense] = []

    def add(self, expense: Expense) -> None:
        self._expenses.append(expense)

    def all(self) -> list[Expense]:
        return list(self._expenses)

    def by_category(self, category: str) -> list[Expense]:
        return [e for e in self._expenses if e.category == category]

    def by_month(self, year: int, month: int) -> list[Expense]:
        return [e for e in self._expenses if e.spent_on.year == year and e.spent_on.month == month]

    def to_json(self) -> str:
        data = [
            {"amount": e.amount, "description": e.description, "spent_on": e.spent_on.isoformat(), "category": e.category}
            for e in self._expenses
        ]
        return json.dumps(data, indent=2)

    def load_json(self, raw: str) -> None:
        for item in json.loads(raw):
            self.add(Expense(item["amount"], item["description"], date.fromisoformat(item["spent_on"]), item["category"]))