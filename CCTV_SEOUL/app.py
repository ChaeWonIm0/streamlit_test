import streamlit as st
import pandas as pd
import numpy as np

st.header("서울시 CCTV 현황 분석")

CCTV_Seoul = pd.read_csv('./CCTV_SEOUL/dataframe/CCTV_in_Seoul.csv', encoding='utf-8')
st.write(CCTV_Seoul)

st.line_chart(CCTV_Seoul)

# import plotly.express as px
# fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
# fig.show()