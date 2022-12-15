import streamlit as st
import pandas as pd
import numpy as np


st.header ("First Machine Learning Linear regression")

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)