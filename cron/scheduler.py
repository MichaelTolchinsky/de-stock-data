from scripts.data_acquisition import fetch_and_save_stock_data
from scripts.data_processing import process_raw_data_and_save
import schedule
import time
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Schedule data acquisition task to run every day at 11 AM
schedule.every().day.at("11:00").do(fetch_and_save_stock_data)

# Schedule data processing task to run every Sunday at 11 AM
schedule.every().sunday.at("11:00").do(process_raw_data_and_save)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(60)  # Check for tasks every minute
