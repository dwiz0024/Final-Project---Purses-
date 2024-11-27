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
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the product elements in the page (you may need to adjust these selectors)
    products = soup.find_all('div', class_='product-item')  # Adjust the class name

    purse_list = []
    
    for product in products:
        # Extract product details (you may need to adjust the HTML structure based on the website)
        name = product.find('h2', class_='product-title').text.strip()  # Adjust tag/class
        price = product.find('span', class_='price').text.strip()  # Adjust tag/class
        image_url = product.find('img')['src']  # Extract image URL

        purse_list.append(Product(name=name, price=price, image_url=image_url))

    return purse_list

# Returns purse data
@app.get("/", response_model=List[Product])
async def root():
    purses = get_purses()
    return purses
