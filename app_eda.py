import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np



def run_eda_app():
    st.write('데이터')

    # 데이터 불러오기
    df = pd.read_csv("./Data/Final.csv")

    # 첫 번째 열 제거 및 컬럼 이름 변경
    df = df.drop(df.columns[0], axis=1)
    df = df.rename(columns={'Entity': 'Country'})

    # 데이터프레임 표시
    st.dataframe(df)

    # 간편 통계 데이터 확인 체크박스
    if st.checkbox('간편 통계 데이터 확인하기'):
        st.dataframe(df.describe())
    else:
        st.text("")

    # 검색 기능
    st.header('검색')
    search = st.text_input('국가별 검색')

    # 검색어와 일치하는 국가 목록 필터링 및 중복 제거
    if search:
        filtered_countries = df[df['Country'].str.contains(search, case=False, na=False)]['Country'].tolist()
    else:
        filtered_countries = df['Country'].tolist()

    # 중복 제거
    filtered_countries = list(set(filtered_countries))

    # 선택박스에 필터링된 국가 목록 표시
    selected_country = st.selectbox('국가를 선택하세요', filtered_countries, key='country_select')
    

    # 선택된 국가의 데이터를 필터링하여 표시
    if selected_country:
        result = df[df['Country'] == selected_country]
        st.dataframe(result)


    




