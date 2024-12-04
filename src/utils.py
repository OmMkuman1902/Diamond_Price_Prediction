import os,sys
import dill
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from dotenv import load_dotenv
import pymysql

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("reading SQL database")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,db=db)
        logging.info("connection established")

        df=pd.read_sql_query("select * from diamonds",mydb)
        print(df.head())

        return df
    except Exception as e:
        raise CustomException(e,sys)


def save_obj(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(Xtrain,ytrain,Xtest,ytest,models):
    try:
        def evaluate_model(true, predicted):
                mae = mean_absolute_error(true, predicted)
                mse = mean_squared_error(true, predicted)
                rmse = np.sqrt(mean_squared_error(true, predicted))
                r2_square = r2_score(true, predicted)
                return mae, rmse, r2_square
        model_list = []
        r2_list =[]
        r2_dict={}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            model.fit(Xtrain, ytrain) # Train model

            # Make predictions
            y_train_pred = model.predict(Xtrain)
            y_test_pred = model.predict(Xtest)
            
            # Evaluate Train and Test dataset
            model_train_mae , model_train_rmse, model_train_r2 = evaluate_model(ytrain, y_train_pred)

            model_test_mae , model_test_rmse, model_test_r2 = evaluate_model(ytest, y_test_pred)

            
            print(list(models.keys())[i])
            model_list.append(list(models.keys())[i])
            
            print('Model performance for Training set')
            print("- Root Mean Squared Error: {:.4f}".format(model_train_rmse))
            print("- Mean Absolute Error: {:.4f}".format(model_train_mae))
            print("- R2 Score: {:.4f}".format(model_train_r2))

            print('----------------------------------')
            
            print('Model performance for Test set')
            print("- Root Mean Squared Error: {:.4f}".format(model_test_rmse))
            print("- Mean Absolute Error: {:.4f}".format(model_test_mae))
            print("- R2 Score: {:.4f}".format(model_test_r2))
            r2_list.append(model_test_r2)
            
            print('='*35)
            print('\n')
            
            for i in range(len(model_list)):
                r2_dict.update({model_list[i]:r2_list[i]}) 

        return r2_dict
    except:
        pass