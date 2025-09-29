from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.items import Item, Items
from app.db import crud, models, database

router = APIRouter(
    prefix="/items",
    tags=["Items"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=Items)
def get_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return Items(items=items)

@router.post("/", response_model=Item)
def add_item(item: Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)
