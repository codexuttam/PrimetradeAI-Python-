def validate_inputs(symbol, side, order_type, quantity, price):
    """Basic validation for trading inputs."""
    errors = []
    
    if not symbol or not isinstance(symbol, str):
        errors.append("Symbol must be a non-empty string.")
    
    if side.upper() not in ['BUY', 'SELL']:
        errors.append("Side must be either 'BUY' or 'SELL'.")
        
    if order_type.upper() not in ['MARKET', 'LIMIT']:
        errors.append("Order type must be either 'MARKET' or 'LIMIT'.")
        
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
                
    return errors
