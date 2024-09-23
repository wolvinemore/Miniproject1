### INF601 - Advanced Programming in Python
### Kadin Heacock
### Miniproject1

#Imports
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# generate market data

ticker_symbol = "AAPL"

ticker = yf.Ticker(ticker_symbol)

# getting 10days worth of stock market data.
hist = ticker.history(period="10d")

print(hist)

# Financials

financials = ticker.financials
#print("\nFinancials:")
#print(financials)

rows = len(financials)
a = np.empty(rows)


'''
#Display and save Graphs
plt.plot(a)
plt.ylabel('Value')
plt.show()
'''