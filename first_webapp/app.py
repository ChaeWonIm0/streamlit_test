# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """ 
    ## 서울의 과거 사진 비교
    ## 
    """
)

# 이미지 링크 삽입


st.write(
    """
    ## 한강
    """
)

col1, col2, col3, col4 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
   st.header("An ho")
   st.image("https://static.streamlit.io/examples/owl.jpg")



