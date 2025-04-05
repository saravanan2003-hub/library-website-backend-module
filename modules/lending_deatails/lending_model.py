from sqlmodel import SQLModel, select, Field
from uuid import UUID, uuid4
from datetime import datetime
from modules.user.user_model import generate_timestamp
from util.database import Session, engine
from .lending_schema import BorrowCreate, Status, BorrowStatus, BorrowResponse
from typing import Optional
from modules.user.user_model import User
from modules.book.book_model import Book
from modules.user.user_schema import UserResponse
from modules.book.book_schema import BookResponse

class BorrowBase(SQLModel):
    user_id:UUID = Field(foreign_key="user.user_id")
    book_id:UUID = Field(foreign_key="book.book_id")
    status: Status = Field(default="request")
    
class History(BorrowBase, table = True):
    borrow_id:UUID = Field(primary_key=True, default_factory=uuid4)
    borrowed_at:datetime = Field(default_factory=generate_timestamp)
    returned_at: Optional[datetime]
    
class HistoryDAO:
    
    def create_history(self, history:BorrowCreate):
        with Session(engine) as session:
            db_history = History(**history.dict())
            session.add(db_history)
            session.commit()
            session.refresh(db_history)
        return db_history
    
    def get_historys(self):
        with Session(engine) as session:
            query = (
                select(History, User, Book)
                .join(User, History.user_id == User.user_id)
                .join(Book, History.book_id == Book.book_id)
            )
        db_historys = session.exec(query).all()
        
        return [
            BorrowResponse(
                borrow_id = history.borrow_id,
                status = history.status,
                borrowed_at = history.borrowed_at,
                returned_at = history.returned_at,
                user=UserResponse(
                    user_id=user.user_id,
                    first_name=user.first_name,
                    last_name = user.last_name,
                    email=user.email,
                    role = user.role
                ),
                book=BookResponse(
                    book_id=book.book_id,
                    book_name=book.book_name,
                    author=book.author,
                    description = book.description,
                    genre= book.genre,
                    status= book.status
                )
            )for  history, user, book  in db_historys
        ]
            
    
    def get_history_by_id(self, borrow_id:UUID):
        with Session(engine) as session:
            query = (
                select(History, User, Book)
                .join(User, History.user_id == User.user_id)
                .join(Book, History.book_id == Book.book_id)
            ).where(History.borrow_id == borrow_id)
        db_history = session.exec(query).first()
        
        history, user, book = db_history
        
        return BorrowResponse(
            borrow_id = history.borrow_id,
            status = history.status,
            borrowed_at = history.borrowed_at,
            returned_at = history.returned_at,
            user=UserResponse(
                user_id=user.user_id,
                first_name=user.first_name,
                last_name = user.last_name,
                email=user.email,
                role = user.role
            ),
            book=BookResponse(
                book_id=book.book_id,
                book_name=book.book_name,
                author=book.author,
                description = book.description,
                genre= book.genre,
                status= book.status
            )
        )
    
    def get_history_by_book_id(self, book_id:UUID):
        with Session(engine) as session:
           query = (
                select(History, User, Book)
                .join(User, History.user_id == User.user_id)
                .join(Book, History.book_id == Book.book_id)
            ).where(History.book_id == book_id)
        db_history = session.exec(query).first()
        
        history, user, book = db_history
        
        return BorrowResponse(
            borrow_id = history.borrow_id,
            status = history.status,
            borrowed_at = history.borrowed_at,
            returned_at = history.returned_at,
            user=UserResponse(
                user_id=user.user_id,
                first_name=user.first_name,
                last_name = user.last_name,
                email=user.email,
                role = user.role
            ),
            book=BookResponse(
                book_id=book.book_id,
                book_name=book.book_name,
                author=book.author,
                description = book.description,
                genre= book.genre,
                status= book.status
            )
        ) 
    
    def get_history_by_user_id(self, user_id:UUID):
        with Session(engine) as session:
            query = (
                select(History, User, Book)
                .join(User, History.user_id == User.user_id)
                .join(Book, History.book_id == Book.book_id)
            ).where(History.user_id == user_id)
        db_historys = session.exec(query).all()
        
        return [
            BorrowResponse(
                borrow_id = history.borrow_id,
                status = history.status,
                borrowed_at = history.borrowed_at,
                returned_at = history.returned_at,
                user=UserResponse(
                    user_id=user.user_id,
                    first_name=user.first_name,
                    last_name = user.last_name,
                    email=user.email,
                    role = user.role
                ),
                book=BookResponse(
                    book_id=book.book_id,
                    book_name=book.book_name,
                    author=book.author,
                    description = book.description,
                    genre= book.genre,
                    status= book.status
                )
            )for  history, user, book  in db_historys
        ]
    
    def update_status(self, update_status:BorrowStatus, borrow_id:UUID):
        with Session(engine) as session:
            db_history = session.exec(select(History).where(History.borrow_id == borrow_id)).first()

            db_history.status = update_status
            db_history.returned_at = generate_timestamp()
            session.add(db_history)
            session.commit()
            session.refresh(db_history)
            
        return db_history
    
    def delete_history(self, borrow_id:UUID):
        with Session(engine) as session:
            db_history = session.exec(select(History).where(History.borrow_id == borrow_id)).first()
            
            session.delete(db_history)
            session.commit()   
            
    