from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from dags_common import default_args
import os
import sys
# Add the parent directory of the scripts package to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts import data_acquisition as da

# Data Acquisition DAG
acquisition_dag = DAG(
    dag_id='data_acquisition',
    default_args=default_args,
    start_date=datetime(2024, 4, 12),
    description='DAG for daily raw stock data acquisition',
    schedule_interval='0 11 * * *',  # Run every day at 11 AM
)

aquisition_task = PythonOperator(
    task_id='fetch_and_save_raw_stock_data',
    python_callable=da.fetch_and_save_raw_stock_data,
    dag=acquisition_dag,
)
