from fastapi import HTTPException
from uuid import UUID

class RequestValidator:
    
    def validate_request_id(self, request_id: UUID):
        if not request_id:
            raise HTTPException(status_code=400, detail="Request Not Found")
        
    def validate_user_id(self, user_id: UUID):
        if not user_id:
            raise HTTPException(status_code=400, detail="User Not Found")
        
        
    def validate_book_id(self, book_id: UUID):
        if not book_id:
            raise HTTPException(status_code=400, detail="Book Not Found")
        
    def validate_request_status(self, status: str):
        if status not in ["pending", "accepted", "rejected"]:
            raise HTTPException(status_code=400, detail="Invalid Status")
        
    