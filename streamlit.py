import streamlit as st
import pandas as pd
import requests

# 1) 데이터프레임 생성
url="http://openAPI.seoul.go.kr:8088/76796269766f756835305541427a6e/json/SeoulLibNewArrivalInfo/1/1000/"
res = requests.get(url)
data = res.json()
df = pd.DataFrame(data['SeoulLibNewArrivalInfo']['row'])

# 2) 검색어 입력 받기
search_term = st.text_input('도서 검색어 입력:')

# 3) 검색 결과 필터링
if search_term:
    filtered_df = df[df['TITLE'].str.contains(search_term)]
    st.write(filtered_df)
else:
    st.write(df)

# 4) 검색 결과 페이지로 이동하는 버튼 생성
if st.button('검색 결과 페이지 보기'):
    url = 'https://search.kyobobook.co.kr/search'
    params = {'keyword': search_term, 'gbCode': 'TOT', 'target': 'total'}
    st.write('[검색 결과 페이지로 이동하기](' + url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()]) + ')')
