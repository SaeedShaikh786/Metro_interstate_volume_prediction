import sys
import os
from src.exception import CustomException
import pickle

from sklearn.metrics import r2_score
def save_obj(file_path,obj):
    """ This function is used to save the object..object may be preprocessing or model.pkl """
    try :
        dir_name=os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as f:
            pickle.dump(file=f,obj=obj)
            
    except Exception as e:
        raise CustomException(e,sys)


def Evaluate_models(models,X_train,y_train,X_test,y_test):
    Report={}
    try:

        for i in range(len(models)):
        
            model_name=list(models.keys())[i]
            model=models[model_name]
            n=len(y_test)
            model.fit(X_train,y_train)
            y_pred=model.predict(X_test)
            r2=r2_score(y_true=y_test,y_pred=y_pred)
            #adj_r_squared = 1 - (1 - r2) * (n - 1) / (n - X_train.shape[1] - 1)
        
            Report[model_name]=r2
        
        return Report
    except Exception as e:
        raise CustomException(e,sys)