
import pandas as pd

data = {
    "Product": ["Rice", "Sugar", "Oil"],
    "Price": [50, 40, 100]
}
df = pd.DataFrame(data)

# Display first row
first_row = df.head(1)
# Average price
avg_price = df["Price"].mean()

print("First row:")
print(first_row)
print("\nAverage Price:", avg_price)
