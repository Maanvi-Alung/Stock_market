#main streamlit code gui
import os
import numpy as np
import pandas as pd
import streamlit as st 
import plotly.express as px 

#title
st.title("STOCK HISTORICAL DATA")     
 
#loading data
option = st.selectbox('WHAT STOCK WOULD YOU LIKE TO KNOW ABOUT',('None','AAPL', 'DELL', 'TCS.IL','TSLA'))
if option =='None':
    st.write("Plese Select one option")
else:
    st.write('You selected:', option)
    df=pd.read_csv(f"data/{option}.csv")
#display dataset
    st.write(df) 

    st.subheader('Stock Graph')

    chart_data = pd.DataFrame(
        np.random.randn(20, 4),
        columns=['Open','High', 'Low', 'Close'])

    st.area_chart(chart_data)




