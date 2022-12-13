
import streamlit as st # st라는 이름으로 사용
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
st.write(titanic)