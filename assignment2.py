import pandas as pd

# 1. Create a sample sales.csv file for testing
data = {
    "date": [
        "2026-01-15",
        "2026-01-20",
        "2026-02-05",
        "2026-02-12",
        "2026-03-01",
    ],
    "store_id": ["S001", "S002", "S001", "S003", "S002"],
    "product_id": ["P101", "P102", "P103", "P101", "P104"],
    "units_sold": [10, 5, 8, 12, 3],
    "unit_price": [15.0, 50.0, 25.0, 15.0, 120.0],
    "category": [
        "Electronics",
        "Home & Kitchen",
        "Electronics",
        "Electronics",
        "Home & Kitchen",
    ],
}
df_sample = pd.DataFrame(data)
df_sample.to_csv("sales.csv", index=False)


# 2. Define the required functions
def load_sales(path: str) -> pd.DataFrame:
  df = pd.read_csv(path, parse_dates=["date"])
  df.set_index("date", inplace=True)
  return df


def total_revenue(df: pd.DataFrame) -> pd.Series:
  df_temp = df.copy()
  df_temp["revenue"] = df_temp["units_sold"] * df_temp["unit_price"]
  return df_temp.groupby("store_id")["revenue"].sum()


def category_pivot(df: pd.DataFrame) -> pd.DataFrame:
  df_temp = df.copy()
  if not isinstance(df_temp.index, pd.DatetimeIndex):
    df_temp.index = pd.to_datetime(df_temp.index)

  df_temp["month"] = df_temp.index.to_period("M")

  pivot_df = pd.pivot_table(
      df_temp,
      values="units_sold",
      index="category",
      columns="month",
      aggfunc="sum",
      fill_value=0,
  )
  return pivot_df


# 3. Execute and test the functions
if __name__ == "__main__":
  # Load the data
  sales_df = load_sales("sales.csv")
  print("--- Loaded DataFrame Preview ---")
  print(sales_df.head())
  print("\n" + "=" * 40 + "\n")

  # Test total_revenue
  revenue_series = total_revenue(sales_df)
  print("--- Total Revenue by Store ---")
  print(revenue_series)
  print("\n" + "=" * 40 + "\n")

  # Test category_pivot
  pivot_table = category_pivot(sales_df)
  print("--- Category Pivot Table (Units Sold by Month) ---")
  print(pivot_table)