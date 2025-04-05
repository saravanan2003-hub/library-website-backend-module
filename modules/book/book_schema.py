from pydantic import BaseModel, HttpUrl
from uuid import UUID
from enum import Enum


class Status(str, Enum):
    available = "available"
    unavailable = " unavailable"

class BookCreate(BaseModel):
    book_name: str
    author: str
    description: str
    genre: str
    status: Status
    book_image: str
    
    
class BookResponse(BookCreate):
    book_id: UUID
    
    class Config:
        from_attributes = True
    
    

__all__ = ["BookCreate", "BookResponce"]
