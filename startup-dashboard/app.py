import pandas as pd
import streamlit as st

df = pd.read_csv("startup_cleaned.csv")


st.sidebar.title("Starting Funding Analysis")

option = st.sidebar.selectbox("Select one", ['Overall Analysis', 'StartUp', 'Investor'])

if option == "Overall Analysis":
    st.title("Overall Analysis")

elif option == "StartUp":
    st.sidebar.selectbox("Select StartUp",df['startup'].unique())
    st.title("StartUp Analysis")
    btn1 = st.sidebar.button("Find Startup Detail")
    
else:
    st.sidebar.selectbox("Select Investor",sorted(set(df['investor'].str.split(',').sum())))
    st.title("Investor Analysis")
    btn2 = st.sidebar.button("Find Investor Detail")








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