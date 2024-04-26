import requests
import os
import sys
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import database as db
from models.raw_stock_data import RawStockData

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = os.getenv("ALPHA_VANTAGE_BASE_URL")
FUNCTION = 'Time_Series_Daily'
SYMBOL = "NVDA"  # stock of your choise


def fetch_stock_data() -> None:
    params = {
        "function": FUNCTION,
        "symbol": SYMBOL,
        "apikey": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()['Time Series (Daily)']
        # Extract data and create list of DailyStockData objects
        raw_stock_data_list = []
        for date, values in data:
            raw_data = RawStockData(date=date,
                                    open=float(values['open']),
                                    high=float(values['high']),
                                    low=float(values['float']),
                                    close=float(values['close']),
                                    volume=int(values['volume']))
            raw_stock_data_list.append(raw_data)
        return raw_stock_data_list
    else:
        print("Failed to fetch data", response.status_code)


def fetch_and_save_raw_stock_data() -> None:
    db.create_or_update_tables()
    raw_data = fetch_stock_data()
    db.save_raw_data(SYMBOL, raw_data)


# if __name__ == "__main__":  # only use for manual testing
#     fetch_and_save_raw_stock_data()
