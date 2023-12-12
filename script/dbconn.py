import pandas.io.sql as sqlio
import pandas as pd
import psycopg2
from psycopg2 import sql
# from sqlalchemy import create_engine 

# Database connection using psycopg
def db_connection_psycopg():
    pgconn = psycopg2.connect(dbname="telecom", 
                              user='postgres',
                              password="0933624757",
                              host="localhost",
                              port="5432")
    return pgconn

# read function to the telecom data
def db_read_table_psycopg(pgconn, table_name):
    sql = f'SELECT * FROM {table_name}'
    df = sqlio.read_sql_query(sql,pgconn)
    return df


