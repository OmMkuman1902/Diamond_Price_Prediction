from flask import flask
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
application=Flask(__name__)
app=application


@app.route('/')
def index():
    return render