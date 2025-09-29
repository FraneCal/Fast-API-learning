import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# -----------------------------
# Pydantic models (example)
# -----------------------------
class Item(BaseModel):
    name: str
    description: str | None = None

class Items(BaseModel):
    items: List[Item]

# -----------------------------
# App initialization
# -----------------------------
app = FastAPI(title="My FastAPI Project", version="0.1.0")

# Define allowed origins (frontend URLs)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],         # Allow all headers
)

# -----------------------------
# In-memory "database"
# -----------------------------
memory_db = {"items": []}

# -----------------------------
# Routes
# -----------------------------
@app.get("/", tags=["Health"])
def root():
    return {"message": "FastAPI project is running 🚀"}

@app.get("/items", response_model=Items, tags=["Items"])
def get_items():
    return Items(items=memory_db["items"])

@app.post("/items", response_model=Item, tags=["Items"])
def add_item(item: Item):
    memory_db["items"].append(item)
    return item

# -----------------------------
# Entry point
# -----------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
