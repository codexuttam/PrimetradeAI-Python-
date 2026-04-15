import os
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceOrderException
from .logging_config import logger
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self, api_key=None, api_secret=None, testnet=True):
        self.api_key = api_key or os.getenv('BINANCE_API_KEY')
        self.api_secret = api_secret or os.getenv('BINANCE_API_SECRET')
        self.testnet = testnet
        
        if not self.api_key or not self.api_secret:
            logger.error("API Key or Secret missing. Please set them in .env file.")
            raise ValueError("API Key and Secret are required.")

        # Initialize client for Futures
        self.client = Client(self.api_key, self.api_secret, testnet=self.testnet)
        
        # Change base url for futures testnet specifically if needed, 
        # though python-binance handled it with testnet=True for spot.
        # For Futures Testnet, we often need to set the base URL explicitly or use specific methods.
        if self.testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi/v1'
            logger.info("Initialized Binance Futures Client on TESTNET")
        else:
            logger.info("Initialized Binance Futures Client on MAINNET")

    def place_futures_order(self, symbol, side, order_type, quantity, price=None, stop_price=None):
        """
        Places a futures order.
        :param symbol: e.g. 'BTCUSDT'
        :param side: 'BUY' or 'SELL'
        :param order_type: 'MARKET', 'LIMIT', or 'STOP_MARKET'
        :param quantity: float/str quantity
        :param price: float/str price (required for LIMIT)
        :param stop_price: float/str stop price (required for STOP_MARKET)
        """
        try:
            params = {
                'symbol': symbol.upper(),
                'side': side.upper(),
                'type': order_type.upper(),
                'quantity': quantity
            }
            
            if order_type.upper() == 'LIMIT':
                if not price:
                    raise ValueError("Price is required for LIMIT orders")
                params['price'] = price
                params['timeInForce'] = 'GTC'
                
            elif order_type.upper() == 'STOP_MARKET':
                if not stop_price:
                    raise ValueError("Stop Price is required for STOP_MARKET orders")
                params['stopPrice'] = stop_price
            
            logger.info(f"Sending order request: {params}")
            
            response = self.client.futures_create_order(**params)
            
            logger.info(f"Order received response: {response}")
            return response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e.message} (Code: {e.code})")
            raise e
        except BinanceOrderException as e:
            logger.error(f"Binance Order Error: {e.message}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected Error: {str(e)}")
            raise e
