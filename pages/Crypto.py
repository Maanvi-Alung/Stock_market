from alpha_vantage.cryptocurrencies import CryptoCurrencies
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from datetime import datetime
from alpha_vantage.foreignexchange import ForeignExchange

cc = CryptoCurrencies(key='JZ41SNOYP2OIRYT3', output_format='pandas')
data, meta_data = cc.get_digital_currency_daily(symbol='BTC', market='INR')
data['4b. close (USD)'].plot()
st.title('Daily close value for bitcoin (BTC)')
st.write(data)
st.subheader('BAR GRAPH')
st.bar_chart(data)


st.title("CURRENT EXCHANGE VALUE")

option = st.selectbox('CURRENCY',('None','AUD', 'CAD', 'INR'))
if option =='None':
    st.subheader("Plese Select one currency")
else:
    cc = ForeignExchange(key='BVMZ1ZAX465D7AQ8')
    # There is no metadata in this call
    data, _ = cc.get_currency_exchange_rate(from_currency='BTC',to_currency=option)
    st.write(data)