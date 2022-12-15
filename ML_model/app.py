import streamlit as st
import pandas as pd
import numpy as np


st.header ("First Machine Learning Linear regression")

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
import os

# os.path : 파이썬 경로 문제 해결
model_path = f"{os.path.dirname(os.path.abspath(__file__))}/model.pkl"
model = joblib.load(model_path)
st.write("## 선형 회귀 모델")
st.write(pd.Series(model.coef_, index=["age", "bmi", "children", "smoker", "sex_male", "region_northwest", "region_northeast", "region_southwest"]))

# age : 나이
st.number_input(
    label="나이",
    step=1, 
    value=30,
    key='age'
)
# st.session_state['age']
# st.write(st.session_state['age'])

# sex : 성별
st.radio(
    label='성별',
    options=["남성", "여성"],
    index=0, # 기본 선택
    key='sex'
)
# st.write(st.session_state['sex'])

# bmi : 실수형
st.number_input(
    label="BMI",
    step=0.1, # 실수형으로 받을 수 있게
    value=25.0,
    key='bmi'
)
#st.write(st.session_state['bmi'])

# children : 자녀수
st.number_input(
    label="자녀수",
    step=1, 
    value=1,
    key='children'
)
#st.write(st.session_state['children'])

# smoker : 흡연여부
st.checkbox(
    label='흡연여부',
    value=False,
    key='smoker'
)
#st.write(st.session_state['smoker'])

# region : 지역

st.selectbox(
    label = "지역",
    options = ["북동쪽", "북서쪽", "남동쪽", "남서쪽"],
    index = 2,
    key = "region"
)

#st.write(st.session_state['region'])

if st.button('예측'):
    st.snow()
    st.balloons()
    # 예측
    # model.predict(X_test) >> 전처리한 데이터 형태로 들어간 행렬(df)
    # df 필요없고, 이중 리스트로 넣어도 됩니다.
    # 이중 리스트 : [[age, bmi, children, smoker, sex_male, region_northwest, region_northeast, region_southwest]]
    state = st.session_state
    input_values = [[]
        state['age'],state['bmi'],state['children'],state['smoker'],state['sex']=='남성',
        state['region']=='북서쪽',state['region']=='북동쪽', state['region']=='남서쪽'
    ]]
    pred = model.predict(input_values)
    st.write(pred[0])
