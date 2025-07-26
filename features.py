import pandas as pd

# Load the cleaned Compound transactions CSV
df = pd.read_csv("compound_transactions.csv")

# Feature Engineering
features = df.groupby("wallet").agg(
    num_transactions=("hash", "count"),
    total_gas_spent=("gas_spent", "sum"),
    avg_transaction_value=("value", "mean"),
    total_transaction_value=("value", "sum"),
    success_rate=("successful", "mean")
).reset_index()

# Normalize success_rate to a percentage
features["success_rate"] = features["success_rate"] * 100

# Save the features
features.to_csv("wallet_features.csv", index=False)
print(" Wallet features saved to wallet_features.csv")
