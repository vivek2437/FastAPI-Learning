from pydantic import BaseModel , EmailStr

class UserCreate(BaseModel):
    username : EmailStr
    email : str
    password : str
    role: str

class UserLogin(BaseModel):
    username:str
    password: str