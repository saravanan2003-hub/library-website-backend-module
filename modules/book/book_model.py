from sqlmodel import SQLModel, select, Field
from uuid import UUID, uuid4
from util.database import engine, Session
from .book_schema import BookCreate,  BookResponse , Status


class BookBase(SQLModel):
    book_name: str = Field(min_length=3)
    author: str = Field(min_length=3)
    genre: str
    description: str
    status: Status = Field(default=Status.available)
    book_image : str
    
class Book(BookBase, table = True):
    book_id: UUID = Field(primary_key=True, default_factory=uuid4)
    
    

class BookDAO:
    
    def create_book(self, book: BookCreate):
        with Session(engine) as session:
            db_book = Book(**book)
            session.add(db_book)
            session.commit()
            session.refresh(db_book)
            
        return db_book
    
    
    def get_books(self):
        with Session(engine) as session:
            db_books = session.exec(select(Book)).all()
        return db_books
    
    
    def get_book_by_id(self, book_id:UUID):
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.book_id == book_id)).first()
        return db_book
    
    
    def get_book_by_book_name(self, book_name: str):
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.book_name == book_name)).first()
        return db_book
    
    
    def get_book_by_author(self, author: str): 
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.author == author)).all()
        return db_book
    
    def get_book_by_genre(self, genre: str):
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.genre == genre)).all()
        return db_book
    
    
    def update_book(self, book_id:UUID, book:BookCreate):
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.book_id == book_id)).first()
            
            db_book.book_name = book.book_name
            db_book.author = book.author
            db_book.description = book.description
            db_book.genre = book.genre
            
            session.add(db_book)
            session.commit()
            session.refresh(db_book)
        return db_book
            
    
    def delete_book(self, book_id: UUID):
        with Session(engine) as session:
            db_book = session.exec(select(Book).where(Book.book_id == book_id)).first()
            session.delete(db_book)
            session.commit()
        return
    