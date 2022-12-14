import streamlit as st
import numpy as numpy
import pandas as pandas

import plotly.graph_objects as go

labels = ['Male_formal','Female_formal','Casual','Sprots','Inner','kids','Shoes']

values = [1921,1359,8311,2697,964,584,3386]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

st.plotly_chart(fig)