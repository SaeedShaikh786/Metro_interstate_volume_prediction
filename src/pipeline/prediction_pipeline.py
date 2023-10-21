import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from src.utils import load_obj


class PredictionPipeline:

    def __init__(self):
        self.model_path=os.path.join("artifacts","model.pkl")
        self.preprocessor_path=os.path.join("artifacts","preprocessor.pkl")

    def predict(self,data):
        try:
            model=load_obj(file_path=self.model_path)
            logging.info("PredictionPipeline : model is loaded ")

            preprocessor=load_obj(file_path=self.preprocessor_path)
            logging.info("PredictionPipeline : preprocessor is loaded ")

            data_arr=preprocessor.transform(data)

            pred=model.predict(data_arr)

            return pred
        except Exception as e:
            raise CustomException(e,sys)


class CustomeData:
    def __init__(self,holiday,temp,clouds_all,weather_main,hour,weekday):

        self.holiday=holiday
        self.temp=temp
        self.clouds_all=clouds_all
        self.weather_main=weather_main
        self.hour=hour
        self.weekday=weekday
    
    def get_data_as_dataframe(self):
        try:

            data={"holiday":[self.holiday],"temp":[self.temp],
            "clouds_all":[self.clouds_all],"weather_main":[self.weather_main],
            "hour":[self.hour],"Weekday":[self.weekday]}

            df=pd.DataFrame(data)
            logging.info("Dataset has been read from user")

            return df
        except Exception as e:
            raise CustomException(e,sys)

