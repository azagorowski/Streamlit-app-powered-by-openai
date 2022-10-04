# App which shows price for Google stock from 7/01/2022 to 7/15/2022

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Stock prices App")

st.markdown("""
    * Open: Opening stock price for the day
    * High: Highest stock price for the day
    * Low: Lowest stock price for the day
    * Close: Closing stock price for the day
    * Adj Close: Adjusted closing stock price for the day
    * Volume: Number of shares traded for the day
""")

st.title("Google Stock Price")

@st.cache(persist=True)
def load_data():
    data = yf.download('GOOGL', start="2022-09-21", end="2022-10-03")
    return data

data = load_data()

st.markdown("""
    #### Google Stock Price from 9/21/2022 to 10/03/2022
""")

st.markdown("""
    ### Closing Price
""")

fig = px.line(data, x=data.index, y="Close")
st.plotly_chart(fig)

st.markdown("""
    ### Volume
""")

fig = px.bar(data, x=data.index, y="Volume")
st.plotly_chart(fig)


st.title("Apple Stock Price")

@st.cache(persist=True)
def load_data():
    data = yf.download('AAPL', start="2022-09-21", end="2022-10-03")
    return data

data = load_data()

st.markdown("""
    #### Apple Stock Price from 9/21/2022 to 10/03/2022
""")

st.markdown("""
    ### Closing Price
""")

fig = px.line(data, x=data.index, y="Close")
st.plotly_chart(fig)

st.markdown("""
    ### Volume
""")

fig = px.bar(data, x=data.index, y="Volume")
st.plotly_chart(fig)