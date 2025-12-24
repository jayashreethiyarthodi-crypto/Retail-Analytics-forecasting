import pandas as pd

# Load data
df = pd.read_csv("data/retail_sales_sample.csv")

# Basic info
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Total net sales
total_sales = df["net_sales"].sum()
print("Total Net Sales:", total_sales)

# Net sales by category
category_sales = df.groupby("category")["net_sales"].sum()
print("\nNet Sales by Category:")
print(category_sales)

# Top products by net sales
top_products = df.sort_values("net_sales", ascending=False).head(3)
print("\nTop 3 Products by Net Sales:")
print(top_products)

# Net sales by store
store_sales = df.groupby("store")["net_sales"].sum()
print("\nNet Sales by Store:")
print(store_sales)
