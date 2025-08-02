import pandas as pd

import streamlit as st

email = st.text_input("Enter Email")
password = st.text_input("Enter Password")

gender = st.selectbox("Select Gender",['male','female','other'])
btn = st.button("Login...")


if btn:
    if email == "shikherjain786@gmail.com" and password == "1234":
        # st.balloons()
        st.success("Login Successful")
        st.write(gender)
    else:
        st.error("Login Failed ")


file = st.file_uploader("Upload the CSV file",type=['csv']) 

if file is not None:
    df =pd.read_csv(file)
    st.dataframe(df)
    st.dataframe(df.head())
    st.dataframe(df.describe())