from .lending_model import HistoryDAO
from .lending_schema import BorrowCreate, BorrowStatus
from uuid import UUID
from modules.user.user_validator import UserValidator
from modules.book.book_validator import BookValidator
from .lending_validator import LendingValitador

class HistoryService:
    
    def create_history(self, history_data: BorrowCreate):
        history = HistoryDAO.create_history(self, history_data)
        return history
    
    def get_histroys(self):
        historys = HistoryDAO.get_historys(self)
        return historys
    
    def get_history_by_id(self, borrow_id:str):
        LendingValitador.validate_borrow_id(borrow_id)
        history = HistoryDAO.get_history_by_id(self, borrow_id)
        return history
    
    def get_histroy_by_user_id(self, user_id:str):
        UserValidator.validate_user_id(user_id)
        histroy = HistoryDAO.get_history_by_user_id(self, user_id)
        return histroy
    
    def get_histroy_by_book_id(self, book_id:str):
        BookValidator.validate_book_id(book_id)
        histroy = HistoryDAO.get_history_by_book_id(self, book_id)
        return histroy
    
    def update_histroy(self, update_data:BorrowStatus, borrow_id:str):
        LendingValitador.validate_borrow_id(borrow_id)
        histroy = HistoryDAO.update_status(self, update_data, borrow_id)
        return histroy
    
    def delete_histroy(self, borrow_id:str):
        LendingValitador.validate_borrow_id(borrow_id)
        histroy =HistoryDAO.delete_history(self, borrow_id)
        return histroy
    