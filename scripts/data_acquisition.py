from dotenv import load_dotenv
from db import database as db
import requests
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

load_dotenv()
API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
BASE_URL = os.environ.get("ALPHA_VANTAGE_BASE_URL")
FUNCTION = os.environ.get("ALPHA_VANTAGE_FUNCTION")
SYMBOL = "NVDA"  # stock of your choise


def fetch_stock_data():
  params = {
    "function": FUNCTION,
    "symbol": SYMBOL,
    "apikey": API_KEY,
  }

  response = requests.get(BASE_URL, params=params)
  if response.status_code == 200:
    return response.json()['Time Series (Daily)']
  else:
    print("Failed to fetch data", response.status_code)


if __name__ == "__main__":
  db.create_or_update_tables()
  raw_data = fetch_stock_data()
  db.save_raw_data(SYMBOL, raw_data)
