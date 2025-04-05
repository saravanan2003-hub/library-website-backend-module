from fastapi import APIRouter, Request
from .lending_service import HistoryService
from .lending_schema import BorrowCreate, BorrowStatus, BorrowResponse
from util.auth import authenticate
from modules.user.user_validator import UserValidator

router = APIRouter()
history_service = HistoryService()


@router.post("/lending/")
def create_history(history:BorrowCreate):
    return history_service.create_history(history)

@router.get("/lending/")
def get_history(request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.get_histroys()

@router.get("/lending/{borrow_id}")
def get_histroy_by_id(borrow_id:str, request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.get_history_by_id(borrow_id)

@router.get("/lending/user/{user_id}")
def get_histroy_by_user_id(user_id:str , request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.get_histroy_by_user_id(user_id)

@router.get("/lending/book/{book_id}")
def get_history_by_book_id(book_id:str, request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.get_histroy_by_book_id(book_id)

@router.patch("/lending/{borrow_id}")
def update_history(update_data:BorrowStatus, borrow_id:str, request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.update_histroy(update_data, borrow_id)

@router.delete("/lending/{borrow_id}")
def delete_histroy(borrow_id:str , request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return history_service.delete_histroy(borrow_id)