
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go

import pandas as pd
from datetime import datetime



ts = TimeSeries(key='BVMZ1ZAX465D7AQ8', output_format='pandas')
df_list = {}
stock_list = ['TSLA','GOOGL','AAPL','AMZN']
selected_stocks = st.multiselect('select stocks to compare', stock_list)
selected_col = st.sidebar.radio("select a column", ['1. open', '2. high', '3. low', '4. close', '5. volume'])
data_size = st.select_slider('Select a date range (1M, 3M, 6M)', [30, 90, 180], key='slider2')
for name in selected_stocks:
    df_list[name] = ts.get_intraday(symbol=name,interval='1min', outputsize='full')
comp_graphs = []
for key, data in df_list.items():
    dataframe = data[0]
    fig = px.line(dataframe.tail(data_size), x=dataframe.tail(data_size).index, y=selected_col, title=f'{key} graph')    
    st.plotly_chart(fig, use_container_width=True)
























