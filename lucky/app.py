# streamlit 라이브러리 호출
import streamlit as st
import numpy as np

# https://docs.streamlit.io/library/get-started/main-concepts
# st.write() 마크다운
st.title("조추첨 페이지")

st.header("여러분의 참여를 환영합니다!")

# 추첨 대상인 13명의 이름을 넣을 수 있는 text_input
# 3 x 4 (row, col)
# 열을 배치하는 메소드
columns = st.columns(4) # 화면을 열로 나누어서 배치합니다.
# 가로 4개의 열 -> columns = [col1, col2, col3, col4]
# col1, col2, col3, col4
# enumerate : index, value 묶음
for idx, col in enumerate(columns): # 열의 위치
    # 이중 for문 (for문 안에 for문)
    # col.text_input(f"조 추첨 대상 {idx+1}", key=idx)
    for idx2 in range(4):
        # key가 겹치면 안 됨
        # col 안에 메소드를 통해서 요소들을 생성해주겠다
        col.text_input(
            f"조 추첨 대상 {idx+1 + idx2 * 4}",
            key=f"{idx+1 + idx2 * 4}"
        ) # 4번 호출됨

# <추첨 버튼>
# 13개의 짝을 지어서 표시해줄 그래픽
st.write(st.session_state)


st.image(
    "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg"
)

