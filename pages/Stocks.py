from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
from datetime import datetime

stock_list= st.selectbox('WHAT STOCK WOULD YOU LIKE TO KNOW ABOUT',('NONE','AAPL', 'DELL', 'GOOGL','TSLA','TCS.IL'))

if stock_list=='NONE':
    print("PLEASE SELECT ONE OPTION")
else:
# if st.button('Get Stock data') and stock:
    ts = TimeSeries(key='BVMZ1ZAX465D7AQ8', output_format='pandas')
    df, meta_data = ts.get_intraday(symbol=stock_list,interval='1min', outputsize='full')
    st.sidebar.info('Meta data')
    st.sidebar.write(meta_data)
    st.sidebar.write(df.columns)
    st.dataframe(df, use_container_width=True)

    st.subheader('Candlestick Visualization')
    size = st.select_slider('Select a date range (1M, 3M, 6M)', [30, 90, 180])
    dfs = df.tail(size)
    fig = go.Figure(data=[go.Candlestick(x=dfs.index, open=dfs['1. open'], high=dfs['2. high'], low=dfs['3. low'], close=dfs['4. close'])])
    st.plotly_chart(fig, use_container_width=True)




