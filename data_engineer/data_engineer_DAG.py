
import pandas as pd
import psycopg2 as db
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine

def get_data_from_postgresql():
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow'"
    conn = db.connect(conn_string)
    df = pd.read_sql("select * from table_fpg1", conn)
    df.to_csv('/opt/airflow/credit_customers.csv', index=False)

def cleaning_data():
    df = pd.read_csv('/opt/airflow/credit_customers.csv')
    df['class'] = df['class'].replace('good', '1')
    df['class'] = df['class'].replace('bad', '0')
    to_integer = ['age', 'duration', 'installment_commitment', 'residence_since', 'existing_credits', 'num_dependents', 'class']
    for i in to_integer:
        df[i] = df[i].astype(int)
    df = df.dropna()
    df = df.replace({',': '', r'\.\d+': ''}, regex=True)
    df.to_csv('/opt/airflow/Final_Project_G1_data_clean.csv', index=False)

def push ():
    # Memanggil fungsi cleaning_data untuk membersihkan dataframe
    df_cleaned = pd.read_csv('/opt/airflow/Final_Project_G1_data_clean.csv') # import csv clean
    # Database connection parameters
    db_params = {
        "user": "airflow",
        "password": "airflow",
        "host": "postgres",
        "port": "5434",
        "database": "airflow",
    }

    # Create an SQLAlchemy engine
    engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}/{db_params['database']}")
    table_name = "table_finalproject"
    # Push the DataFrame to PostgreSQL
    df_cleaned.to_sql(table_name, engine, if_exists="replace", index=False)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
}

with DAG('FP_Data_Pipeline_Group1',
         description='End-to-end Data Pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         start_date=datetime(2023, 10, 1),
         catchup=False) as dag:
    
    fetch_task = PythonOperator(
        task_id='get_data_from_postgresql',
        python_callable=get_data_from_postgresql)
    
    clean_task = PythonOperator(
        task_id='cleaning_data',
        python_callable=cleaning_data)
    
    push_task = PythonOperator(
        task_id = 'push_task',
        python_callable=push
    )
    
    fetch_task >> clean_task >> push_task
