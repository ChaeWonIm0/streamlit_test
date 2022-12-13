# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """ 
    # 제 첫 웹페이지입니다.
    ## 부족하지만 많이 사랑해주십쇼
    ### 기부는 1$씩
    #### 1$ 는 1300원 입니다.
    """
)

# 이미지 링크 삽입
st.image(
        "https://cdn.pixabay.com/photo/2018/03/27/17/25/cat-3266673_1280.jpg"
)
st.image(
            "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_1280.jpg"
)

st.image(
    "https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FZgihY%2FbtrSYmKNFXT%2FxjyZIeKs9s7wZ7HLaH9JK0%2Fimg.png"
)