import streamlit as st
import pandas as pd
from mylib import myTextAnalyzer as ta
from PIL import Image

def main():
        st.header("단어 빈도수 시각화")
    

@st.dialog("데이터 미리보기")
def preview_file(df):
    st.dataframe(df)

def whether_file(uploaded_file) :
    if uploaded_file :
        if st.button("데이터 파일 확인") :
            df = pd.read_csv(uploaded_file)
            preview_file(df)

def set_parameter():

    column_name = st.text_input("데이터가 있는 컬럼명(공백 구분)")

    st.subheader("설정")

    with st.form("parameters") :
        bar_words = st.checkbox("빈도수 그래프")
        count_bar_words = st.slider("단어 수", 10, 50, 30, 1)
        word_cloud = st.checkbox("워드 클라우드")
        count_word_cloud = st.slider("단어 수", 20, 500, 250, 1)  
        submitted = st.form_submit_button("분석 시작")
        if submitted :
            if bar_words or word_cloud :
                return {
                        "column_name" : column_name,
                        "bar_words" : bar_words, 
                        "count_bar_words" : count_bar_words,
                        "word_cloud" : word_cloud,
                        "count_word_cloud" : count_word_cloud
                        }
            else :
                st.warning("빈도수 그래프나 워드 클라우드를 선택하세요")
            
    return 0


def load_image(image_file) :
    img = Image.open(image_file)
    return img