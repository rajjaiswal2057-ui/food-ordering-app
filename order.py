def calculate_order_total(subtotal, discount_percent=0):
    if not isinstance(subtotal, (int, float)) or isinstance(subtotal, bool):
        raise TypeError("subtotal must be a number")
    if subtotal < 0:
        raise ValueError("subtotal cannot be negative")
    if not 0 <= discount_percent <= 100:
        raise ValueError("discount_percent must be between 0 and 100")
    return round(subtotal * (1 - discount_percent / 100), 2)
