import datetime
import json
import os
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cart = {
    "items": [],
    "total": 0,
}

def load_cart():
    """
    Loads cart data from JSON file or creates a new JSON file if one doesn't exist.
    """
    global cart
    try:
        if os.path.exists("data/cart.json"):
            with open("data/cart.json", "r") as file:
                cart = json.load(file)
        else:
            save_cart()
    except json.JSONDecodeError:
        save_cart()

def save_cart():
    """
    Saves cart data to JSON file.
    """
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data/cart.json", "w") as file:
        json.dump(cart, file, indent=4)

def load_products():
    """
    Returns products in a JSON file.
    """
    try:
        if os.path.exists("data/products.json"):
            with open("data/products.json", "r") as file:
                products = json.load(file)
                return products
    except json.JSONDecodeError:
        print("Wrong JSON data.")
        return None

products = load_products()

@app.get("/", response_class=HTMLResponse)
def read_main(request: Request):
    """
    Reads the main HTML page.
    """
    return templates.TemplateResponse(
        "index.html", {"request": request, "products": products}
    )

@app.get("/cart", response_class=HTMLResponse)
def show_cart(request: Request):
    """
    Uses the cart data to populate the cart.html page with the total price of products added.
    """
    # print(cart)
    return templates.TemplateResponse("cart.html", {"request": request, "cart": cart})

@app.post("/add-to-cart")
async def add_to_cart(request: Request):
    """
    Updates the total price as products are added to the cart.
    """
    data = await request.json()
    product_id = data.get("productId")
    product = next(
        (p for p in products["products"] if p["id"] == int(product_id)), None
    )
    if product:
        cart["items"].append(product)
    total = sum(item["price"] for item in cart["items"])
    cart["total"] = total
    print(cart)
    save_cart()
    return JSONResponse(content={"total": total})

@app.exception_handler(404)
async def custom_404(request: Request, e: HTTPException):
    """
    Uses FastAPI to create a custom page for 404 errors.
    """
    return HTMLResponse(
        content="<html><body><h1>Page Not Found</h1></body></html>", status_code=404
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
