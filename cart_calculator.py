import os
import json

def save_total_price():
    # You should define this function to handle the saving of an empty cart or default cart data
    cart_data = {"items": []}  # Default empty cart, can be adjusted as needed
    with open("data/data.json", "w") as file:
        json.dump(cart_data, file)

def cart_calculator():
    """
    Calculates the total price of items in the cart.
    """
    try:
        if os.path.exists("data/data.json"):
            with open("data/data.json", "r") as file:
                cart_data = json.load(file)

            # Ensure we have items in the cart, and calculate the total price
            if "items" in cart_data and isinstance(cart_data["items"], list):
                total_price = 0.0
                for item in cart_data["items"]:
                    # Assuming each item has 'price' and 'quantity'
                    price = item.get("price", 0.0)
                    quantity = item.get("quantity", 1)
                    total_price += price * quantity
                
                return {"total_price": total_price}

            else:
                # In case the cart is empty or not in expected format
                save_total_price()
                return {"total_price": 0.0}

        else:
            # If the file doesn't exist, initialize with an empty cart
            save_total_price()
            return {"total_price": 0.0}

    except json.JSONDecodeError:
        # In case the JSON is malformed, reset the cart to a safe state
        save_total_price()
        return {"total_price": 0.0}
