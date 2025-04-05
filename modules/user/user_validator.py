from fastapi import HTTPException, status
from uuid import UUID

class UserValidator:
    def validate_user_id(self, user_id: str):
        if not user_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Not Found")
        
    
    
    def validate_email(self, email:str):
        if not email:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Enter Your Authorized Email")
    
    
    def validate_user_details(email, password):
        if not email or password != True:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail= "User Details Not Found")


    def validate_user_role(role):
        if role != "admin":
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Access denied. Admins only")