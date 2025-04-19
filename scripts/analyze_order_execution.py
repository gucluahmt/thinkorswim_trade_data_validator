import pandas as pd

# Read data
df = pd.read_csv("../data/order_execution_logs.csv")

# Basic Summary
print("\n🔹 Total Orders:", len(df))
print("🔹 Executed Orders:", len(df[df['status'] == 'Executed']))
print("🔹 Cancelled Orders:", len(df[df['status'] == 'Cancelled']))
print("🔹 Unique Symbols:", df['symbol'].nunique())
print("\n🔹 Orders by Type:")
print(df['order_type'].value_counts())

# Flag high-volume trades (quantity > 100)
df['high_volume_flag'] = df['quantity'].apply(lambda x: 'Yes' if x > 100 else 'No')

# Export flagged data (optional)
df.to_csv("../data/flagged_order_summary.csv", index=False)
