from db import database as db
from dotenv import load_dotenv
import requests
import os

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


def fetch_and_save_raw_stock_data():
    db.create_or_update_tables()
    raw_data = fetch_stock_data()
    db.save_raw_data(SYMBOL, raw_data)

# if __name__ == "__main__": only use for manual testing
#   fetch_and_save_raw_stock_data()
