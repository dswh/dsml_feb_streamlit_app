import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser

    Shown are the stock prices of Apple.
    """
)


ticker_symbol = st.text_input(
                    "Enter Stock Symbol",
                    "AAPL",
                    key="placeholder"
)



# ticker_symbol = "AAPL"


col1, col2 = st.columns(2)

## start date of analysis
with col1:
    start_date = st.date_input("Input Starting Date",
                datetime.date(2019,1,1))

## end date
with col2:
    end_date = st.date_input("Input End Date",
                datetime.date(2022,12,31))

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d", 
                                start=f"{start_date}",
                                end=f"{end_date}")


st.write(f"""
### {ticker_symbol}'s EOD prices """)

st.dataframe(ticker_df)


##showcasing charts

st.write("""
## Daily Closing Price Chart
""")
st.line_chart(ticker_df.Close)


st.write("""
## Volume of Shares traded each day
""")
st.line_chart(ticker_df.Volume)