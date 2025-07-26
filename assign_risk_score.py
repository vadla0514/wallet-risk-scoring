import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load wallet features
df = pd.read_csv("wallet_features.csv")

# Define features to be used for scoring
features = ["num_transactions", "total_gas_spent", "success_rate"]

# Normalize features
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[features] = scaler.fit_transform(df[features])

# Compute risk score (weighted sum)
# You can tune weights as per your domain logic
df_scaled["risk_score"] = (
    0.4 * df_scaled["num_transactions"] +
    0.2 * (1 - df_scaled["total_gas_spent"]) +  # Less gas = better
    0.4 * df_scaled["success_rate"]
) * 1000

# Round the score
df_scaled["risk_score"] = df_scaled["risk_score"].round().astype(int)

# Save results
df_scaled[["wallet", "risk_score"]].to_csv("wallet_risk_scores.csv", index=False)
print(" Risk scores saved to wallet_risk_scores.csv")
