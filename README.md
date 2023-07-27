# FYERS-CLI

FYERS-CLI is a command-line interface that allows you to interact with the FYERS trading platform. It provides various commands and options to perform different tasks, including order placement, order modification, order cancellation, fetching quotes, fetching order history, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands and Options](#commands-and-options)
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

The FYERS-CLI tool provides a convenient way to interact with the FYERS trading platform. You can use it to place orders, modify existing orders, cancel orders, fetch quotes and market depth, and retrieve order history. The various options available allow you to customize your orders according to your trading needs.

Note: The examples provided are for illustrative purposes and may need to be modified based on your specific use case.

For more information, refer to the [FYERS API documentation](https://api-docs.fyers.in/v1.0/docs/introduction).

---

Now, the installation section includes the step for installing dependencies using the `requirements.txt` file.
