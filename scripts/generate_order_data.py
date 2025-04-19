import pandas as pd
import random

symbols = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'NVDA']
order_types = ['Market', 'Limit', 'Stop']
statuses = ['Executed', 'Cancelled', 'Pending']
data = []

for _ in range(1200):
    row = {
        'order_id': random.randint(100000, 999999),
        'symbol': random.choice(symbols),
        'order_type': random.choice(order_types),
        'quantity': random.randint(10, 500),
        'price': round(random.uniform(100, 2000), 2),
        'status': random.choice(statuses)
    }
    data.append(row)

df = pd.DataFrame(data)
df.to_csv('../data/order_execution_logs.csv', index=False)
print("✅ Large dataset created successfully.")
