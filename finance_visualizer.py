import yfinance as yf
import matplotlib.pyplot as plt
import argparse

def get_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def visualize_data(data, ticker):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Close'], label=f'Closing Price of {ticker}')
    plt.title(f'Historical Price Data of {ticker}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Financial Data Visualizer')
    parser.add_argument('--symbol', type=str, required=True, help='The symbol of the stock/crypto to visualize e.g. AAPL')
    parser.add_argument('--start', type=str, required=True, help='The start date in YYYY-MM-DD format')
    parser.add_argument('--end', type=str, required=True, help='The end date in YYYY-MM-DD format')
    
    args = parser.parse_args()

    stock_data = get_data(args.symbol, args.start, args.end)
    visualize_data(stock_data, args.symbol)
