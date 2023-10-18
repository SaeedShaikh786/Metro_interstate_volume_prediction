from src.logger import logging
from src.exception import CustomException
import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
# from src.components.data_transformation import DataTransformation
# from src.components.model_trainer import ModelTrainer
@dataclass
class DataingestionConfig:
    raw_data_path=os.path.join("artifacts","raw.csv")
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def InitiateDataIngestion(self):
        try:
            logging.info("Data ingestion has started")
            data=pd.read_csv("Notebooks/data/metro.csv")
            logging.info("Splitting the data")
            train_set,test_set=train_test_split(data,test_size=0.30,random_state=42)

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            data.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info(f"Data has saved to {self.ingestion_config.raw_data_path}")

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)
            

        except Exception as e:
            raise CustomException(e,sys)


