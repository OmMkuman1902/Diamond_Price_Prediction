import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_obj


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifact\model.pkl'
            preprocessor_path='artifact\preprocessor.pkl'
            model=load_obj(file_path=model_path)
            print({type(model)})
            preprocessor=load_obj(file_path=preprocessor_path)
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)

            return preds
        
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(self, carat:int, depth:int, table:int, x:int, y:int, z:int, cut:str, color:str, clarity:str):
        self.carat=carat
        self.depth=depth
        self.table=table
        self.x=x
        self.y=y
        self.z=z
        self.cut=cut
        self.clarity=clarity
        self.color=color

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "carat":[self.carat],
                "depth":[self.depth],
                "table":[self.table],
                "x":[self.x],
                "y":[self.y],
                "z":[self.z],
                "cut":[self.cut],
                "color":[self.color],
                "clarity":[self.clarity],
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)
        