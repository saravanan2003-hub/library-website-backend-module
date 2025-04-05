import jwt
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from pydantic_settings import BaseSettings 
from fastapi import Request, HTTPException
from sqlmodel import select

hashing = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_password(password: str):
    return hashing.hash(password)


def verify_password(plain_password, hashed_password):
    return hashing.verify(plain_password, hashed_password)


Algorithm = "HS256"

class SecretKey(BaseSettings):
    secret_key :str
    class Config:
        env_file = ".env"
        

secret_key = SecretKey()


def jwt_token_encrypt(UserDetial):
    payload={
        "first_name":UserDetial.first_name,
        "last_name":UserDetial.last_name,
        "email" : UserDetial.email,
        "role" : UserDetial.role,
        "user_id":str(UserDetial.user_id),
    }
    token=jwt.encode(payload,secret_key.secret_key,algorithm=Algorithm)
    return token

def jwt_token_decrypt(jwt_token):
    payload=jwt.decode(jwt_token,secret_key.secret_key,algorithms=Algorithm)
    return payload



def authenticate(request: Request):
    from modules.user.user_model import User, engine,Session #the reason to put  here is we cant able to import as a circlutae
    bearer_token=request.headers.get("Authorization")
    jwt_token=bearer_token.split(" ")[1]
    payload=jwt_token_decrypt(jwt_token)
    email=payload["email"]
    role = payload.get("role")
    with Session(engine) as session:
        user=session.exec(select(User).where(User.email==email)).first()
        if not user:
            raise HTTPException(status_code=401,detail="Unauthorized")
        
        return {"user_id": user.user_id, "role": role}















