### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

#Imports
import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

if not os.path.exists("Charts"):
    os.mkdir("Charts")

# generate market data

tickers = (["AAPL","AMZN","V","GME","MSFT"])

# Adding Stock data for Mon-Fri Trading days
for ticker in tickers:
    stock_data = yf.download(ticker, start='2024-09-09', end='2024-09-20')


    # numpy to give the number of tickers
    a = np.empty(len(tickers))
    b = np.array(stock_data)
    print(b)

    # Displays graphs
    plt.figure(figsize=(18, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.title(f'{ticker} Stock Price')
    plt.xlabel('Date', labelpad = 0)
    plt.ylabel('closing prices')
    plt.legend()
    plt.show()
    plt.savefig(f'Charts\\{ticker}.png')


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
