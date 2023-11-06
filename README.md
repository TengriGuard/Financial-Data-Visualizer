# Financial Data Visualizer

This tool is designed to fetch and visualize financial data, providing a clear and interactive chart of stock prices over a specified period.

## Features

- Fetch historical data for any stock listed on Yahoo Finance.
- Visualize the closing prices with an interactive and scalable chart.
- Easy-to-use with command-line arguments for stock symbol and date range.

## Installation

Before running this script, you need to install the required Python packages. You can install these using pip:

```bash
pip install yfinance matplotlib pandas

Usage

Run the script with the -h option to view the help message:

bash

python finance_visualizer.py -h

To fetch and visualize data for a stock, run:

bash

python finance_visualizer.py --symbol [STOCK_SYMBOL] --start [START_DATE] --end [END_DATE]

Replace [STOCK_SYMBOL] with the symbol of the stock, [START_DATE] and [END_DATE] with the range of dates in YYYY-MM-DD format.
Example

bash

python finance_visualizer.py --symbol AAPL --start 2020-01-01 --end 2023-01-01

This will generate and display a plot of Apple Inc. (AAPL) stock prices from January 1, 2020, to January 1, 2023.
Contribution

Contributions, issues, and feature requests are welcome!

Feel free to check issues page.
License

Distributed under the MIT License. See LICENSE for more information.
