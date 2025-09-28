# Following the instructions on this video: https://www.youtube.com/watch?v=-ykeT6kk4bk&t=1148s

from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# What kind of data structure does the URL endpoint accept when it is a type "Item"
# (look at create_item function)
class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None

inventory = {}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description="The ID of the item you would like to view"), gt=0):
    return inventory[item_id]

@app.get("/get-by-name")
def get_item(name: Optional[str] = None):
    # Loops through the list
    for item_id in inventory:
        # Looks if it matches the value which is written in the URL, if it does it returns it
        if inventory[item_id].name == name:
            return inventory[item_id]
    return {"Data": "Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}

    # One way of inserting items
    # inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}

    # Other way
    inventory[item_id] = item
    return inventory[item_id]