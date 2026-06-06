from models import Category, Expense


DEFAULT_CATEGORIES = [
    Category("food", ["restaurant", "grocery", "cafe", "coffee", "lunch"]),
    Category("transport", ["uber", "fuel", "petrol", "metro", "taxi"]),
    Category("utilities", ["electricity", "water", "internet", "phone"]),
    Category("entertainment", ["movie", "netflix", "game", "concert"]),
]


def categorize(expense: Expense, categories: list[Category] = DEFAULT_CATEGORIES) -> str:
    text = expense.description.lower()
    for category in categories:
        if any(keyword in text for keyword in category.keywords):
            return category.name
    return "uncategorized"


def categorize_all(expenses: list[Expense], categories: list[Category] = DEFAULT_CATEGORIES) -> list[Expense]:
    for expense in expenses:
        expense.category = categorize(expense, categories)
    return expenses