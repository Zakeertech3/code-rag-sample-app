from dataclasses import dataclass, field
from datetime import date


@dataclass
class Category:
    name: str
    keywords: list[str] = field(default_factory=list)


@dataclass
class Expense:
    amount: float
    description: str
    spent_on: date
    category: str = "uncategorized"

    def is_uncategorized(self) -> bool:
        return self.category == "uncategorized"