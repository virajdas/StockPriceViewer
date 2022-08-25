import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
from mpl_finance import candlestick_ohlc

def main(ticker):
    ticker = ticker.upper()
    if len(ticker) > 4:
        print('INVALID TICKER')

    # TIME FRAME
    start_date = dt.datetime(2015, 1, 1)
    end_date = dt.datetime.now()

    # LOAD DATA
    data = web.DataReader(ticker, 'yahoo', start_date, end_date)

    # RESTRUCTURE DATA
    data = data[['Open', 'High', 'Low', 'Close']]
    data.reset_index(inplace=True)
    data['Date'] = data["Date"].map(matdates.date2num)

    # VISUALIZATION
    plot = plt.subplot()
    plot.grid(True)
    plot.set_axisbelow(True)
    plot.set_title(f"{ticker} Share Price", color='white')
    plot.set_facecolor('white')
    plot.figure.set_facecolor('#121212')
    plot.tick_params(axis='x', colors='white')
    plot.tick_params(axis='y', colors='white')
    plot.xaxis_date()

    candlestick_ohlc(plot, data.values, width=0.5, colorup='#00ff00')
    plt.show()

if __name__ == '__main__':
    main('aapl')