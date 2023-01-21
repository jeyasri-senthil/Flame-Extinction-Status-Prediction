# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:07:39 2023

@author: jeyasri
"""

import numpy as np
import pickle
import streamlit as st

# Loading the trained model
loaded_model = pickle.load(open('C:/Users/jeyasri/Downloads/Acoustic Fire Extinguisher/fireextinction_trained.sav','rb'))

def flamestatus_prediction(input_data):
    
    #changing the input data into numpy array
    id_np_array = np.asarray(input_data)
    id_reshaped = id_np_array.reshape(1,-1)

    prediction = loaded_model.predict(id_reshaped)
    print(prediction)

    if(prediction[0]==0):
        return "STATUS: FLAME IS NOT EXTINCTED"
    else:
        return "STATUS: FLAME IS EXTINCTED"
    
def main():
    
    st.title('FLAME STATUS PREDICTION')
    
    SIZE = st.text_input('FLAME SIZE (cm)')
    FUEL = st.text_input('FUEL USED')
    DISTANCE = st.text_input('DISTANCE SPREAD (cm)')
    DESIBEL = st.text_input('DECIBEL VALUE (dB)')
    AIRFLOW = st.text_input('LEVEL OF AIRFLOW (m/s)')
    FREQUENCY = st.text_input('FIRE FREQUENCY (Hz)')
    
    
    # Prediction code
    diagnosis = ''
    
    if st.button('PREDICT'):
        diagnosis = flamestatus_prediction([SIZE, FUEL, DISTANCE, DESIBEL, AIRFLOW, FREQUENCY])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    

