# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
st.write(titanic) # 적당히 짤라줌

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """ 
    ## 서울의 과거 사진
    ## 
    """
)

# 이미지 링크 삽입


st.write(
    """
    ## 귀엽죠?
    """
)

st.image(
        "https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg"
)


st.image(
            "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg"
)


st.image(
    "https://cdn.pixabay.com/photo/2017/08/07/22/57/coffee-2608864_1280.jpg"
)


st.image(
    "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg"
)



st.image(
    "https://cdn.pixabay.com/photo/2016/01/20/13/05/cat-1151519_1280.jpg"
)

st.write(
    """




    ## 정답은 인간입니다.

    """
)

st.image(
    "https://cdn.pixabay.com/photo/2022/12/13/03/12/03-12-04-105_1280.jpg"
)




