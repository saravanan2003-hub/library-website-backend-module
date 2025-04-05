from fastapi import APIRouter, Request
from .user_service import UserService
from .user_schema import UserCreate, UserCredential, UserResponse
from util.auth import hash_password, verify_password, jwt_token_decrypt, jwt_token_encrypt, authenticate
from .user_validator import UserValidator

router = APIRouter()
user_service = UserService()

@router.get("/users/" ,response_model = list[UserResponse])
def get_users(request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    
    return user_service.get_all_user()


@router.get("/users/get_user_by_user_id", response_model = UserResponse)
def get_user_by_id(request:Request):
    user_dict = authenticate(request)
    user_id = user_dict["user_id"]
    
    return user_service.get_user_by_id(user_id)
    
@router.put("/users/update", response_model = UserResponse)
def update_user(user:UserCreate, request:Request):
    user_dict = authenticate(request)
    user_id = user_dict["user_id"]
    return user_service.update_user(user_id, user)


@router.get("/users/email/{email}", response_model = UserResponse)
def get_user_by_email(email:str):
    return user_service.get_user_by_email(email)

@router.post("/auth/signup/")
def register_user(user: UserCreate):
    user.password = hash_password(user.password)
    return user_service.create_user(user)

@router.post("/auth/signin/")
def verify_user(user:UserCredential):
    email = user.email
    plain_password = user.password
    db_user_details = user_service.get_user_by_email(email)
    db_email = db_user_details.email
    hashed_password = db_user_details.password
    UserValidator.validate_user_details(db_email, verify_password(plain_password,hashed_password))
    return jwt_token_encrypt(db_user_details)


@router.get("/token/{token}")
def decript_token(token):
    return jwt_token_decrypt(token)
    
     

