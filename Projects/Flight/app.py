import streamlit as st
from db_helper import DB
import plotly.express as px

db = DB()

st.sidebar.title("Flights Analytcis")
option = st.sidebar.selectbox("Flights Analytcis",['Select','Check Flight','Data Analysis','Data Visualization'])

if option == 'Check Flight':
    st.title("Flights Analytcis")
    st.subheader("Overview")
    st.sidebar.write("""
    This application is designed to analyze flight data, providing insights into various aspects such as delays, cancellations, and on-time performance. Users can explore the data through interactive visualizations and statistical summaries.
    """)

    col1,col2 = st.columns(2)

    with col1:
        Source = st.selectbox("Select Source City",db.fetch_source_city_names())
        # st.write(db.fetch_source_city_names())

    with col2:
        Destination = st.selectbox("Select Destination City",db.fetch_destination_city_names())
        # st.write(db.fetch_destination_city_names())

    if st.button("Search"):
        st.write(f"Searching flights from {Source} to {Destination}...")
        st.dataframe(db.fetch_all_flights(Source,Destination))
        pass

elif option == 'Data Analysis':
    st.title("Data Analysis")
    st.subheader("Analyzing Flight Data")
    st.sidebar.write("""
    In this section, we will perform data analysis on the flight dataset. We will look into patterns, trends, and anomalies in the data to derive meaningful insights.
    """)
    airline, frequency = db.fetch_airline_frequencies()

    # st.write(freq) 
    data = {'Airlines': airline, 'Frequencies': frequency}
    fig = px.pie(data, values='Frequencies', names='Airlines', title='Simple Pie Chart')
    st.plotly_chart(fig) 

    # cities, frequencies = db.fetch_busy_airport()
    df = db.fetch_busy_airport()
    st.dataframe(df)
    fig = px.bar(df, x=0, y=1, title='Busy Airports', labels={'0': 'Airport', '1': 'Number of Flights'})
    st.plotly_chart(fig, use_container_width=True)

    df1 = db.daily_freq()
    st.dataframe(df1)
    fig = px.line(df1, x=0, y=1, title='Daily Flight Frequencies', labels={'0': 'Date of Journey', '1': 'Number of Flights'})
    st.plotly_chart(fig, use_container_width=True)

elif option == 'Data Visualization':
    st.title("Data Visualization")
    st.subheader("Visualizing Flight Data")
    st.sidebar.write("""
    This section focuses on visualizing the flight data using various charts and graphs. Users can interact with the visualizations to better understand the data and its implications.
    """)
else:
    st.title("Welcome")
    st.sidebar.write("Select an option from the sidebar to get started.")

