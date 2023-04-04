import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image
import time


st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

Latest_iteration = st.empty()
bar = st.progress(0)

import time 
for i in range(100):
    Latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column, = st.beta_columns(2)
button =left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味:' , text
# 'コンディション:' , condition


# if st.checkbox('Show Image'):
#     img = Image.open('muji.jpg') 
#     st.image(img, caption='Yuri', use_column_width=True)

