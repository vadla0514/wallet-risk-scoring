import pandas as pd

COMPOUND_V2_ADDRESS = "0x3d9819210a31b4961b30ef54be2aed79b9c9cd3b".lower()

# Load the complete transaction dataset
df = pd.read_csv("all_transactions.csv")

# Standardize to_address to lowercase
df["to_address"] = df["to_address"].str.lower()

# Filter only Compound transactions
compound_df = df[df["to_address"] == COMPOUND_V2_ADDRESS]

# Save
compound_df.to_csv("compound_transactions.csv", index=False)
print(" Compound-only transactions saved to compound_transactions.csv")
