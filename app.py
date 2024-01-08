import streamlit as st
import pandas as pd
import numpy as np

from time import sleep

# 페이지 기본 설정
st.set_page_config(
    page_icon="👍",
    page_title="ㄴㅇ라넝ㄹㄴ",
    layout="wide"
)

# 페이지 헤더, 서브헤더 제목 설정
st.header("최고의 페이지")
st.subheader("뭐라는것이오")

number = st.number_input(
    label="나이를 입력해 주세요",
    min_value=10,
    max_value=100,
    value=30,
    step=5
)
st.write("당신이 입력하신 나이는 : ", number)

code = '''echo "하이";'''
st.code(code, language='php')

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )

st.write(f'You wrote {len(txt)} characters.')