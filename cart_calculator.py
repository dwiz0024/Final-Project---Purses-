from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import json

app = FastAPI()

# Configure template directory
templates = Jinja2Templates(directory="templates")

# Mount a static directory for any CSS or JS files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    # This will render the HTML page when accessing the root endpoint
    return templates.TemplateResponse("index.html", {"request": request})

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

