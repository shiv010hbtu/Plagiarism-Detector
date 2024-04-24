import streamlit as st
from plagiarism_tool import tool
import pandas as pd
import numpy as np

st.title('Plagiarism Tool')

x = st.text_input('Enter sentence 1 here', placeholder='Sample Text')
y = st.text_input('Enter sentence 2 here', placeholder='sample text')
if len(x)==0 and len(y)==0:
    x = 'Sample Text'
    y = 'sample text'
# if len(y)==0:
#     x = 'Sample Text'
#     y = 'sample text'
    
z = tool(x,y)[0]
m = tool(x,y)[1]
section = st.sidebar.radio('Explore Different Tools from here :' , ['Plagiarism Tool','Bag of Word Model','Chart Analysis'])
if section=='Plagiarism Tool':
    st.write('Sentence 1: ' , x)
    st.write('Sentence 2 : ',y)
    if z*100 > 50:
        emoji = ':sunglasses:'
    else:
        emoji = ':cry:'
    st.write(f'Similarity : The two given sentences are {z*100:.2f}% similar {emoji}')

elif section=='Bag of Word Model':
    st.header('Bag of word model for the given DataFrame')
    mn = pd.DataFrame(m , index = ['Sentence 1' , 'Sentence 2'])
    st.write(mn)
elif section=='Chart Analysis':
    st.header('Chart Analysis of the text inputs')
    mn = pd.DataFrame(m , index = ['Sentence 1' , 'Sentence 2'])
    st.bar_chart(mn) 