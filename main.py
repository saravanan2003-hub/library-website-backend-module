from fastapi import FastAPI
from contextlib import asynccontextmanager
from modules.user.user_controller import router as user_router
from modules.book.book_controller import router as book_router
from modules.lending_deatails.lending_controller import router as histroy_router
from modules.requests.request_controller import router as request_router
from util.database import create_db_and_table
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app):
    create_db_and_table()
    yield
    
app = FastAPI(title="user_task", lifespan=lifespan)

app.include_router(user_router)
app.include_router(book_router)
app.include_router(histroy_router)
app.include_router(request_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],  # ✅ Allow your frontend
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # ✅ Allow all headers (including Authorization for JWT)
)

@app.get("/")
def status():
    return {
        "status": "ok"
    }