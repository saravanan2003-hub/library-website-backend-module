from fastapi import HTTPException, status
from uuid import UUID


class BookValidator:
    def validate_book_id(self, book_id:str):
        if not book_id:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Book Not Found")
        
    
    def validate_book_name(self, book_name:str):
        if not book_name:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Book Not Found")
        
        
    def validate_author(self, author:str):
        if not author:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Author Not Found")
        
    def validate_genre(self, genre:str):
        if not genre:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail = "Genre Not Found")