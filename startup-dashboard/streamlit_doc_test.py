import streamlit as st
import pandas as pd
import time


st.title("Startup Dashboard")
st.header("I'm Learning Streamlit")
st.subheader("It is very good Library")

st.write('this is the normal text using write')

st.markdown("""
### Movies
- Pushpa 2
- Jawan
- Pathaan
- Bahubali
- Avengers
""")

st.code("""
def fx(x):
    return x**2
        
x = fx(29)
print(x)

""")

st.latex(f"""
23 + 5  = {23+5} 
(x+y)^2 = x^2 + y^2 +2.a.b
""")

df = pd.DataFrame({
    'name':['abc','pqr','xyz'],
    'marks':[80,70,76],
    'package':[10,24,45]
})

st.dataframe(df)

st.metric('Revnue','RS 3L','3%')
st.metric('Revnue','RS 3L','-3%')
st.metric('Revnue','RS 3L','+3%')

st.json({
    'name':['abc','pqr','xyz'],
    'marks':[80,70,76],
    'package':[10,24,45]
})

st.image('image.png')
st.video('https://youtu.be/EFmxPMdBqmU')

st.sidebar.title('Side Title')
st.sidebar.image('image.png')
st.sidebar.video('https://youtu.be/EFmxPMdBqmU')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Column 1 Title')
    st.image('image.png')
with col1:
    st.video('https://youtu.be/EFmxPMdBqmU')
    
with col2:
    st.subheader('Column 2 Title')
    st.image('image.png')
    st.video('https://youtu.be/EFmxPMdBqmU')


st.error('Login failed !')
st.success('Login success !')
st.info('Information')
st.warning('Warning !')

st.progress(26)


bar = st.progress(0)

_,_,_,_,_,_,_,_,_,_,_,_,_,_,col_progress = st.columns(15)

with col_progress:
    bar_txt = st.empty()

for i in range(1,101):
    time.sleep(0.01)
    bar.progress(i)
    bar_txt.write(i)


email = st.text_input("Enter Email")
age = st.number_input("Enter Age")
date = st.date_input("Enter Date")
st.write(email,age,date)


