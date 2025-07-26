##  Wallet Risk Scoring

This project performs **risk scoring of DeFi wallet addresses** using transaction data from the Compound V2 protocol. It analyzes wallet behaviors and generates risk scores on a scale from 0 to 1000, then visualizes and categorizes these scores for interpretation.

---

##  Project Structure

wallet_risk_scoring/
│

├── fetch_transactions.py # Fetches Compound transactions for wallet list

├── extract_features.py # Derives wallet behavior features

├── risk_scoring_model.py # Assigns risk scores to wallets

├── analyze_risk_scores.py # Performs analysis & visualization of scores

│
├── wallet_list.txt # Input list of wallet addresses

├── compound_transactions.csv # Raw on-chain transaction data

├── wallet_features.csv # Engineered wallet features

├── wallet_risk_scores.csv # Final wallet risk scores

│
├── risk_score_histogram.png # Histogram of score distribution

├── risk_score_pie_chart.png # Pie chart of risk category breakdown

│
├── .env # (Not committed) contains private API key

└── .gitignore # Hides .env and Python cache

### 1. **Fetch Wallet Transactions**

We use Compound V2 APIs to pull transaction histories for a list of wallet addresses:

`bash
python fetch_transactions.py

## Feature Extraction

We engineer key features from the raw data such as:

Total borrow count

Total repay count

Active days

Transaction frequency

Net balance movement

Borrow-to-repay ratio

## Risk Scoring

Each wallet is assigned a risk score between 0 and 1000 using simple heuristics:

Low activity or high borrow/low repay: → low score (higher risk)

Balanced, healthy behavior: → high score (lower risk)

## Tools & Libraries Used

pandas – for data manipulation

matplotlib – for plotting

python-dotenv – to manage API keys securely

Compound API – to fetch DeFi transaction data

Scikit-learn 

## Future Work

Use real credit scoring models (e.g., logistic regression)

Pull data from multiple DeFi protocols (Aave, Uniswap, etc.)

Deploy via Streamlit dashboard or API


