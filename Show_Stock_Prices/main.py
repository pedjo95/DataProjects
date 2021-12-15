import yfinance as yf
import streamlit as st

st.write("""
    # Simple Stock Price App
    
    The stock **closing price** and **volume** of Google!
""")

tickerSymbol = 'GOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
