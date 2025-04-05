from fastapi import HTTPException, status
from uuid import UUID

class LendingValitador:
    
    def validate_borrow_id(borrow_id :UUID):
        if not borrow_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="History Not Found")