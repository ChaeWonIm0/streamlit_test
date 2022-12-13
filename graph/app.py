
import streamlit as st # st라는 이름으로 사용
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.write(
    '''
    # 탐색적 데이터 분석 (EDA) & Seaborn을 통한 데이터 시각화
    데이터의 특성에 따라서 시각화의 방식도 달라집니다

    ## 데이터의 종류

    정형 데이터 : 값으로 나타낼 수 있는 데이터 (숫자)
    비정형 데이터 : 정형 데이터가 아닌 것(이미지, 언어 등)
    1. 정형 데이터
    대분류	소분류	예시
    수치형 데이터
    (사칙 연산이 가능한 데이터)	연속형 데이터	키, 몸무게, 수입
    이산형 데이터	과일 개수, 책의 페이지 수
    범주형 데이터
    (범주로 나누어지는 데이터)	순서형 데이터	학점, 순위(랭킹)
    명목형 데이터	성별, 음식종류, 우편번호
    수치형 데이터 numerical data
    계산 가능한 데이터
    사칙 연산이 가능한 데이터

    연속형 데이터 : continuous data : 값이 연속된 데이터
    subway에서 15cm와 30cm 빵을 고른 경우 >> 16cm, 17cm, 18cm, ... 등 존재
    15.5cm, 16cm, 16.5cm ... 등이 존재. 값사이의 무한한 사이값 존재.
    값이 끊기지 않고 연속된 데이터입니다
    실수형(float)로 표현할 수 있는 데이터
    이산형 데이터 : discrete data : 정수로 딱 떨어져 셀 수 있는 데이터(자연수)
    초밥 : 12g (연속형 데이터) / 밥알 수는 320개, 320개 등 (이산형 데이터)
    정수형(int)로 표현할 수 있는 데이터
    범주형 데이터 categorical data
    범주를 나눌 수 있는 (그룹,분류, 소속) 데이터로, 사칙연산이 안됨
    순서형 데이터에 한해서 (ordinal data) 순위를 매길 수 있습니다(ranking) 크고 작음을 비교할 수 있음

    학점 (수우미양가, 분류체계), 스포츠 경기 순위

    명목형 데이터 nominal data : 순위가 따로 없는, 비교할 수 없는, 더 높고 낮는게 상관없는 유일한 데이터

    성별, 우편번호, 반, 소속 등

    숫자로만 되어 있다고 해서, 무조건 수치형 데이터는 아닙니다! (ex. 장발장의 죄수번호 '24601')
    탐색적 데이터 분석과 그래프
    그래프, 통계 수치 등을 활용해서 데이터를 파악하는 과정.
    탐색적 데이터 분석 단계에서는 다양한 그래프 그림
    그래프는 데이터를 한눈에 파악하기 쉬움 (경향성)
    데이터가 어떻게 구성되어 있는지
    어떤 변수(피처)가 중요한지
    어떻게 피처를 제시할지
    어떻게 새로운 변수를 만들지 등
    모델링에 필요한 다양한 정보를 얻을 수 있습니다.

    모델링
    1) 변수들에게 답을 이끌어내는 과정

    2) 어떠한 변수를 넣고, 빼야할까요

    3) 변형을 어떻게 시켜야 할까요.

    결측치, 이상치
    4) 전처리 → 피처 엔지니어링 > 모든 데이터를 하나하나 읽어서 못하겠으니, 차트, 플롯 => 경향성 => 변수(피처)를 튜닝해나가는 과정

    수치형 데이터 시각화
    수치형 데이터는 '일정한 범위 내에서 어떻게 분포(distribution) 되어있는지 중요해요.

    (몰려있는 경우, 퍼져있는 경우 등)

    이 분포를 알아야 데이터를 어떻게 변환할지,
    어떻게 해석해서 활용할지 판단할 수 있습니다.

    데이터의 분포가 열마다 다르면 머신러닝이 불가 어느정도 비슷한 모양으로 변경해서 스케일링합니다. 어떤 스케일링으로 할지는 관건
    '''

titanic = sns.load_dataset('titanic')
st.write(titanic) # 적당히 잘라줌

titanic.head()
    
sns.hisplot(data=titanic, x = 'age')
st.pyplot()
st.pyplot(fig)
    '''
    titanic.head()

    [ ]
    1
    titanic.tail()

    [ ]
    1
    titanic.info()
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 891 entries, 0 to 890
    Data columns (total 15 columns):
    #   Column       Non-Null Count  Dtype   
    ---  ------       --------------  -----   
    0   survived     891 non-null    int64   
    1   pclass       891 non-null    int64   
    2   sex          891 non-null    object  
    3   age          714 non-null    float64 
    4   sibsp        891 non-null    int64   
    5   parch        891 non-null    int64   
    6   fare         891 non-null    float64 
    7   embarked     889 non-null    object  
    8   class        891 non-null    category
    9   who          891 non-null    object  
    10  adult_male   891 non-null    bool    
    11  deck         203 non-null    category
    12  embark_town  889 non-null    object  
    13  alive        891 non-null    object  
    14  alone        891 non-null    bool    
    dtypes: bool(2), category(2), float64(2), int64(4), object(5)
    memory usage: 80.7+ KB
    [ ]
    1
    titanic.describe()
'''
'''
    히스토그램(histogram)
    수치형 데이터의 구간별 빈도수를 나타내는 그래프
    구조

    sns.histplot()
    형태
    histplot(data = 분석하려고 하는 데이터셋(데이터프레임), x = 분포를 파악하려는 변수명)

    [ ]
    ↳ 숨겨진 셀 7개
    커널밀도추정 함수 그래프 (kdeplot)
    커널 밀도 추정 kernel density estimation
    히스토그램을 매끄럽게 곡선으로 연결한 그래프
    [ ]
    ↳ 숨겨진 셀 12개
    러그플롯(rugplot)
    주변 분포 marginal distribution을 나타내는 그래프
    단독으로 사용하기보다는 주로 다른 분포도 그래프와 함께 사용합니다
    단일 변수가 어떻게 분포되어 있는지 x축 위에 작은 러그로 표시하는 플롯
    값이 밀집되어 있을 수록 러그들도 밀집
    [ ]
    ↳ 숨겨진 셀 2개
    범주형 데이터 시각화
    설명
    범주형 데이터 값에 따라 수치형 데이터 값이 어떻게 달라지는지 파악하기 위함
    막대그래프
    ↳ 숨겨진 셀 1개
    그래프
    x = 범주형 데이터 : 등급 y = 수치형 데이터 : 운임

    [ ]
    ↳ 숨겨진 셀 3개
    포인트 플롯 (pointplot)
    1) 막대그래프 모양만 다를 뿐, 동일한 정보 제공
    2) 막대그래프의 문제점 : 겹칠 때는 눈에 잘 띄지 않습니다.

    해결점 : 그래프를 점과 선으로 표시합니다.

    [ ]
    1
    sns.pointplot(x='class', y = 'fare', data=titanic)

    포인트 플롯
    포인트 플롯은 여러 그래프를 동시에 그릴 때 시각적으로 유리합니다

    [ ]
    ↳ 숨겨진 셀 2개
    박스플롯 (Boxplot)
    5가지 요약 수치 five-number summary (표시)

    제1사분위수(Q1): 전체 데이터 중 하위 25%에 해당하는 값
    제2사분위수(Q2): 50%에 해당하는 값(중앙값)
    제3사분위수(Q3): 상위 25%에 해당하는 값
    사분위범위수(IQR): Q3−Q1
    [ ]
    ↳ 숨겨진 셀 2개
    바이올린플롯(violinplot)
    박스플롯 + kde 합쳐놓은 그래프
    박스플롯 : 5개 지표 서머리 / 곡선 형태의 외형
    [ ]
    ↳ 숨겨진 셀 7개
    카운트플롯 (countplot)
    value_counts 랑 유사함

    범주형 데이터의 갯수를 확인할 때 사용

    [ ]
    ↳ 숨겨진 셀 11개
    barplot 과 countplot이 헷갈릴 경우
    barplot : 막대 그래프를 그려줌
    : 범주형 데이터별 수치형 데이터의 통계값(평균) countplot : 범주형 게이터의 갯수
    [ ]
    ↳ 숨겨진 셀 3개
    파이 그래프(pie)
    범주형 데이터별 비율을 알아볼 때 사용하는 그래프
    seaborn X (matplotlib을 써야함)
    [ ]
    1
    2
    3
    4
    5
    6
    import matplotlib.pyplot as pandas
    x = [10, 60, 30]
    labels = ['A','B','C']

    plt.pie(x=x, labels=labels, autopct='%.1f%%')
    plt.show()

    💞 데이터 관계 시각화
    데이터 간의 관계를 색상으로 표현한 그래프
    효과
    비교해야 할 데이터가 많을 때 주로 사용합니다.
    sns.heatmap ( ) 함수를 사용해서 호출합니다.
    [ ]
    ↳ 숨겨진 셀 10개
    라인 플롯(lineplot)
    두 수치형 데이터 사이의 관계를 나타낼 때 사용합니다(직선)
    x에 전달한 값에 따라 y에 전달한 값의 평균 + 신뢰구간
    구조
    sns.lineplot( )
    [ ]
    ↳ 숨겨진 셀 9개
    회귀선을 포함한 산점도 그래프 (regplot)
    regplot() : 산점도 + 선형회귀선
    회귀선을 그려서 데이터의 상관관계를 파악합니다.
    [ ]
    ↳ 숨겨진 셀 4개
    모든 종류의 그래프 소환 (pairplot)
    [ ]
    ↳ 숨겨진 셀 4개
    1차 과제
    데이터 시각화를 포함한 웹앱 제작

    streamlit, pandas, numpy, matplotlib, seaborn
    Streamlit
    파이썬 코드 만으로 웹에서 서비스되는 홈페이지를 만들어주는 프레임워크 입니다.
    '''
)

