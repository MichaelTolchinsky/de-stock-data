import os
import sys
from typing import List
from psycopg2 import pool
# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.processed_stock_data import ProcessedStockData
from models.raw_stock_data import RawStockData

# Initialize the connection pool
connection_pool = pool.SimpleConnectionPool(
    minconn=1,
    maxconn=10,
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    dbname=os.getenv("POSTGRES_DB"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

# Get a connection from the connection pool.
def get_connection() -> None:
    return connection_pool.getconn()

# Release the connection back to the connection pool.
def release_connection(conn) -> None:
    connection_pool.putconn(conn)


def create_or_update_tables() -> None:
  # Connect to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Create raw data table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS raw_stock_data (
                    id SERIAL PRIMARY KEY,
                    symbol TEXT,
                    date DATE,
                    open NUMERIC,
                    high NUMERIC,
                    low NUMERIC,
                    close NUMERIC,
                    volume INTEGER
                    )''')

    # Create processed data table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS processed_stock_data (
                    id SERIAL PRIMARY KEY,
                    symbol TEXT,
                    date DATE,
                    close NUMERIC
                    )''')

    conn.commit()
    cursor.close()
    release_connection(conn)


def save_raw_data(stock_symbol: str, raw_data: List[RawStockData]) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    # Insert raw data into the raw_data table
    for date, values in raw_data.items():
        cursor.execute('''INSERT INTO raw_stock_data (symbol, date, open,    high, low, close, volume)
                  VALUES (%s, %s, %s, %s, %s, %s, %s)''',
                       (stock_symbol, date, float(values['1. open']), float(values['2. high']), float(values['3. low']), float(values['4. close']), int(values['5. volume'])))

    conn.commit()
    cursor.close()
    release_connection(conn)


def fetch_raw_data() -> RawStockData:
    conn = get_connection()
    cursor = conn.cursor()

    # Fetch data from the raw_stock_data table
    cursor.execute('''SELECT symbol, date, close FROM raw_stock_data
                    WHERE date = (SELECT MAX(date) FROM raw_stock_data)
                    ''')
    raw_data = cursor.fetchone()

    conn.commit()
    cursor.close()

    return raw_data


def save_processed_data(processed_data: List[ProcessedStockData]) -> None:
    conn = get_connection()
    cursor = conn.cursor()

    symbol = processed_data['symbol']
    date = processed_data['date']
    close = processed_data['close']

    cursor.execute('''
                  INSERT INTO processed_stock_data (symbol,date,close)
                  VALUES (%s, %s, %s)
                  ''', (symbol, date, close))

    conn.commit()
    cursor.close()
    release_connection(conn)
