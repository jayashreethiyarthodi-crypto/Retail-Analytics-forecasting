import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/retail_sales_sample.csv", parse_dates=["date"])

# Sort by date
df = df.sort_values("date")

# Prepare data for regression
df["time_index"] = np.arange(len(df))

X = df[["time_index"]]
y = df["net_sales"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Forecast next 3 months
future_periods = 3
future_index = np.arange(len(df), len(df) + future_periods).reshape(-1, 1)
forecast = model.predict(future_index)

# Create forecast dataframe
forecast_df = pd.DataFrame({
    "month_ahead": [1, 2, 3],
    "forecasted_net_sales": forecast
})

print("Forecasted Sales:")
print(forecast_df)

# Plot results
plt.plot(df["date"], y, label="Historical Sales")
plt.plot(
    pd.date_range(df["date"].max(), periods=future_periods + 1, freq="M")[1:],
    forecast,
    linestyle="--",
    label="Forecast"
)
plt.xlabel("Date")
plt.ylabel("Net Sales")
plt.title("Retail Sales Forecast")
plt.legend()
plt.show()
