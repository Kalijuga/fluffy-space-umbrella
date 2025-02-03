from datetime import datetime, timedelta
transactions = [
    {"type": "Sale", "amount": 1500, "date": "2025-01-29"},
    {"type": "Purchase", "amount": 500, "date": "2025-01-29"},
    {"type": "Sale", "amount": 420, "date": "2025-01-29"},
    {"type": "Purchase", "amount": 6969, "date": "2025-01-29"},
]

def sum_up(my_type):
    amount_values = [t["amount"] for t in transactions if t["type"] == my_type]
    return sum(amount_values)

def filter_transactions(key, value):
    return [t for t in transactions if t[key] == value]

yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")


yest_transactions = filter_transactions("date", yesterday)
num_yesterday = len(yest_transactions)


total_income = sum_up("Sale")
total_expenses = sum_up("Purchase")

print(f"Transactions yesterday: {num_yesterday}")
print(f"Total income: {total_income}")
print(f"Total expenses: {total_expenses}")

if total_income > total_expenses:
    print("You made money!")
else:
    print("You lost money!")