import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/macos/Downloads/sales_data.csv', parse_dates=['Date'])
print(df.head())
# Monthly revenue
monthly = df.groupby(pd.Grouper(key='Date', freq='M')).agg({'Revenue':'sum'}).reset_index()
plt.figure(figsize=(10,4))
plt.plot(monthly['Date'], monthly['Revenue'])
plt.title('Monthly Revenue')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()
# Overall Summary Metrics
total_revenue = df['Revenue'].sum()
total_profit = df['Profit'].sum()
total_orders = df['OrderID'].nunique()
total_units = df['Units'].sum()
avg_order_value = df['Revenue'].mean()
avg_profit_margin = (df['Profit'].sum() / df['Revenue'].sum()) * 100

print("=== Overall Sales Summary ===")
print(f"Total Orders: {total_orders}")
print(f"Total Units Sold: {total_units}")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Profit: ₹{total_profit:,.2f}")
print(f"Average Order Value (AOV): ₹{avg_order_value:,.2f}")
print(f"Average Profit Margin: {avg_profit_margin:.2f}%")
# Category-wise Summary
category_summary = df.groupby('Category').agg({
    'Revenue': 'sum',
    'Profit': 'sum',
    'Units': 'sum'
}).sort_values(by='Revenue', ascending=False)

print("\n=== Category-wise Summary ===")
print(category_summary)
# Region-wise Summary
region_summary = df.groupby('Region').agg({
    'Revenue': 'sum',
    'Profit': 'sum',
    'OrderID': 'count'
}).rename(columns={'OrderID': 'Orders'}).sort_values(by='Revenue', ascending=False)

print("\n=== Region-wise Summary ===")
print(region_summary)
# Top 5 Performing Sales Reps
top_reps = df.groupby('SalesRep').agg({
    'Revenue': 'sum',
    'Profit': 'sum'
}).sort_values(by='Revenue', ascending=False).head(5)

print("\n=== Top 5 Sales Representatives ===")
print(top_reps)
# Visualization (matplotlib)
import matplotlib.pyplot as plt

category_summary['Revenue'].plot(kind='bar', figsize=(8,4), title='Revenue by Category')
plt.ylabel('Revenue (₹)')
plt.show()