import argparse
import json
import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
from ipdb import set_trace

# data = yf.download(tickers='TSLA', period='5y', interval='1d')
# print(data)

# tmp = data.iloc[:,1].values
# plt.plot(tmp)
# plt.show()

if __name__ == '__main__':
    # parse input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--stocks', type=str, required=True)
    parser.add_argument('--period', type=str, default='1y')
    parser.add_argument('--interval', type=str, default='1d')
    parser.add_argument('--feature', type=str, default='Close')
    parser.add_argument('--sample_len', type=int, default=30)
    parser.add_argument('--label_len', type=int, default=1)
    parser.add_argument('--samples_per_stock', type=int, default=5)
    parser.add_argument('--save_dir', type=str, default='./data')
    args = parser.parse_args()

    # load list of stock names
    with open(args.stocks) as stock_file:
        json_data = json.load(stock_file)
    
    stock_names = json_data['stock_names']
    print(stock_names)

    # retrieve data
    data = yf.download(tickers=' '.join(stock_names), 
                        period=args.period, 
                        interval=args.interval)
    set_trace()
    print(data.columns)
    print(type(data))

    out_data = {each: [None, None] for each in stock_names}
    for stock in stock_names:
        stock_data = data[args.feature][stock].values
        out_data[stock][0] = np.zeros((args.samples_per_stock, args.sample_len))
        out_data[stock][1] = np.zeros((args.samples_per_stock, args.label_len))

        inds = np.random.choice(len(stock_data)-(args.label_len + args.sample_len), 
                                args.samples_per_stock,
                                replace=False)
        for i in range(args.samples_per_stock):
            out_data[stock][0][i] = stock_data[inds[i]:inds[i]+args.sample_len]
            out_data[stock][1][i] = stock_data[inds[i]+args.sample_len:inds[i]+args.sample_len+args.label_len]

    set_trace()

