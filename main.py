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

@app.get("/prodict/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product == products[id]:
            return products[id]
    return "Product Ont found"

@app.post("/product")
def add_product(request: Products):
    products.append(request)
    return products

@app.put("/product/{id}")
def update_product(id: int, product: Products):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product update succesfully" 
    return "Product Not found"

@app.delete("/product")
def delete_product(id: int):
    for product in products:
        if product.id == id:
            del product
            return "Product deleted"
    return "Product Not found"

# postgresql://postgres:IEQS64fTTKCWr6WN@db.umkfsgrvznsrcdsvgdzg.supabase.co:5432/postgres
