from src.exception import CustomException
import sys
import os
import pandas as pd
import numpy as np
from src.logger import logging
from dataclasses import dataclass
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.utils import save_obj


@dataclass
class DataTransformationConfig:
    preprocessor_path=os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.get_preprocessor_path=DataTransformationConfig()

    def get_preprocessor_obj(self):

        '''This function gives preprocessor object'''
        try:
            cat_cols=['holiday', 'weather_main', 'Weekday']
            num_cols=['hour', 'temp', 'clouds_all']

            num_pipeline=Pipeline(
            steps=[("imputer",SimpleImputer()), ("scalar",StandardScaler())] )

            cat_pipeline = Pipeline(
            steps=[("imputer",SimpleImputer(strategy="most_frequent")),
            ("encoder",OneHotEncoder(sparse_output=False,handle_unknown="ignore"))]
            )

            preprocessor=ColumnTransformer([("num_pipeline",num_pipeline,num_cols),
                            ("cat_pipeline",cat_pipeline,cat_cols)])
            logging.info("preprocessor obj has been created")
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)
    
    def InitiateDataTransformation(self,train_path,test_path):
        """ this function initiates data transformation and save preprocessor obj returns transform data"""
        try:
            logging.info("DataTransformation: reading the data")
            train_data=pd.read_csv(train_path)
            test_data=pd.read_csv(test_path)

            X_train,y_train=train_data.drop("traffic_volume",axis=1),train_data["traffic_volume"]
            
            X_test,y_test=test_data.drop("traffic_volume",axis=1),test_data["traffic_volume"]

            preprocessor=self.get_preprocessor_obj()

            X_train_arr=preprocessor.fit_transform(X_train)
            X_test_arr=preprocessor.transform(X_test)

            train_arr=np.c_[X_train_arr,np.array(y_train)]
            test_arr=np.c_[X_test_arr,np.array(y_test)]

            save_obj(file_path=self.get_preprocessor_path.preprocessor_path,obj=preprocessor)
            logging.info(f"preprocessor obj has been saved to {self.get_preprocessor_path.preprocessor_path}")

            return (train_arr,test_arr)
            
        except Exception as e:
            raise CustomException(e,sys)


