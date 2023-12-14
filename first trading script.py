# HANIF TRADING

import pandas as pd
import numpy as np
import yfinance as yf
import backtrader as bt
import matplotlib.pyplot as mplot
from scipy.optimize import curve_fit

# Collect AAPL historical price data
aapl = yf.download("BX", start="2023-11-6", end="2023-12-13", interval = '1h')

# Print the column names to verify the changes
#print(aapl.head())


closeprice = aapl[['Adj Close']]
openprice = aapl[['Open']]
highprice = aapl[['High']]

ema = aapl['Adj Close'].ewm(span=3, adjust=False).mean()



mplot.plot(aapl.index, closeprice, label='Closing Price')
mplot.plot(aapl.index, ema, label='Moving average')
mplot.legend()
mplot.show()

"""# Customize the plot
mplot.plot(aapl['Adj Close'])
mplot.xlabel('Date')
mplot.ylabel('Price')
mplot.title('AAPL')
  # Add legend to distinguish between series
"""



