from fastapi import FastAPI
from model import Products

app = FastAPI()

@app.get("/")
def greet():
    return "Hello, World!"

products = [
    Products(id=1, name = "Phone", description = "Ram 12GB, Rom 126GB", price = 120.2, quantity=2),
    Products(id = 2, name = "Laptop", description = "Ram 16GB, SSD 500GB", price = 600.2, quantity = 5)
]

@app.get("/products")
def get_all_products():
    return products
