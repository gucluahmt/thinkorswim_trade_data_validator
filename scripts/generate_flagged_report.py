import pandas as pd

df = pd.read_csv('../data/order_execution_logs.csv')

# Anomaly conditions
condition_1 = (df['quantity'] > 1000) & (df['status'] == 'Pending')
condition_2 = (df['price'] > 1800) & (df['status'] == 'Cancelled')

# Combine all anomalies
flagged_df = df[condition_1 | condition_2].copy()
flagged_df['anomaly_reason'] = ''

flagged_df.loc[condition_1, 'anomaly_reason'] = 'High Quantity - Still Pending'
flagged_df.loc[condition_2, 'anomaly_reason'] = 'High Price - But Cancelled'

# Save flagged entries
flagged_df.to_csv('../data/flagged_order_summary.csv', index=False)

print(f"🚩 Flagged report generated. Entries: {len(flagged_df)}")

