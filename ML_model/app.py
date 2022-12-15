import streamlit as st
import pandas as pd
import numpy as np


st.header ("First Machine Learning Linear regression")

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
model = joblib.load('./ML_model/app.py')
model_info = pd.Series(model.coef_, index = df.drop['expenses'].X.columns)
st.write(model_info)