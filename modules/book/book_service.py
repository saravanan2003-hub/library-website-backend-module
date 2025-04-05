from .book_model import BookDAO
from .book_schema import BookCreate
from .book_validator import BookValidator
from uuid import UUID


class BookService:
    def book_create(self, book_data:BookCreate):
        book = BookDAO.create_book(self, book_data)
        return book
    
    def get_books(self):
        books = BookDAO.get_books(self)
        return books
    
    def get_book_by_id(self, book_id:str):
        BookValidator.validate_book_id(self, book_id)
        book = BookDAO.get_book_by_id(self, book_id)
        return book
    
    def get_book_by_book_name(self, book_name:str):
        BookValidator.validate_book_name(self, book_name)
        book = BookDAO.get_book_by_book_name(self, book_name)
        return book
    
    def get_book_by_author(self, author:str):
        BookValidator.validate_author(self, author)
        book = BookDAO.get_book_by_author(self, author)
        return book
    
    def get_book_by_genre(self, genre:str): 
        BookValidator.validate_genre(self, genre)
        book = BookDAO.get_book_by_genre(self, genre)
        return book
    
    def update_book(self, book_id:str, book_data:book_create):
        BookValidator.validate_book_id(self, book_id)
        book = BookDAO.update_book(self, book_id, book_data)
        return book
    
    def delete_book(self, book_id:str):
        BookValidator.validate_book_id(self, book_id)
        book = BookDAO.delete_book(self, book_id)
        return book
     
            