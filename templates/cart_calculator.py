from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/cart")
def cart_calculator():
    """
    Uses FastAPI to calculate the total price of purses added to customer's cart.
    """
    # Opens and loads local data.json file
    with open('data.json', 'r') as file:
        data = json.load(file)  # Reads JSON data from data.json file
        
    # Provides total price of purses added to customer's cart in U.S. Dollars
    total_price = float(data["bpi"]["USD"]["rate_float"])
    return {"total_price": total_price}
