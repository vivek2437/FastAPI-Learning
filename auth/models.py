from sqlalchemy import Column, Integer, String
from auth_database import Base

class User(Base):
    __totalname__='users'

    id = Column(Integer, primary_key=True, index=True)
    username =  Column(String(255), index=True , unique=True)
    email= Column(String(255) , index=True , unique=True)
    hashed_password = Column(String)
    role = Column(String(50),default='user')


    
