import streamlit as st
# from from_mongo import df

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# st.data_editor(df)
