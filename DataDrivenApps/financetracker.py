import yfinance as yf
import streamlit as st


st.write("""
# Simple Stock Price App
This App allows you to track the stock price of a given stock:
Example tickerSymbols
- Google: GOOGL
- Apple: AAPL
         """)


tickerSymbol = st.text_input("Enter the stock price you want to check")
start_data = st.text_input("Enter the start data for tracking? In format: yyyy-m-dd")
end_date = st.text_input("Enter the end data you want to track to? In format: yyyy-m-dd")

# Retrieve Data fro tickerSymbol 
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker:
tickerDf = tickerData.history(period='1d', start=start_data, end=end_date)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)