from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    id: int | None = None
    name: str
    description: Optional[str] = None

class Items(BaseModel):
    items: List[Item]
