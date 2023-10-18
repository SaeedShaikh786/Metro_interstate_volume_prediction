import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import Evaluate_models,save_obj
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor,AdaBoostRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from dataclasses import dataclass
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
import mlflow
from urllib.parse import urlparse
from mlflow.models import infer_signature
import mlflow.sklearn

@dataclass
class ModelTrainerConfig:
    model_trainer_path=os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_path=ModelTrainerConfig()

    def Metrics(self,y_test,y_pred):
        try:
            r2=r2_score(y_pred=y_pred,y_true=y_test)
            mae=mean_absolute_error(y_pred=y_pred, y_true = y_test)
            mse=mean_squared_error(y_pred=y_pred, y_true = y_test)

            return r2,mae,mse
        except Exception as e:
            raise CustomException(e,sys)

    def InitiateModeltraining(self,train_arr,test_arr):
        try:
            logging.info("Model training has started")
            models={
            "GradientBoostingRegressor":GradientBoostingRegressor(),
            "AdaBoostRegressor":AdaBoostRegressor(),"KNN-regressor":KNeighborsRegressor()}
            logging.info("Model training has started")
            X_train,y_train=train_arr[:,:-1],train_arr[:,-1]
            X_test,y_test=test_arr[:,:-1],test_arr[:,-1]
            
            Report=Evaluate_models(models,X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)
            logging.info("------")
            best_model_score = max(sorted(Report.values()))
            logging.info(f"best model score {best_model_score}")
            best_model_name=[key for key ,value in Report.items() if value==best_model_score][0]

            print(f"bestmodel is {best_model_name}")
            logging.info(f"best model found is {best_model_name}")
            best_model=models[best_model_name]
            save_obj(file_path=self.model_path.model_trainer_path,obj=best_model)
            logging.info(f"model saved to {self.model_path.model_trainer_path}")

            #params={"n_estimators":150,"criterion":"friedman_mse","max_features":"log2"}

            with mlflow.start_run():
                prediction=best_model.predict(X_test)


                r2,mae,mse=self.Metrics(y_pred=prediction,y_test=y_test)
                logging.info(f"r2:{r2} ,mae:{mae}")

                print(f"R2 score {r2}")
                print(f"MAE : {mae}")
                print(f"MSE : {mse}")

                #mlflow.log_params(params)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("mse",mse)

                predictions = best_model.predict(X_train)
                
                signature = infer_signature(X_train, predictions)
                ## For Remote server only(DAGShub)

                #remote_server_uri="https://dagshub.com/krishnaik06/mlflowexperiments.mlflow"
                #mlflow.set_tracking_uri(remote_server_uri)

                tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

                # Model registry does not work with file store
                if tracking_url_type_store != "file":

            # Register the model
            # There are other ways to use the Model Registry, which depends on the use case,
            # please refer to the doc for more information:
            # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(best_model ,"model", registered_model_name=f"{best_model_name}",signature=signature) 
                else:

                    mlflow.sklearn.log_model(best_model,"Model")
            
            #Params={"n_estimators":150,"criterion":"friedman_mse","max_features":"log2","oob_score":True}
            #B_model=RandomForestRegressor(Params)

            #save_obj()                             
        except Exception as e:

            raise CustomException(e,sys)
    

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
