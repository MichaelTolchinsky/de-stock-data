from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from dags_common import default_args
import os
import sys
# Add the parent directory of the scripts package to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scripts import data_processing as ds

# Data Processing DAG
processing_dag = DAG(
  dag_id='data_processing',
  default_args=default_args,
  start_date=datetime(2024,4,12),
  description='DAG for weekly data processing',
  schedule_interval='0 12 * * 0',  # Run week day at 12 AM
  #schedule_interval=None
)

processing_task = PythonOperator(
  task_id='process_and_save_data',
  python_callable=ds.process_and_save_data,
  dag=processing_dag,
)