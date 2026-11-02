from menu import MENU


def add_to_cart(cart, item, quantity=1):
    if item not in MENU:
        raise ValueError(f"'{item}' is not on the menu")
    if quantity <= 0:
        raise ValueError("quantity must be greater than zero")
    cart[item] = cart.get(item, 0) + quantity
    return cart
