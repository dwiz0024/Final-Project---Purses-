from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Defines a Pydantic model for purse details
class Product(BaseModel):
    name: str
    price: str
    image_url: str

# Pulls purses from Michael Kors website
def get_purses():
    url = 'https://www.michaelkors.com/women/handbags/'
    response = requests.get(url)
    
    # Returns an empty list, if the request fails
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Finds all products by class name
    products = soup.find_all('div', class_='product-item')

    purse_list = []
    
    for product in products:
        # Extracts purse details from Michael Kors website
        name_tag = product.find('h2', class_='product-title')
        price_tag = product.find('span', class_='price')
        image_tag = product.find('img')

        # Ensures the purse details exist before extracting them
        if name_tag and price_tag and image_tag:
            name = name_tag.text.strip()
            price = price_tag.text.strip()
            image_url = image_tag['src']

            purse_list.append(Product(name=name, price=price, image_url=image_url))

    return purse_list

# FastAPI route to get purses
@app.get("/", response_model=List[Product])
async def root():
    purses = get_purses()
    return purses
