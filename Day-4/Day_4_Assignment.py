import pandas as pd

# Data
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
litres = [10, 12, 9, 11, 13, 8, 14]

# Create DataFrame
df = pd.DataFrame({"day": days, "litres": litres})

# Display first 3 rows
print("First 3 rows:")
print(df.head(3))

# Shape, Columns, Dtypes
print("\nShape:", df.shape)
print("Columns:", df.columns.tolist())
print("Data types:\n", df.dtypes)
