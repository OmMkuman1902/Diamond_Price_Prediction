from flask import Flask,render_template,request,jsonify
import numpy as np
import pandas as pd
from src.logger import logging
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

from sklearn.preprocessing import StandardScaler
application=Flask(__name__)
app=application


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata' ,methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        logging.info("custom data initiated")
        data=CustomData(
            cut=request.form.get('cut'),
            clarity=request.form.get('clarity'),
            color=request.form.get('color'),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
        )

        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        logging.info("dataframe converted")

        predict_pipeline=PredictPipeline()
        results=predict_pipeline.predict(pred_df)

        if results==None:
            print("null result")
        
        return render_template("home.html", result=results)


if __name__=="__main__":
    app.run(debug=True)