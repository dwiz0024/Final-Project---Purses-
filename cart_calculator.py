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
    try:
        with open('data.json', 'r') as file:
            cart_data = json.load(file)
    except FileNotFoundError:
        return {"error": "Cart file not found."}
    except json.JSONDecodeError:
        return {"error": "Error reading cart data."}

    total_price = 0.0

    for item in cart_data["items"]:

        price = float(item.get("price", 0))
        quantity = int(item.get("quantity", 1))
        
        total_price += price * quantity

    return {"total_price": total_price}



def load_bitcoins():
    """Load bitcoin data from JSON file or create new if doesn't exist"""
    global bitcoins
    try:
        if os.path.exists("data/bitcoins.json"):
            with open("data/bitcoins.json", "r") as file:
                bitcoins = json.load(file)
        else:
            save_bitcoins()
    except json.JSONDecodeError:
        save_bitcoins()

