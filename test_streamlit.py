import streamlit as st

st.title('Hello, Streamlit World')

name = 'kwangjin'
st.title(f'Hello, {name}. Welcome~~~~')

'다음은 데이터 프레임 출력 예시입니다.'
import pandas as pd
df = pd.DataFrame({
    'A' : [1, 2, 3, 4,],
    'B' : [10, 20, 30, 40]
})

df

import time
text = st.info('텍스트가 변할 겁니다.')
time.sleep(2)
text.info('2초가 지났습니다.')