from sqlalchemy.orm import Session
from app.db import models
from app.schemas.items import Item

def get_items(db: Session):
    return db.query(models.Item).all()

def create_item(db: Session, item: Item):
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
