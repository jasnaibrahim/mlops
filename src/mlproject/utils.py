import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("localhost")
user=os.getenv("root")
password=os.getenv("12345")
db=os.getenv("college")
def read_sql_data(self):
    logging.info("reading data from sql")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("connection established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)
