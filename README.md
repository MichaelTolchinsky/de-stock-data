# Stock Data Pipeline

This repository contains a Python-based stock data pipeline that retrieves, processes, and analyzes stock market data. The pipeline is designed to automate the acquisition of stock data from an external source, store it in a database, process the data to derive insights, and perform analytics tasks.

## Features:

- **Data Acquisition:** Fetches the latest stock market data from an external API (e.g., Alpha Vantage) using Python scripts.
- **Data Storage:** Stores the acquired stock data in a SQLite database for efficient data retrieval and management. (will move to postgres/mongo container)
- **Data Processing:** Processes the raw stock data to perform various transformations, calculations, and analytics.
- **Automated Workflow:** Utilizes Apache Airflow for task scheduling and orchestration.

## Dependencies:

- Python 3.x
- Requests library for HTTP requests
- SQLite database for data storage (will move to postgres/mongo container)
- Apache Airflow for task scheduling and orchestration
