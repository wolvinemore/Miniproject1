### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

#imports
import os
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import time
import copy
from datetime import datetime, timedelta

if not os.path.exists("Charts"):
    os.mkdir("Charts")

# Get today's date
today = datetime.now()

# Calculate the date 10 days ago
ten_days_ago = today - timedelta(days=14)

# generate market data

tickers = (["AAPL","AMZN","V","GME","MSFT"])

# Adding Stock data for Mon-Fri Trading days
for ticker in tickers:
    data = yf.Ticker(ticker)
    hist = data.history(start=ten_days_ago, end=today)
    last10days = []
    for date in hist['Close'][:11]:
        last10days.append(date)

    # numpy to give the number of tickers
    a = np.array(last10days)
    b = np.array(data)


    # Displays graphs
    if len(last10days) == 10:
        a = np.array(last10days)
        maxlist = copy.copy(a)
        max_price = maxlist[-1]+10
        min_price = maxlist[0]-10

        plt.plot(a, label='Close Price')
        plt.title(f'{ticker} Stock Price')
        plt.xlabel('Dates', labelpad = 0)
        plt.ylabel('Closing prices')
        plt.axis((11, 1, min_price, max_price))
        plt.legend()
        plt.savefig(f'Charts\\{ticker}.png')

    else:
        print("Do mot have 10 days you only have {len(last10days)}")
