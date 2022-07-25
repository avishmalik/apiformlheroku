# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 12:29:17 2022

@author: Avish
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()

class model_input(BaseModel):
    
    age : int
    sex : int
    cp : int
    trestbps : int
    chol : int
    fbs : int
    restecg : int
    thalach : int
    exang : int
    oldpeak : float
    slope : int
    ca : int
    thal : int
    
#loading the saved model
heartmodel = pickle.load(open('trained_model.sav','rb'))

@app.post('/heart_disease_prediction')
def heart_dis_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['age']
    sex = input_dictionary['sex']
    cp = input_dictionary['cp']
    tres = input_dictionary['trestbps']
    chol = input_dictionary['chol']
    fbs = input_dictionary['fbs']
    restecg = input_dictionary['restecg']
    thalach = input_dictionary['thalach']
    exang = input_dictionary['exang']
    oldpeak = input_dictionary['oldpeak']
    slope = input_dictionary['slope']
    ca = input_dictionary['ca']
    thal = input_dictionary['thal']
    
    input_list = [age,sex,cp,tres,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    
    prediction = heartmodel.predict([input_list])
    
    if prediction[0] == 1:
        return "The Person having the given details has a heart disease"
    else:
        return "The Person with the given details does not have a heart disease"