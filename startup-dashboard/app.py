import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.set_page_config(layout = 'wide',page_title = "Startup Analysis")
df = pd.read_csv("startup_cleaned.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

def load_overall_analysis():

    # Total funding (in INR Crores) across all funding rounds.
    total = round(df['amount'].sum())

    # Average total funding per startup.
    avg = df.groupby('startup')['amount'].sum().mean()
    
    # Highest single funding round received by any startup.
    max = df.groupby('startup')['amount'].max().sort_values(ascending = False).head(1).values[0]
    
    # Total highest funding received by a single startup (all rounds combined).
    max1 = df.groupby('startup')['amount'].sum().max()
    
    total_startup = df['startup'].nunique()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric('Total',str(total)+' Cr')

    with col2:
        st.metric('Total Startups',total_startup)

    with col3:
        st.metric('Average',str(round(avg))+' Cr')


    col4, col5 = st.columns(2)
    with col4:
        st.metric('Highest single funding',str(max)+' Cr')

    with col5:
        st.metric('Total highest funding',str(max1)+' Cr')
        
    

    st.header("Month on Month Graph")
    
    selected_option = st.selectbox('Select Type' ,['Total','Count'])
    if selected_option == 'Total':
        t_df = df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
        t_df = df.groupby(['year','month'])['amount'].count().reset_index()
    
    t_df['x-axis'] = t_df['month'].astype('str') + '-' +t_df['year'].astype('str')

    fig_m, ax_m = plt.subplots()
    ax_m.plot(t_df['x-axis'],t_df['amount'])
    st.pyplot(fig_m)



def load_investment_details(investor):

    st.header(investor)

    last_5df = df[df["investor"].str.contains(investor)][['date','startup','vertical','city','round','amount']].head(5)
    big_series = df[df["investor"].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending =False).head(5)
    
    st.subheader("Most Recent Investment")
    st.dataframe(last_5df)
    
    st.subheader("Biggest investor")
    col1,col2 = st.columns(2)

    with col1:
        st.subheader(f"{investor} investor Table")
        st.dataframe(big_series)

    with col2:
        st.subheader(f"{investor} investor Graph")
        fig, ax = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)


    vertical_series = df[df["investor"].str.contains(investor)].groupby('vertical')['amount'].sum()
    round_series = df[df["investor"].str.contains(investor)].groupby('round')['amount'].sum()
    city_series = df[df["investor"].str.contains(investor)].groupby('city')['amount'].sum()
    
    colG1,colG2,colG3 = st.columns(3)

    with colG1:
        st.subheader("Sector Invested In ")
        fig_v, ax_v = plt.subplots()
        ax_v.pie(vertical_series, labels = vertical_series.index)
        st.pyplot(fig_v)
        
    with colG2:
        st.subheader("Stage Invested In ")
        fig_r, ax_r = plt.subplots()
        ax_r.pie(round_series, labels = round_series.index)
        st.pyplot(fig_r)
        
    with colG3:
        st.subheader("City Invested In ")
        fig_c, ax_c = plt.subplots()
        ax_c.pie(city_series, labels = city_series.index)
        st.pyplot(fig_c)


    year_series = df[df["investor"].str.contains(investor)].groupby('year')['amount'].sum()

    st.subheader("Year Of Year Investment Graph ")
    fig_y, ax_y = plt.subplots()
    ax_y.plot(year_series.index,year_series.values)
    st.pyplot(fig_y)


st.sidebar.title("Starting Funding Analysis")
option = st.sidebar.selectbox("Select one", ['Overall Analysis', 'StartUp', 'Investor'])

if option == "Overall Analysis":
    st.title("Overall Analysis")
    # btn0 = st.sidebar.button('Show Overall Analysis')
    # if btn0:
    #     with st.spinner("Loading Overall Analysis details..."):
    #         load_overall_analysis()
    load_overall_analysis()


elif option == "StartUp":
    st.sidebar.selectbox("Select StartUp",df['startup'].unique())
    st.title("StartUp Analysis")
    btn1 = st.sidebar.button("Find Startup Detail")
    
else:
    selected_investor = st.sidebar.selectbox("Select Investor",sorted(set(df['investor'].str.split(',').sum())))
    btn2 = st.sidebar.button("Find Investor Detail")
    st.title("Investor Analysis")
    if btn2:
        with st.spinner("Loading investment details..."):
            load_investment_details(selected_investor)










# email = st.text_input("Enter Email")
# password = st.text_input("Enter Password")

# gender = st.selectbox("Select Gender",['male','female','other'])
# btn = st.button("Login...")


# if btn:
#     if email == "shikherjain786@gmail.com" and password == "1234":
#         # st.balloons()
#         st.success("Login Successful")
#         st.write(gender)
#     else:
#         st.error("Login Failed ")


# file = st.file_uploader("Upload the CSV file",type=['csv']) 

# if file is not None:
#     df =pd.read_csv(file)
#     st.dataframe(df)
#     st.dataframe(df.head())
#     st.dataframe(df.describe())