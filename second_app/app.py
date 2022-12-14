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

st.header("Size of the fashion market for all items_bar_chart")
st.bar_chart(fashion, width = 150, height = 600)
import plotly.express as px

# st.header("Male formal Market size")
# st.bar_chart(fashion, x="Male_formal", y="2020", color="2021")

# fig = px.scatter(fashion)
# fig.show()

# fig = px.parallel_categories(fashion_market)

fashion_market = pd.pivot_table(fashion, index = 'index')
st.write(fashion_market)

import plotly.graph_objects as go

st.header ("2022_SS pie chart ")
labels = ['Male_formal','Female_formal','Casual','Sprots','Inner','kids','Shoes']
values = [1921,1359,8311,2697,964,584,3386]
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
st.plotly_chart(fig)

data = {
    "항목" : ["Male_formal", "Female_formal", "Casual", "Sports", "Inner", "Kids", "Shoes", "bag"],
    "2020_SS" : [1538.9, 1187.5, 6993, 2265.6, 911.1, 356.5, 2917.5, 1273.4],
    "2020_FW" : [2342.1, 1480.1, 8612.7, 3714.5, 1196.5, 555.5, 3187.6, 1790.4],
    "2020" : [3881, 2667.7, 15605.6, 5980.1, 2107.6, 912, 6105.1, 1247],
    "2021_SS" : [1888.4, 1660.7, 7665.1, 2402.2, 864.9, 487, 3093, 1691.4],
    "2021_FW" : [2565.3, 1484.3, 9747.8, 3387.4, 1201.9, 637.7, 3575.1, 2938.5],
    "2021" : [4453.6, 3085, 17402.9, 5789.6, 2066.8, 1124.7, 6668.1, 1353.1],
    "2022_SS" : [1921.1, 1359.7, 8311.2, 2696.9, 964.6, 584.2, 3386.9, 0]
}
columns = ["항목", "2020_SS", "2020_FW", "2020", "2021_SS","2021_FW", "2021", "2022_SS"]
index = ["Male_formal", "Female_formal", "Casual", "Sports", "Inner", "Kids", "Shoes", "bag"]
df = pd.DataFrame(data, index=index, columns=columns)

fig = plt.figure(figsize=(8,4))
sns.histplot(data = df, x = 'Casual')
st.pyplot(fig)

# st.write(fashion_market)

st.write("")
"copyright by JiWon Seo & Chaewon Im"
st.write("")