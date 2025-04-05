from fastapi import APIRouter , File, UploadFile, Form, Request
from .book_service import BookService
from .book_schema import BookResponse, BookCreate, Status
from uuid import UUID
import cloudinary
import cloudinary.uploader
from util.auth import authenticate
from modules.user.user_validator import UserValidator


cloudinary.config(
    cloud_name="dvdp7km2p",
    api_key="561237235751194",
    api_secret="Y6CqfNdaPwwMxr2CN3jn2d961LM"
)


def convert_image_to_url(file: UploadFile = File(...)):
    result = cloudinary.uploader.upload(file.file)
    image_url = result.get("url")
    print(image_url)
    return {"url": image_url}

router = APIRouter()
book_service = BookService()


@router.post("/books/", response_model = BookResponse)
async def create_book(request:Request, book_name: str = Form(...),author: str = Form(...),description: str = Form(...),genre: str = Form(...),book_image: UploadFile = File(...)):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    
    # Convert the image to a URL
    image_url = convert_image_to_url(book_image)["url"]
    
    # Construct the book data dictionary manually
    book_data = {
        "book_name": book_name,
        "author": author,
        "description": description,
        "genre": genre,
        "book_image": image_url
    }

    # Pass the data to the service
    return book_service.book_create(book_data)

    

@router.get("/books/", response_model = list[BookResponse])
def get_books(book_id :str | None = None , book_name:str | None = None , author:str | None = None, genre:str | None = None, q: str | None = None):
    if book_id:
        return book_service.get_book_by_id(book_id)
    
    if book_name:
        return book_service.get_book_by_book_name(book_name)
    
    if author:
        return book_service.get_book_by_author(author)
    
    if genre:
        return book_service.get_book_by_genre(genre)
    
    if q:  # 🔥 Search Function (Only One Filter at a Time)
        books = book_service.get_books()  # Fetch all books
        filtered_books = []
        for book in books:
            if q.lower() in book.book_name.lower():
                filtered_books.append(book)
            elif q.lower() in book.author.lower():
                filtered_books.append(book)
            elif q.lower() in book.genre.lower():
                filtered_books.append(book)
        
        return filtered_books
    
    return book_service.get_books()
    
    

@router.put("/books/{book_id}", response_model = BookResponse)
def update_book(book_id:str,book_data:BookCreate, request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return book_service.update_book(book_id,book_data)

@router.delete("/books/{book_id}")
def delete_book(book_id:str , request:Request):
    user_dict = authenticate(request)
    role = user_dict["role"]
    UserValidator.validate_user_role(role)
    return book_service.delete_book(book_id)