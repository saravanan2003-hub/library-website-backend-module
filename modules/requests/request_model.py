from sqlmodel import SQLModel, select, Field
from uuid import UUID, uuid4
from datetime import datetime, timezone
from util.database import engine, Session
from .request_schema import RequestCreate, RequestResponse, request_status
from modules.user.user_model import User
from modules.book.book_model import Book
from modules.user.user_schema import UserResponse
from modules.book.book_schema import BookResponse

def generate_timestamp():
    return datetime.now(timezone.utc)


class RequestBase(SQLModel):
    user_id: UUID = Field(foreign_key="user.user_id")
    book_id: UUID = Field(foreign_key="book.book_id")
     
    
class Request(RequestBase, table=True):
    request_id: UUID = Field(primary_key=True, default_factory=uuid4)
    status: request_status  = Field(default=request_status.pending)
    requested_at: datetime = Field(default_factory=generate_timestamp)
    
    
class requestDAO:
    
    def create_request(self, request: RequestCreate):
        with Session(engine) as session:
            db_request = Request(**request.dict())
            session.add(db_request)
            session.commit()
            session.refresh(db_request)
        return db_request
    
    def get_requests(self):
        with Session(engine) as session:
            query = (
            select(Request, User, Book)
            .join(User, Request.user_id == User.user_id)
            .join(Book, Request.book_id == Book.book_id)
        ).where(Request.status == "pending")
        db_request = session.exec(query).all()

        return [
            RequestResponse(
                request_id=request.request_id,
                status=request.status,
                user=UserResponse(
                    user_id=user.user_id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    role=user.role
                ),
                book=BookResponse(
                    book_id=book.book_id,
                    book_name=book.book_name,
                    author=book.author,
                    description=book.description,
                    genre=book.genre,
                    status=book.status,
                    book_image = book.book_image
                )
            ) for request, user, book in db_request  
        ]
    
    
    def get_request_by_id(self, request_id: UUID):
        with Session(engine) as session:
            query = (
                select(Request, User, Book)
                .join(User, Request.user_id == User.user_id)
                .join(Book, Request.book_id == Book.book_id)
            ).where(Request.request_id == request_id)
            db_request = session.exec(query).first()
        
            request, user, book = db_request
        
        return RequestResponse(
            request_id=request.request_id,
            status=request.status,
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
                status= book.status,
                book_image = book.book_image
            )
        )
       
    
    def update_request(self, request_id: UUID, request: RequestCreate): 
        with Session(engine) as session:
            db_request = session.exec(select(Request).where(Request.request_id == request_id)).first()
            
            db_request.status = request.status
            
            session.add(db_request)
            session.commit()
            session.refresh(db_request)
        return db_request 
    
    def delete_request(self, request_id: UUID):
        with Session(engine) as session:
            db_request = session.exec(select(Request).where(Request.request_id == request_id)).first()
            session.delete(db_request)
            session.commit()
        return db_request
        
    def get_request_by_user_id(self, user_id: UUID):
        with Session(engine) as session:
            query = (
                select(Request, User, Book)
                .join(User, Request.user_id == User.user_id)
                .join(Book, Request.book_id == Book.book_id)
            ).where(Request.user_id == user_id)
            db_request = session.exec(query).all()
        
        return [
            RequestResponse(
                request_id=request.request_id,
                status=request.status,
                user=UserResponse(
                    user_id=user.user_id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    role=user.role
                ),
                book=BookResponse(
                    book_id=book.book_id,
                    book_name=book.book_name,
                    author=book.author,
                    description=book.description,
                    genre=book.genre,
                    status=book.status,
                    book_image = book.book_image
                )
            ) for request, user, book in db_request  
        ]
    
    def get_request_by_book_id(self, book_id: UUID):
        with Session(engine) as session:
            query = (
                select(Request, User, Book)
                .join(User, Request.user_id == User.user_id)
                .join(Book, Request.book_id == Book.book_id)
            ).where(Request.book_id == book_id)
            db_request = session.exec(query).all()
        
        return [
            RequestResponse(
                request_id=request.request_id,
                status=request.status,
                user=UserResponse(
                    user_id=user.user_id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                    email=user.email,
                    role=user.role
                ),
                book=BookResponse(
                    book_id=book.book_id,
                    book_name=book.book_name,
                    author=book.author,
                    description=book.description,
                    genre=book.genre,
                    status=book.status
                )
            ) for request, user, book in db_request  
        ]