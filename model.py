from sqlalchemy import Column, Integer, String, Date
from database import Base

class Book(Base):
    __tablename__ = "books"

    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True, nullable=False)
    author = Column(String(255), index=True, nullable=False)
    published_date = Column(Date, nullable=True)
    isbn = Column(String(13), unique=True, index=True, nullable=False)