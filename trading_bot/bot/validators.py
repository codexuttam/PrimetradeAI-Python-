def validate_inputs(symbol, side, order_type, quantity, price, stop_price=None):
    """Basic validation for trading inputs."""
    errors = []
    
    if not symbol or not isinstance(symbol, str):
        errors.append("Symbol must be a non-empty string.")
    
    if side.upper() not in ['BUY', 'SELL']:
        errors.append("Side must be either 'BUY' or 'SELL'.")
        
    if order_type.upper() not in ['MARKET', 'LIMIT', 'STOP_MARKET']:
        errors.append("Order type must be one of: MARKET, LIMIT, STOP_MARKET.")
        
    try:
        qty_val = float(quantity)
        if qty_val <= 0:
            errors.append("Quantity must be greater than zero.")
    except (ValueError, TypeError):
        errors.append("Quantity must be a valid number.")
        
    if order_type.upper() == 'LIMIT':
        if price is None:
            errors.append("Price is required for LIMIT orders.")
        else:
            try:
                price_val = float(price)
                if price_val <= 0:
                    errors.append("Price must be greater than zero.")
            except (ValueError, TypeError):
                errors.append("Price must be a valid number.")

    if order_type.upper() == 'STOP_MARKET':
        if stop_price is None:
            errors.append("Stop Price is required for STOP_MARKET orders.")
        else:
            try:
                stop_val = float(stop_price)
                if stop_val <= 0:
                    errors.append("Stop Price must be greater than zero.")
            except (ValueError, TypeError):
                errors.append("Stop Price must be a valid number.")
                
    return errors
