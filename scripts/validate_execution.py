import pandas as pd

# Load dataset
df = pd.read_csv('../data/order_execution_logs.csv')

# Check for inconsistencies: Quantity zero with status Executed
invalid_executions = df[(df['status'] == 'Executed') & (df['quantity'] == 0)]

# Check for unrecognized status values
valid_statuses = ['Executed', 'Cancelled', 'Pending']
invalid_statuses = df[~df['status'].isin(valid_statuses)]

# Save results
invalid_executions.to_csv('../data/invalid_quantity_executions.csv', index=False)
invalid_statuses.to_csv('../data/invalid_status_entries.csv', index=False)

print("✅ Execution validation completed.")
print(f"- Invalid quantity executions: {len(invalid_executions)}")
print(f"- Invalid status entries: {len(invalid_statuses)}")
