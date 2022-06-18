import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download(tickers='TSLA', period='5y', interval='1d')
print(data)

tmp = data.iloc[:,1].values
plt.plot(tmp)
plt.show()