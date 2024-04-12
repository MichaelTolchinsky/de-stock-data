from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from dags_common import default_args
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from scripts.data_acquisition import fetch_and_save_raw_stock_data

# Data Acquisition DAG
acquisition_dag = DAG(
  dag_id='data_acquisition',
  default_args=default_args,
  start_date=datetime(2024,4,12),
  description='DAG for daily raw stock data acquisition',
  schedule='0 11 * * *',  # Run every day at 11 AM
)

aquisition_task = PythonOperator(
  task_id='fetch_and_save_raw_stock_data',
  python_callable=fetch_and_save_raw_stock_data,
  dag=acquisition_dag,
)

