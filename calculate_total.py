from cart import add_to_cart
from menu import MENU


def main():
    cart = {}
    add_to_cart(cart, "burger", 2)
    add_to_cart(cart, "fries", 1)
    add_to_cart(cart, "cola", 2)

    total = 0
    for item, qty in cart.items():
        line = MENU[item] * qty
        total += line
        print(f"{item:<8} x{qty}  = {line:>7.2f}")

    print("-" * 22)
    print(f"ORDER TOTAL     = {total:>7.2f}")
    assert total == 420.0, "Unexpected order total"


if __name__ == "__main__":
    main()
