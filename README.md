# SPPML

The objective of the SPPML (Stock Performance Prediction with Machine Learning) project is to develop a platform that can predict the future performance of a stock based on its metrics and past performance.  Some specific goals for this library are as follows:
1. develop a flexible framework for generating data for training
2. implement several learning methods for prediction (neural nets, lstm, etc.)
3. use an api to automatically buy and sell stocks based on predictions (and hopefully "beat" the market)

## Generating Data

Perhaps the most challenging aspect of the project will be generating useful data to train on.  There exists huge amount of information for any stock on the market which is easily obtainable.  However, an open question is what information will actually contribute towards a better model and what is just noise.  Some questions that could be posed are:
- What time frame of data should be considered (are there any benefits to including longterm data or should there be some weighting to encourage the model to use recent data)?
- What types of time series data should be used? Should opening, closing, high, and/or low prices, and/or volume traded be considered.
- What derived metrics if any from the raw market data should be used?  These could moving average, EPI, fundamental stocks performance indicators, etc.
- What generic metrics about the company could be included?  These could include a large ramge of factors such as company size, when it pays out dividends, what market category it is in, etc.

First raw data must be retrieved.  Stock data is retrieved using [Yahoo! Finance's API](https://pypi.org/project/yfinance/) for python.  Inputs to retrieve data can 



