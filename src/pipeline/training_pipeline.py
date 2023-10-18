import sys
from src.exception import CustomException
from src.components.model_trainer import ModelTrainer

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

if __name__=="__main__":
    
    try:
        obj=DataIngestion()
        train_path,test_path=obj.InitiateDataIngestion()
        tf_obj=DataTransformation()
        train_arr,test_arr=tf_obj.InitiateDataTransformation(train_path=train_path,test_path=test_path)
        model_obj=ModelTrainer()
        model_obj.InitiateModeltraining(train_arr=train_arr,test_arr=test_arr)
    except Exception as e:
        raise CustomException(e,sys)