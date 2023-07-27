---

# FYERS-CLI

FYERS-CLI is a command-line interface that allows you to interact with the FYERS trading platform. It provides various commands and options to perform different tasks, including order placement, order modification, order cancellation, fetching quotes, fetching order history, and more. Additionally, it offers a live market data feature to keep you updated with real-time price changes.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands and Options](#commands-and-options)
- [Live Market Data](#live-market-data)
- [Examples](#examples)
- [Conclusion](#conclusion)

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd fyers-cli
```

2. Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Usage

The FYERS-CLI tool follows the general syntax:

```bash
fyers-cli <command> [options]
```

## Commands and Options

FYERS-CLI provides the following commands and options:

1. `--gen`: Generate a new authentication code and access token.

2. `<symbol> <product> <validity> [--qty <QTY> --type <TYPE> --buy/--sell]`: Place a new order.

3. `--modify <orderId> [--qty <QTY> --type <TYPE> --limitPrice <PRICE> --stopPrice <PRICE>]`: Modify an existing order.

4. `--quote <symbol>`: Fetch quotes and market depth.

5. `--history <orderID>|--history`: Retrieve specific order or order history for the current trading day.

6. `--cancel <orderID>`: Cancel an order.

### Options

FYERS-CLI supports various options for order placement and modification. Below are the available options and their descriptions:

- `--qty <QTY>`: Specify the quantity for the order.

- `--type <TYPE>`: Specify the order type. Supported values are "limit," "market," "stoporder," and "stoplimit."

- `--buy`: Include this option for a buy order.

- `--sell`: Include this option for a sell order.

- `--limitPrice <PRICE>`: Specify the limit price for limit and stoplimit orders.

- `--stopPrice <PRICE>`: Specify the stop price for stop and stoplimit orders.

- `--offlineOrder`: Include this option when placing After Market Orders (AMO) order.

- `--disclosed`: Specify the disclosed quantity for equity orders.

- `--stopLoss`: Specify the stop loss price for cover order and bracket order.

- `--takeProfit`: Specify the take profit price for bracket order.

### Choices & Descriptions

1. `<product>`: Specify the product type for the order. Supported values are "CNC," "INTRADAY," "MARGIN," "CO," and "BO."

2. `<validity>`: Specify the validity of the order. Supported values are "IOC" (Immediate or Cancel) and "DAY" (Valid till the end of the day).

3. `--offlineOrder`: Specify "True" for AMO orders and "False" for orders placed during market hours.

## Live Market Data

The FYERS-CLI also offers a live market data feature. It allows you to subscribe to real-time market data for a specific symbol. To use this feature, follow the steps below:

1. Ensure you have the necessary credentials by generating the authentication code and access token.

2. Open the `config/marketdata.conf` file and set the `symbol` to the desired trading symbol.

3. Run the live market data process using the command:

```bash
python live_market_data.py
```

You will start receiving real-time market data for the specified symbol, including price updates and other relevant information.

### How to Use Live Market Data

1. Ensure that you have completed the installation and have the required credentials.

2. Open the `config/marketdata.conf` file using a text editor.

3. Set the value of `symbol` to the trading symbol for which you want to receive live market data. For example, to track the NSE stock "SBIN-EQ," set the `symbol` as follows:

```json
{
  "symbol": "NSE:SBIN-EQ"
}
```

4. Save the `marketdata.conf` file.

5. Open a terminal or command prompt and navigate to the FYERS-CLI directory.

6. Run the live market data process using the following command:

```bash
python live_market_data.py
```

Now, you will receive real-time market data for the specified trading symbol. The CLI will continuously display the updated prices and other information in the terminal.

## Examples

Here are some examples of how to use the FYERS-CLI:

1. Placing a Limit Buy Order:

```bash
fyers-cli NSE:SBIN-EQ CNC DAY --qty 100 --type limit --buy
```

2. Placing a Market Sell Order:

```bash
fyers-cli NSE:SBIN-EQ CNC DAY --qty 50 --type market --sell
```

3. Modifying an Existing Order:

```bash
fyers-cli --modify 12345678 --qty 50 --type limit --limitPrice 305.50
```

4. Fetching Quotes and Market Depth:

```bash
fyers-cli --quote NSE:SBIN-EQ
```

5. Retrieving Order History:

```bash
fyers-cli --history 12345678
```

6. Canceling an Order:

```bash
fyers-cli --cancel 12345678
```

## Conclusion

The FYERS-CLI tool provides a convenient way to interact with the FYERS trading platform. You can use it to place orders, modify existing orders, cancel orders, fetch quotes and market depth, and retrieve order history. Additionally, the live market data feature keeps you updated with real-time price changes for a specified trading symbol.

Note: The examples provided are for illustrative purposes and may need to be modified based on your specific use case.

For more information, refer to the [FYERS API documentation](https://fyers.in/products/api/).

---

Now, the `readme.md` file includes detailed information about how to use the live market data feature in the FYERS-CLI.
