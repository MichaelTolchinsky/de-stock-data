import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import database as db

def process_data(raw_data):
  symbol, date, close = raw_data
  transformed_data = {'symbol': symbol, 'date': date, 'close': close}
  return transformed_data

if __name__ == "__main__":
  raw_data = db.fetch_raw_data()
  processed_data = process_data(raw_data)
  db.save_processed_data(processed_data)
