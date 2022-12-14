import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# from streamlit_image_comparison import image_comparison
# import cv2


st.set_page_config("Fashion Trand")


st.image("./2020 image/유아인.png") #카메라


st.header("1980's Fashion vs 2020's Fashion")

st.write("")
"This web is a site where you can know the fashion from the past to the present.!"
st.write("")

st.markdown("### 1980's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("./1980 image/1980패션 봄.jpg")

with col2:
   st.header("Summer")
   st.image("./1980 image/1980패션 여름.jpg")
with col3:
    st.header("Fall")
    st.image("./1980 image/1980패션 가을.jpg")

with col4:
    st.header("Winter")
    st.image("./1980 image/1980패션 겨울.jpg")

st.markdown("### 2020's Fashion")
col1, col2, col3, col4 = st.columns(4)

with col1:
   st.header("Spring")
   st.image("./2020 image/2020패션 봄.jpg")

with col2:
   st.header("Summer")
   st.image("./2020 image/2020패션 여름.jpg")

with col3:
    st.header("Fall")
    st.image("./2020 image/2020패션 가을.jpg")

with col4:
    st.header("Winter")
    st.image("./2020 image/2020패션 겨울.jpg")

add_selectbox = st.sidebar.selectbox("여성패션 온라인 쇼핑몰", ("---선택해주세요---","45번가", "갠소", "고고싱","그녀희재","그레이시크"))

add_selectbox = st.sidebar.selectbox("남성패션 온라인 쇼핑몰", ("---선택해주세요---","무신사", "디에프디", "힙합퍼",))

add_selectbox = st.sidebar.selectbox("액세서리 온라인 쇼핑몰", ("---선택해주세요---","도나앤디","러블링","윙블링"))

add_selectbox = st.sidebar.selectbox("신발 온라인 쇼핑몰", ("---선택해주세요---","러블리슈즈", "보가", "사뿐",))

st.header(" 1st half of 2020 - 1st half of 2022 Fashion market size trend ")

st.markdown("#####      (Unit: KRW 1 billion) ")

fashion = pd.read_csv("./dataframe/2020-2022_fashion_marketing.csv")
st.write(fashion)
# graph = sns.pairplot(fashion)

st.header("Size of the fashion market for all items")
st.bar_chart(fashion, width = 150, height = 600)


import plotly.express as px

# st.header("Male formal Market size")
# st.bar_chart(fashion, x="Male_formal", y="2020", color="2021")

# fig = px.scatter(fashion)
# fig.show()

# fig = px.parallel_categories(fashion_market)


# st.line_chart(data=mosq_data, x='모기지수 발생일', 
#                               y=['모기지수(수변부)','모기지수(주거지)','모기지수(공원)'])

fashion_market = pd.pivot_table(fashion, index = 'index')
#st.write(fashion_market)

st.header("Male formal Market size")
st.area_chart(fashion_market, height = 600)

st.line_chart(data="fashion_market")

def draw_line_plot(style):
  plt.title('나이와 재산 간 상관관계')
  plt.plot(
      [10,20,30,40], # x축에 위치할 데이터
      [1,4,9,16], # y축에 위치할 데이터
      style
  )
  plt.xlabel('나이')
  plt.ylabel('재산')
  plt.grid(True)
  plt.show()