from sqlmodel import SQLModel , select ,Field
from fastapi import HTTPException, status
from uuid import UUID, uuid4
from datetime import datetime ,timezone
from util.database import engine ,Session
from .user_schema import UserCreate, Role, UserResponse
from util.auth import jwt_token_encrypt
from typing import Optional

def generate_timestamp():
    return datetime.now(timezone.utc)


class UserBase(SQLModel):
    __tablename__= "user"
    first_name:str = Field(min_length = 3)
    last_name:str = Field(min_length = 3)
    email:str = Field(unique = True)
    password:str = Field(min_length = 8)
    role : Role = Field(default = Role.student) 
    

class User(UserBase, table = True):
    user_id: UUID = Field(primary_key=True, default_factory=uuid4)
    created_at: datetime = Field(default_factory=generate_timestamp)
    updated_at: Optional[datetime]
    
    
    
class userDAO:
    
    def create_user(self, user:UserCreate):
        with Session(engine) as session:
            db_user = User(**user.dict())
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
        return jwt_token_encrypt(db_user)
            
    def get_users(self):
        with Session(engine) as session:
            db_user = session.exec(select(User)).all()
        return db_user
    
    def get_user_by_id(self,user_id: UUID):
        with Session(engine) as session:
            db_user = session.exec(select(User).where(User.user_id == user_id)).first()
        return db_user
    
    def update_user(self,user_id:UUID, user:UserCreate):
        with Session(engine) as session:
            db_user = session.exec(select(User).where(User.user_id == user_id)).first()
            
            db_user.first_name = user.first_name
            db_user.last_name = user.last_name
            db_user.updated_at = generate_timestamp()
            
            session.add(db_user)
            session.commit()
            session.refresh(db_user)
        return db_user
    
    def get_user_by_email(self, email:str):
        with Session(engine) as session:
            db_user = session.exec(select(User).where(User.email == email)).first()
            if not db_user:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Details Not Found")
        return db_user