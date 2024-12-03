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
    Uses FastAPI to calculate the total price of purses added to the customer's cart.
    """
    # Opens and loads local data.json file
    with open('data.json', 'r') as file:
        data = json.load(file)  # Reads JSON data from data.json file
        
    # Provides total price of purses added to customer's cart in U.S. Dollars
    total_price = float(data["bpi"]["USD"]["rate_float"])
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

