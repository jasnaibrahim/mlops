from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.Data_ingestion import DataIngestion
from src.mlproject.components.Data_ingestion import DataIngestionConfig

if  __name__ =="__main__":
    logging.info("the execution has started")

try:
    data_ingestion = DataIngestion()
    data_ingestion.initiate_dataingestion()

except Exception as e:
    logging.info("Custom Exception")
    raise CustomException(e,sys)