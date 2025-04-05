from pydantic import BaseModel
from uuid import UUID
from enum import Enum

class Status(str, Enum):
    borrow = "borrow"
    returned = "returned"
    request = "request" 
    
class BorrowCreate(BaseModel):
    user_id: UUID
    book_id: UUID
    
class BorrowResponse(BorrowCreate):
    borrow_id : UUID 
    status : Status
    
    class Config:
        from_attributes = True
        
class BorrowStatus(BaseModel):
    status: Status
    
        
__all__ = ["BorrowCreate", "BorrowResponce", "BorrowStatus"]