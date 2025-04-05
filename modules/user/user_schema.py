from pydantic import BaseModel, EmailStr
from uuid import UUID
from enum import Enum

class Role(str ,Enum):
    student = "student"
    admin = "admin"
   

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    role : Role = Role.student
    password: str
    
class UserResponse(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: EmailStr
    role: Role 
    
    class Config:
        from_attributes = True
        
class  UserCredential(BaseModel):
    email: str
    password: str
        

__all__  = ["UserCreate", "UserResponce"]