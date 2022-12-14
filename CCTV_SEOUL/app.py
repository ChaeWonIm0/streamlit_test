import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

st.header("서울시 CCTV 현황 분석")

CCTV_Seoul = pd.read_csv('./CCTV_SEOUL/dataframe/CCTV_in_Seoul.csv', encoding='utf-8')
st.write(CCTV_Seoul)

CCTV_Seoul.columns