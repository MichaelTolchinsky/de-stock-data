import os
import sys
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import database as db
from models.processed_stock_data import ProcessedStockData
from models.raw_stock_data import RawStockData


def process_data(raw_data: RawStockData) -> ProcessedStockData:
    symbol, date, close = raw_data
    transformed_data = {'symbol': symbol, 'date': date, 'close': close}
    return transformed_data


def process_and_save_data() -> None:
    raw_data = db.fetch_raw_data()
    processed_data = process_data(raw_data)
    db.save_processed_data(processed_data)

# if __name__ == "__main__": only use for manual testing
#   process_and_save_data()