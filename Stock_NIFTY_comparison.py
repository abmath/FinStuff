import streamlit as st
import numpy as np
import pandas as pd
from datetime import date
from nsepy import get_history

stock = st.text_input('Your stock')
#st.text(stock)

start_dt = st.date_input('Select start date of analysis')

end_dt = st.date_input('Select end date of analysis')

if len(stock) < 3:
	st.text('Please select a stock')
elif end_dt <= start_dt:
	st.text('Please select appropriate date ranges')
else:
	st.text('Showing analysis of '+stock+' vs NIFTY for '+str(start_dt)+' to '+str(end_dt))


# Get NIFTY Data

nifty_df = get_history(symbol = 'NIFTYBEES', start = start_dt, end = end_dt)

if nifty_df.shape[0] == 0:
	st.text("Unable to download NIFTY data please retry")

nifty_df = nifty_df['symbol','VMAP','Open','High','Low']

stock_df = get_history(symbol = stock, start = start_dt, end = end_dt)

if stock_df.shape[0] == 0:
	st.text('Unable to get stock data, please retry or rework on the input parameters')

stock_df = stock_df['symbol','VMAP','Open','High','Low']
stock_df.columns = ['stock'+var for var in stock_df.columns]

analysis_pd = pd.merge(stock_df, nifty_df, on = 'Date')
st.text('Done!')


# Functionalities to show

#1 Line chart of prices over date
#2 Delta changes over 1,2,3 days
#3 Correlation between price changes and delta changes
#4 


