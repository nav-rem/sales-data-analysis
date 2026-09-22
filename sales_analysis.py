import pandas as pd

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# -----------------------------
# Load and Inspect
# -----------------------------

print("First 5 rows:")
print(df.head())

print("\nTotal number of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())


# -----------------------------
# Filter, Slice, and Add
# -----------------------------

# Filter: units_sold > 50 and store_id == 3
filtered_df = df.loc[
    (df["units_sold"] > 50) & (df["store_id"] == 3)
]

# Keep required columns, while retaining units_sold
# because it is needed to calculate revenue_per_unit
filtered_df = filtered_df.loc[
    :, ["date", "product", "revenue", "units_sold"]
]

# Calculate revenue per unit
filtered_df["revenue_per_unit"] = (
    filtered_df["revenue"] / filtered_df["units_sold"]
)

# Sort by revenue_per_unit from highest to lowest
sorted_df = filtered_df.sort_values(
    by="revenue_per_unit",
    ascending=False
)

# Display top 10 rows
print("\nTop 10 rows:")
print(sorted_df.head(10))


# -----------------------------
# Group-by and Aggregate
# -----------------------------

store_summary = (
    df.groupby("store_id")
    .agg(
        total_units_sold=("units_sold", "sum"),
        average_revenue=("revenue", "mean")
    )
    .reset_index()
)

print("\nStore Summary:")
print(store_summary)


# -----------------------------
# Pivot Table
# -----------------------------

pivot_df = pd.pivot_table(
    df,
    index=None,
    columns="product",
    values="units_sold",
    aggfunc="sum"
)

print("\nPivot Table:")
print(pivot_df)