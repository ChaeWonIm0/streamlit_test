# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
from streamlit_image_comparison import image_comparison


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

st.image(
        "https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg"
)

col1, col2 = st.coloumns(2)
col1.image = "https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg"
col2.image = "https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg"


st.image(
            "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg"
)



st.write(
    """
    ## 청계천

    """
)

st.image(
    "https://cdn.pixabay.com/photo/2022/12/13/03/12/03-12-04-105_1280.jpg"
)




