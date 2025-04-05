from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from modules.user.user_schema import UserResponse
from modules.book.book_schema import BookResponse

class request_status(str, Enum):
    pending = "pending"
    accepted = "accepted"
    rejected = "rejected"
    
class RequestCreate(BaseModel):
    user_id: UUID
    book_id: UUID
    status: request_status = request_status.pending
    
class RequestResponse(BaseModel):
    request_id: UUID
    user : UserResponse
    book : BookResponse
    status: request_status
    
    
    class Config:
        from_attributes = True