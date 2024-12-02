import json
import urllib.request


def cart_calculator():
    """
    Calculates total price of items (purses) added to customer's cart.
    """
    URL = 
    with urllib.request.urlopen(URL) as response:
        data = response.read()
        data = json.loads(data)
        price_in_usd = float(data["bpi"]["USD"]["rate_float"])
        return price_in_usd


def main():
    print(cart_calculator())


if __name__ == "__main__":
    main()
