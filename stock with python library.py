#This script to Extract Stock Data Using a Python Library


!pip install yfinance==0.1.67
#!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd

#Analyze AAPL stock info
apple = yf.Ticker("AAPL")
apple_info=apple.info
apple_info
apple_info['country']

#Extract AAPL share price index
apple_share_price_data = apple.history(period="max") 
#The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data.head()
apple_share_price_data.reset_index(inplace=True)
#Price AAPL share price over time
apple_share_price_data.plot(x="Date", y="Open")

#Extract AAPL share price index
apple.dividends
apple.dividends.plot()

#Analyze AMD stock info
amd = yf.Ticker("AMD")
amd_info=amd.info
amd_info['country']
amd_share_price_data.head()
amd_share_price_data.reset_index(inplace=True)
#Price AMD share price over time
amd_share_price_data.plot(x="Date", y="Open")
