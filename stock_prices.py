# App which shows price for Google and Apple stocks from 9/21/2022 to 10/03/2022

import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import date
import Main

st.set_page_config(page_title="GPT-3 Stock prices App", page_icon=":rocket:", layout="wide")

Main.app()

st.markdown("""
    * Open: Opening stock price for the day
    * High: Highest stock price for the day
    * Low: Lowest stock price for the day
    * Close: Closing stock price for the day
    * Adj Close: Adjusted closing stock price for the day
    * Volume: Number of shares traded for the day
""")

st.title("Current Google Stock prices")

today = date.today()

@st.cache(persist=True)
def load_data():
    data = yf.download('GOOGL', start="2022-10-04", end=today.strftime("%Y-%m-%d"))
    return data

data = load_data()

d1 = today.strftime("%m/%d/%Y")

st.markdown("""
    #### Google Stock Price from 10/04/2022 to {}
""".format(str(d1)))



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

st.title("Historical Google Stock prices")

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


st.title("Historical Apple Stock prices")

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