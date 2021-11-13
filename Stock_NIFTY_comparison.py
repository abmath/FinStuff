import streamlit as st
import numpy as np
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


# Functionalities to show

#1 Line chart of prices over date
#2 Delta changes over 1,2,3 days
#3 Correlation between price changes and delta changes
#4 


