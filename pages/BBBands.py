from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import numpy as np
from alpha_vantage.techindicators import TechIndicators
import pandas as pd
from datetime import datetime



st.title(f'BBbands indicator (60 min)')
ti = TechIndicators(key='BVMZ1ZAX465D7AQ8', output_format='pandas')
opt= st.selectbox('WHAT STOCK WOULD YOU LIKE TO KNOW ABOUT',('NONE','AAPL', 'DELL', 'GOOGL','TSLA'))
if opt=='NONE':
    print("PLEASE SELECT ONE OPTION")
else:
    data, meta_data = ti.get_bbands(symbol=opt, interval='60min', time_period=60)
    st.line_chart(data)
    st.write(data)