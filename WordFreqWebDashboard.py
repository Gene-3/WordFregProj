import streamlit as st
from mylib import myTextAnalyzer as ta
from mylib import myStreamlitVisualizer as sv
from konlpy.tag import Okt

sv.main()

with st.sidebar :
    uploaded_file = st.file_uploader("파일 선택", type = ['csv'])

    sv.whether_file(uploaded_file)

    params = None
    my_stopwords = []
    title = None
    ylabel = None
    if uploaded_file :
        params = sv.set_parameter()
        my_stopwords = st.text_area("불용어를 입력하세요",'').split()
        st.subheader("워드클라우드")
        title = st.text_input("타이틀을 입력해주세요")
        ylabel = st.text_input("키워드를 입력해주세요")
    else : 
        st.warning("파일을 첨부해주세요")


if uploaded_file and params and params["column_name"]:
    target_column = params.get("column_name")

    counter = None
    if target_column :
        corpus = ta.load_corpus_from_csv(uploaded_file, params['column_name'])
        tokenizer = Okt().pos
        my_tags = ['Noun', 'Verb', 'Adjective']
        num_words = 20
        font_path = 'c:/Windows/Fonts/malgun.ttf'

        with st.spinner("빈도수 그래프 생성중...") :
            tokens = ta.tokenizer_korean_corpus(corpus, tokenizer, my_tags, my_stopwords)
            counter = ta.analyze_word_freq(tokens)
        
    if params.get("bar_words") :
        xlabel = '빈도수'
        ta.visualize_barhgraph(counter, num_words, title, xlabel, ylabel, font_path)
        
        
    if params.get("word_cloud") :
            ta.visualize_wordcloud(counter, num_words, font_path)
if uploaded_file and params and not params["column_name"]:
    st.warning("컬럼명을 입력하세요")
