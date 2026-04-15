# Binance Futures Trading Bot (Testnet)

A simplified Python trading bot designed to place Market, Limit, and Stop-Market orders on the Binance Futures Testnet (USDT-M).

## Features
- **Place Orders**: Supports MARKET, LIMIT, and STOP_MARKET orders.
- **Side Support**: BUY and SELL directions.
- **Robust CLI**: Built with `click` and `rich` for a clean user experience.
- **Validation**: Strict input validation for symbols, sides, types, quantities, and prices.
- **Logging**: Detailed logging of all API interactions and errors to `bot.log`.
- **Error Handling**: Graceful handling of network, API, and validation errors.

## Project Structure
```
trading_bot/
  bot/
    __init__.py
    client.py        # Binance client wrapper (Testnet configured)
    orders.py        # Order placement orchestration logic
    validators.py    # CLI & API input validation
    logging_config.py # Structured logging setup
  cli.py             # CLI entry point (Main interface)
  requirements.txt   # Dependencies
  .env.example       # Template for API credentials
  bot.log            # (Generated) Log file for tracking actions
```

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Binance Futures Testnet Account ([Register here](https://testnet.binancefuture.com))

### 2. Installation
Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

### 3. Configuration
Copy the `.env.example` file to `.env` and fill in your Testnet API credentials:
```bash
cp .env.example .env
```
Edit `.env`:
```text
BINANCE_API_KEY=your_testnet_key
BINANCE_API_SECRET=your_testnet_secret
```

## Usage Examples

### Place a Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 65000
```

### Place a Stop-Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_MARKET --quantity 0.001 --stop-price 70000
```

## Assumptions & Design Decisions
- **Testnet Focus**: The client is hardcoded to interact with the Binance Futures Testnet URL.
- **python-binance**: Used for its reliable wrapper around the Binance API.
- **Rich Output**: Integrated `rich` to provide a professional and readable CLI output.
- **Logging**: Rotating file handler (10MB) to ensure log files don't consume excessive disk space.
- **Time In Force**: LIMIT orders default to `GTC` (Good Till Cancelled).

## Requirements
- `python-binance`
- `python-dotenv`
- `click`
- `rich`
