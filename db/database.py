import sqlite3

def create_or_update_tables():
  # Connect to the database
  # will move to docker container later
  conn = sqlite3.connect('db/stock_data.db')
  cursor = conn.cursor()

  # Create raw data table if not exists
  cursor.execute('''CREATE TABLE IF NOT EXISTS raw_stock_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT,
                    date TEXT,
                    open REAL,
                    high REAL,
                    low REAL,
                    close REAL,
                    volume INTEGER
                    )''')

  # Create processed data table if not exists
  cursor.execute('''CREATE TABLE IF NOT EXISTS processed_stock_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    symbol TEXT,
                    date TEXT,
                    close REAL
                    )''')

  conn.commit()
  cursor.close()


def save_raw_data(stock_symbol, raw_data):
  # will move to docker container later
  conn = sqlite3.connect('db/stock_data.db')
  cursor = conn.cursor()

  # Insert or replace raw data into the raw_data table
  for date, values in raw_data.items():
    cursor.execute('''INSERT OR REPLACE INTO raw_stock_data (symbol, date, open,    high, low, close, volume)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                      (stock_symbol, date, float(values['1. open']), float(values['2. high']), float(values['3. low']), float(values['4. close']), int(values['5. volume'])))

  conn.commit()
  cursor.close()


def fetch_raw_data():
  conn = sqlite3.connect('db/stock_data.db')
  cursor = conn.cursor()

  # Fetch data from the raw_stock_data table
  cursor.execute('''SELECT symbol, date, close FROM raw_stock_data
                    WHERE date = (SELECT MAX(date) FROM raw_stock_data)
                    ''')
  raw_data = cursor.fetchone()

  conn.commit()
  cursor.close()

  return raw_data


def save_processed_data(processed_data):
  # will move to docker container later
  conn = sqlite3.connect('db/stock_data.db')
  cursor = conn.cursor()

  symbol = processed_data['symbol']
  date = processed_data['date']
  close = processed_data['close']

  cursor.execute('''
                  INSERT INTO processed_stock_data (symbol,date,close)
                  VALUES (?, ?, ?)
                  ''', (symbol, date, close))

  conn.commit()
  cursor.close()
