import pandas as pd
import streamlit as st

#To Run the app use this command -> streamlit run main.py
st.title('Streamlit App')

st.write('Hello World')

st.write('This is a DataFrame')
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

st.button('Say Hello')


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

name = st.text_input('What is your name?')
if name:
    st.write(f'Hello {name}')

options = ['python','java','c++']
st.selectbox('Select a language', options)
