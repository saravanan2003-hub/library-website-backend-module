from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)

def create_db_and_table():
    SQLModel.metadata.create_all(engine)
    

__all__ = ["engine", "Session", "create_db_and_table"]