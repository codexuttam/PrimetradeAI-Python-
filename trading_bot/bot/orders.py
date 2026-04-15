from .client import BinanceFuturesClient
from .validators import validate_inputs
from .logging_config import logger

class OrderManager:
    def __init__(self, api_key=None, api_secret=None):
        self.client = BinanceFuturesClient(api_key, api_secret)

    def execute_order(self, symbol, side, order_type, quantity, price=None):
        """Validates and executes an order."""
        # Validate inputs
        errors = validate_inputs(symbol, side, order_type, quantity, price)
        if errors:
            for err in errors:
                logger.error(f"Validation Error: {err}")
            return {"success": False, "errors": errors}

        try:
            response = self.client.place_futures_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )
            return {"success": True, "data": response}
        except Exception as e:
            return {"success": False, "errors": [str(e)]}
