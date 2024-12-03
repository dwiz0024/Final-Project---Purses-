from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import json

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})

@app.get("/cart")
def cart_calculator():
    """
    Calculates the total price of items in the cart.
    """
    # Opens and loads the cart data (cart.json containing the items and prices)
    try:
        with open('cart.json', 'r') as file:
            cart_data = json.load(file)
    except FileNotFoundError:
        return {"error": "Cart file not found."}
    except json.JSONDecodeError:
        return {"error": "Error reading cart data."}
    
    # Initialize total price variable
    total_price = 0.0

    # Iterate over cart items and calculate total price
    for item in cart_data["items"]:
        # Assuming each item has a price and quantity
        price = float(item.get("price", 0))
        quantity = int(item.get("quantity", 1))
        
        # Add the price of this item to the total, considering its quantity
        total_price += price * quantity

    # Return the total price
    return {"total_price": total_price}
