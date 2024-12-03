import os
import json

def save_total_price():
    """
    Defines an empty cart json file, which will be populated as customers add items to their cart.
    """
    cart_data = {"items": []}
    with open("data/cart_data.json", "w") as file:
        json.dump(cart_data, file)

def cart_calculator():
    """
    Calculates the total price of items in the cart.
    """
    try:
        if os.path.exists("data/cart_data.json"):
            with open("data/cart_data.json", "r") as file:
                cart_data = json.load(file)

            if "items" in cart_data and isinstance(cart_data["items"], list):
                total_price = 0.0
                for item in cart_data["items"]:
                    price = item.get("price", 0.0)
                    quantity = item.get("quantity", 1)
                    total_price += price * quantity
                
                return {"total_price": total_price}

            else:
                # Initializes an empty cart if the file is empty or in the wrong format
                save_total_price()
                return {"total_price": 0.0}

        else:
            # Initializes an empty cart if the file does not exist
            save_total_price()
            return {"total_price": 0.0}

    except json.JSONDecodeError:
        # Resets cart in the case of an error
        save_total_price()
        return {"total_price": 0.0}
