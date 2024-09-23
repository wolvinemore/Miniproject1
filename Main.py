### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

#Imports
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
#import pdb; pdb.set_trace()

# generate market data

ticker = "AAPL"

#ticker = yf.Ticker(ticker_symbol)
stock_data = yf.download(ticker, start='2024-09-09', end='2024-09-20')

# getting 10days worth of stock market data.
#hist = ticker.history(period="10d")

'''
# Financials

financials = ticker.financials
#print("\nFinancials:")
#print(financials)

rows = len(financials)
a = np.empty(rows)
'''

#Display and save Graphs

plt.figure(figsize=(12, 6))
plt.plot(stock_data['Close'], label='Close Price')
plt.title('AAPL Stock Price')
plt.xlabel('Date')
plt.ylabel('closing prices')
plt.legend()
plt.show()