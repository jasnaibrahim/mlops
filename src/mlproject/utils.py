import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd



def read_sql_data(self):
    logging.info("reading data from sql")
    try:
        df=pd.read_csv("artifacts/raw.csv")
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)
