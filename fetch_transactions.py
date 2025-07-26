import requests
import os
import time
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv

# Load the Covalent API key from .env
load_dotenv()
API_KEY = os.getenv("COVALENT_API_KEY")

# Setup retry logic
session = requests.Session()
retries = Retry(
    total=5,  # Retry up to 5 times
    backoff_factor=1,  # Wait 1s, then 2s, then 4s...
    status_forcelist=[429, 500, 502, 503, 504],
    raise_on_status=False
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("https://", adapter)

CHAIN_ID = "1"  # Ethereum Mainnet
BASE_URL = "https://api.covalenthq.com/v1"

# Read wallet addresses
df = pd.read_excel("Wallet id.xlsx")  # Replace with your actual filename if different
  # Or your CSV path
wallets = df["wallet_id"].tolist()

all_data = []

for i, address in enumerate(wallets):
    url = f"{BASE_URL}/{CHAIN_ID}/address/{address}/transactions_v2/?key={API_KEY}"

    try:
        response = session.get(url, timeout=15)  # Add timeout
        response.raise_for_status()  # Raise for HTTP errors
        data = response.json()
        txs = data["data"]["items"]
        print(f"[{i+1}/{len(wallets)}] Wallet {address} fetched. {len(txs)} txs.")
        
        for tx in txs:
            all_data.append({
                "wallet": address,
                "hash": tx["tx_hash"],
                "block_signed_at": tx["block_signed_at"],
                "value": tx["value"],
                "gas_spent": tx["gas_spent"],
                "to_address": tx["to_address"],
                "from_address": tx["from_address"],
                "successful": tx["successful"]
            })

        time.sleep(1.5)  # Delay to avoid rate limit

    except requests.exceptions.RequestException as e:
        print(f"[{i+1}/{len(wallets)}]  Error fetching {address}: {e}")
        continue

# Save result
pd.DataFrame(all_data).to_csv("all_transactions.csv", index=False)
print(" All wallet transactions fetched and saved to all_transactions.csv.")
