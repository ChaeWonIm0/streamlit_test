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
    "file:///C:/Users/%EC%9E%84%EC%B1%84%EC%9B%90/Downloads/%EB%8C%91(@dap.chaewon)%20%E2%80%A2%20Instagram%20%EC%82%AC%EC%A7%84%20%EB%B0%8F%20%EB%8F%99%EC%98%81%EC%83%81.html"
)