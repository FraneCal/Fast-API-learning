from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine, Base
import models

Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    brand: str

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500", "http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

inventory = {
    1: {
        "name": "banana",
        "price": 2.99,
        "brand": "regular"
    },
    2: {
            "name": "apple",
            "price": 1.79,
            "brand": "crazy"
        }
}

@app.get("/")
def home():
    return {"Detail": "This is the homepage."}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    if item_id not in inventory:
        return {"Detail": "Item not found."}

    return inventory[item_id]

@app.get("/all-items")
def get_all_items():
    return inventory

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    # Check if the item exists in the database
    if item_id not in inventory:
        # If it doesn't, add it to the item_id place with the value item (Base model defined above)
        inventory[item_id]=item
        return inventory[item_id]

    return {"Detail": "Item already exists."}

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    # Check if the item exists in the database
    if item_id in inventory:
        # If the name value is not None (which means user has entered some value) update it
        if item.name is not None:
            inventory[item_id]["name"] = item.name

        # If the price value is not None (which means user has entered some value) update it
        if item.price is not None:
            inventory[item_id]["price"] = item.price

        # If the brand value is not None (which means user has entered some value) update it
        if item.brand is not None:
            inventory[item_id]["brand"] = item.brand

        return inventory[item_id]

    return {"Detail": "Item doesn't exists."}

@app.delete("/delete-item")
def delete_item(item_id: int):
    pass