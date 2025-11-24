import sys

def format_product_info(product_id: str, name: str, quantity: int, price: float) -> str:
    """
    Create a human-readable summary of product details.
    """
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")
    if price < 0:
        raise ValueError("Price cannot be negative.")

    return (
        "Product Information:\n"
        f"ID      : {product_id}\n"
        f"Name    : {name}\n"
        f"Quantity: {quantity}\n"
        f"Price   : ${price:.2f}"
    )


if __name__ == "__main__":
    # Expecting: python product.py <id> <name> <quantity> <price>
    if len(sys.argv) != 5:
        print("Usage: python product.py <product_id> <name> <quantity> <price>")
        sys.exit(1)

    product_id = sys.argv[1]
    name = sys.argv[2]
    quantity = int(sys.argv[3])
    price = float(sys.argv[4])

    print(format_product_info(product_id, name, quantity, price))
