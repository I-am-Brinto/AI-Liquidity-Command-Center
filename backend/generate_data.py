import pandas as pd
import random
from datetime import datetime, timedelta

providers = ["bKash", "Nagad", "Rocket"]
types = ["cash_in", "cash_out"]

data = []

start_time = datetime.now()

for i in range(100):
    provider = random.choice(providers)
    transaction_type = random.choice(types)

    amount = random.randint(500, 10000)

    data.append({
        "transaction_id": i + 1,
        "provider": provider,
        "type": transaction_type,
        "amount": amount,
        "timestamp": start_time + timedelta(minutes=i)
    })

df = pd.DataFrame(data)

df.to_csv("../data/transactions.csv", index=False)

print("Synthetic transaction data created successfully")
print(df.head())
