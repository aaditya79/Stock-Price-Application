import streamlit as st
import yfinance as yf

st.write("""
# Stock Price Application 
###### Found below are the opening and closing prices for different stocks between 2012-06-02 and 2022-06-02. 
""")

st.write("""
## GOOGL
""")
data = yf.Ticker('GOOGL')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## TSLA
""")
data = yf.Ticker('TSLA')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## NVDA
""")
data = yf.Ticker('NVDA')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## META
""")
data = yf.Ticker('META')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## AAPL
""")
data = yf.Ticker('AAPL')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## AMZN
""")
data = yf.Ticker('AMZN')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## NFLX
""")
data = yf.Ticker('NFLX')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## TWTR
""")
data = yf.Ticker('TWTR')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## MSFT
""")
data = yf.Ticker('MSFT')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## HPE
""")
data = yf.Ticker('HPE')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## IBM
""")
data = yf.Ticker('IBM')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)

st.write("""
## INTC
""")
data = yf.Ticker('INTC')
ch = data.history(period='1d', start='2012-6-2', end='2022-6-2')
st.write("""
###### Opening Price
""")
st.line_chart(ch.Open)
st.write("""
###### Closing Price
""")
st.line_chart(ch.Close)
