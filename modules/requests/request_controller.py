from fastapi import APIRouter, Request
from .request_service import RequestService
from .request_schema import RequestCreate, RequestResponse
from util.auth import authenticate
from modules.user.user_validator import UserValidator
from uuid import UUID


router = APIRouter()
request_service = RequestService()

@router.post("/requests/")
def create_request(request:RequestCreate):
    return request_service.create_request(request)

@router.get("/requests/")
def get_requests(request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return request_service.get_all_request()

@router.get("/requests/{request_id}" )
def get_request_by_id(request_id:UUID):
    return request_service.get_request_by_id(request_id)

@router.put("/requests/{request_id}" )  
def update_request(request_id:UUID, request:RequestCreate, request_token:Request):
    user_dict = authenticate(request_token)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return request_service.update_request(request_id, request)

@router.delete("/requests/{request_id}")
def delete_request(request_id:str , request:Request):
    authenticate(request)
    return request_service.delete_request(request_id)

@router.get("/requests/user/{user_id}")
def get_request_by_user_id(user_id:UUID,  request:Request):
    authenticate(request)
    return request_service.get_request_by_user_id(user_id)

@router.get("/requests/book/{book_id}")
def get_request_by_book_id(book_id:str, request:Request):
    authenticate(request)
    return request_service.get_request_by_book_id(book_id)