import pandas as pd

# Data
data = {
    "category": ["rent", "food", "utilities", "transport"],
    "amount": [15000, 8000, 2000, 3000]
}

df = pd.DataFrame(data)

# Compute total, average, max, min in one command
summary = df["amount"].agg(["sum", "mean", "max", "min"])

print("Expense Summary:")
print(summary)
