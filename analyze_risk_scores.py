import pandas as pd
import matplotlib.pyplot as plt

# Load risk score data
df = pd.read_csv("wallet_risk_scores.csv")

# Basic statistics
print("Risk Score Summary Statistics:")
print(df['risk_score'].describe())

# Define risk categories
def categorize(score):
    if score <= 300:
        return "Low Risk"
    elif score <= 700:
        return "Medium Risk"
    else:
        return "High Risk"

# Apply categorization
df['risk_level'] = df['risk_score'].apply(categorize)

# Count per category
risk_counts = df['risk_level'].value_counts()
print("\nRisk Category Counts:")
print(risk_counts)

# Percentage breakdown
risk_percentages = risk_counts / len(df) * 100
print("\nRisk Category Percentages:")
print(risk_percentages.round(2))

# Plotting histogram
plt.figure(figsize=(10, 6))
plt.hist(df['risk_score'], bins=20, color='steelblue', edgecolor='black')
plt.title("Distribution of Wallet Risk Scores")
plt.xlabel("Risk Score")
plt.ylabel("Number of Wallets")
plt.grid(True)
plt.savefig("risk_score_histogram.png")  # Save to file
plt.show()

# Plotting pie chart
plt.figure(figsize=(7, 7))
plt.pie(risk_counts, labels=risk_counts.index, autopct='%1.1f%%', startangle=140, colors=['green', 'orange', 'red'])
plt.title("Wallet Risk Level Distribution")
plt.savefig("risk_score_pie_chart.png")  # Save to file
plt.show()
