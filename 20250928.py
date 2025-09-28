# Following the instructions on this video: https://www.youtube.com/watch?v=-ykeT6kk4bk&t=1148s

from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# What kind of data structure does the URL endpoint accept when it is a type "Item"
# (look at create_item function)
class Item(BaseModel):
    name:str
    price: float
    brand: Optional[str] = None

# Create this new class so we can only update one thing e.g. name or price
# otherwise we would have to update all values
class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# Instead of using this empty dictionary, use an actual database
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
    raise HTTPException(status_code = 404, detail="Item name not found.")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    # Check if the ID exists, if not return this message
    if item_id in inventory:
        raise HTTPException(status_code = 400, detail="Item ID already exists.")

    # One way of inserting items
    # inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}

    # Other way; create a new item based on the input
    inventory[item_id] = item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    # Check if the ID exists, if not return this message
    if item_id not in inventory:
        raise HTTPException(status_code = 404, detail="Item ID does not exists.")
    
    # Update only the name
    if item.name != None:
        inventory[item_id].name = item.name

    # Update only the price
    if item.price != None:
        inventory[item_id].price = item.price

    # Update only the brand
    if item.brand != None:
        inventory[item_id].brand = item.brand
    
    return inventory[item_id]

@app.delete("/delete-item")
def delete_update(item_id: int):
    # Check if the ID exists, if not return this message
    if item_id not in inventory:
        raise HTTPException(status_code = 404, detail="Item ID does not exists.")
    
    # If it does delete it
    del inventory[item_id]

    return {"Success": "Item deleted!"}
