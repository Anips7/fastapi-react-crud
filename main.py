from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from models import Product  # Pydantic schema
from database import SessionLocal, engine
import database_models

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3002"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
database_models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------------
# GET ALL PRODUCTS
# ----------------------------
@app.get("/products", response_model=List[Product])
def get_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


# ----------------------------
# GET PRODUCT BY ID
# ----------------------------
@app.get("/products/{product_id}", response_model=Product)
def product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# ----------------------------
# CREATE PRODUCT
# ----------------------------
@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
def add_product(product: Product, db: Session = Depends(get_db)):

    # Check if ID already exists
    existing = db.query(database_models.Product).filter(
        database_models.Product.id == product.id
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Product ID already exists")

    new_product = database_models.Product(**product.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# ----------------------------
# UPDATE PRODUCT
# ----------------------------
@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, updated_product: Product, db: Session = Depends(get_db)):

    product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    # Do NOT update ID
    update_data = updated_product.model_dump(exclude={"id"})

    for key, value in update_data.items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


# ----------------------------
# DELETE PRODUCT
# ----------------------------
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(database_models.Product).filter(
        database_models.Product.id == product_id
    ).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return
