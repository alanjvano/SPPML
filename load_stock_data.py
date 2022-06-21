import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import argparse
import json

# data = yf.download(tickers='TSLA', period='5y', interval='1d')
# print(data)

# tmp = data.iloc[:,1].values
# plt.plot(tmp)
# plt.show()

if __name__ == '__main__':
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--stocks', type=str, required=True)
    args = parser.parse_args()

    with open(args.stocks) as stock_file:
        json_data = json.load(stock_file)
    
    stock_names = json_data['stock_names']
    print(stock_names)

    data = yf.download(tickers=' '.join(stock_names), period='1y', interval='1d')
    print(data.columns)
