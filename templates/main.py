import datetime
import json
import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.exception_handler(404)
def custom_404(request, e):
    """
    Creates page for 404 errors.
    """
    return HTMLResponse("Page Not Found.")



bitcoins = {
    "transactions": [],
    "total_cost": 0,
}


def save_bitcoins():
    """Save bitcoin data to JSON file"""
    if not os.path.exists("data"):
        os.makedirs("data")
    with open("data/bitcoins.json", "w") as file:
        json.dump(bitcoins, file, indent=4)


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


load_bitcoins()


@app.get("/bitcoin", response_class=HTMLResponse)
def show_buy_bitcoin_form(request: Request):
    return templates.TemplateResponse("buy-bitcoin.html", {"request": request})


@app.post("/bitcoin", response_class=HTMLResponse)
async def buy_bitcoin(request: Request):
    """Process the form submission to fake-buy bitcoin"""
    form = await request.form()
    quant = form.get("quantity")
    quant = float(quant)
    price = get_bitcoin_price()
    total = price * quant
    total = round(total, 2)
    bitcoins["transactions"].append(
        {
            "quantity": quant,
            "price": price,
            "total": total,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
    )
    bitcoins["total_cost"] += total
    # bitcoins['total_cost_str'] = f'{str(total):,.2f}'

    save_bitcoins()

    # return templates.TemplateResponse(
    #     "bitcoin.html", {"request": request, "bitcoins": bitcoins}
    # )
    return RedirectResponse(url="/bitcoin/transactions", status_code=303)


@app.get("/bitcoin/transactions", response_class=HTMLResponse)
def show_all_bitcoin_transactions(request: Request):
    return templates.TemplateResponse(
        "bitcoin.html",
        {
            "request": request,
            "bitcoins": bitcoins,
        },
    )


@app.get("/find_stock_price")
async def find_stock_price(stock: str):
    """Find the price of a stock"""
    try:
        ticker = yf.Ticker(stock)
        info = ticker.info
        current_price = info.get("currentPrice")
    except Exception:
        current_price = 0
    return JSONResponse({"stock": stock.upper(), "price": f"{current_price:.2f}"})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)