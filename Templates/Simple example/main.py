import uvicorn
from fastapi import FastAPI, Path, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI Starter", version="0.1.0")

# Allow frontend (e.g., Vite/React on port 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Models
# -----------------------------
class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

# -----------------------------
# In-memory "database"
# -----------------------------
inventory = {}

# -----------------------------
# Routes
# -----------------------------
@app.get("/", tags=["Health"])
def root():
    return {"message": "FastAPI starter is running 🚀"}

@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: int = Path(gt=0, description="The ID of the item you would like to view")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item not found.")
    return inventory[item_id]

@app.get("/items/by-name", tags=["Items"])
def get_item_by_name(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item name not found.")

@app.post("/items/{item_id}", tags=["Items"])
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists.")
    inventory[item_id] = item
    return item

@app.put("/items/{item_id}", tags=["Items"])
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    
    stored_item = inventory[item_id]

    if item.name is not None:
        stored_item.name = item.name
    if item.price is not None:
        stored_item.price = item.price
    if item.brand is not None:
        stored_item.brand = item.brand

    return stored_item

@app.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID does not exist.")
    del inventory[item_id]
    return {"success": f"Item {item_id} deleted."}

# -----------------------------
# Run the server
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
