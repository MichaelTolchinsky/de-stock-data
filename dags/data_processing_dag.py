from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from dags_common import default_args
import sys
import os
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from scripts.data_processing import process_and_save_data

# Data Processing DAG
processing_dag = DAG(
  dag_id='data_processing',
  default_args=default_args,
  start_date=datetime(2024,4,12),
  description='DAG for weekly data processing',
  schedule='0 12 * * 0',  # Run week day at 12 AM
)

aquisition_task = PythonOperator(
  task_id='fetch_and_save_processed_stock_data',
  python_callable=process_and_save_data,
  dag=processing_dag,
)

