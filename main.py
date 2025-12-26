from fastapi import FastAPI, Depends
from model import Products
from database import engine, SessionLocal
from sqlalchemy.orm import Session

import database_model

app = FastAPI()

# database connection
database_model.Base.metadata.create_all(bind = engine)

products = [
    Products(id=1, name = "Phone", description = "Ram 12GB, Rom 126GB", price = 120.2, quantity=2),
    Products(id = 2, name = "Laptop", description = "Ram 16GB, SSD 500GB", price = 600.2, quantity = 5)
]

# Making connection to db and close after used (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Products).all()
    return db_products


@app.get("/prodict/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if db_product:
        return db_product
    return "Product Not Found"


@app.post("/product")
def add_product(request: Products, db: Session = Depends(get_db)):
    db.add(database_model.Products(**request.model_dump()))
    db.commit()
    return db.query(database_model.Products).all()


@app.put("/product/{id}")
def update_product(id: int, product: Products, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product update succesfully" 
    return "Product Not found"


@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Products).filter(database_model.Products.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product deleted"
    return "Product Not found"
