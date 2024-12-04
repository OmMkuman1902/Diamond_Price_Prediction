# Basic Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
# Modelling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from xgboost import XGBRegressor
import warnings
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_obj
from dataclasses import dataclass
from src.utils import evaluate_model


@dataclass
class ModelTrainerConfig():
    trained_model_file_path=os.path.join('artifact','model.pkl')

class Model_trainer():
    def __init__(self):
        self.Model_trainer_config=ModelTrainerConfig()

    def initiate_model_trainer(self,train_arr,test_arr):
        try:
            logging.info("spliting traing and testinput data")
            Xtrain,ytrain,Xtest,ytest=(
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]
            )

            models={
                    "Linear Regression": LinearRegression(),
                    "Lasso": Lasso(),
                    "Ridge": Ridge(),
                    "K-Neighbors Regressor": KNeighborsRegressor(),
                    "Decision Tree": DecisionTreeRegressor(),
                    "Random Forest Regressor": RandomForestRegressor(),
                    "XGBRegressor": XGBRegressor(), 
                    "AdaBoost Regressor": AdaBoostRegressor()
                    }
            
            model_report :dict=evaluate_model(Xtrain=Xtrain,ytrain=ytrain,Xtest=Xtest,ytest=ytest,models=models)
            logging.info("evaluate model called and returned the model report")


            best_model_acc=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_acc)]

            logging.info("best model with accuracy found")

            save_obj(
                file_path=self.Model_trainer_config.trained_model_file_path,
                obj=best_model_name
            )

            return(
                best_model_name,
                best_model_acc
            )


            
            
        except  Exception as e:
            raise CustomException(e,sys)


