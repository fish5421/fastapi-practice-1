from sqlite3 import Timestamp
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode = True

class PostBase(BaseModel):
    image_url: str
    image_url_type: str
    creator_id: int

# for PostDisplay
class User(BaseModel):
    username: str
    class Config():
        orm_mode = True

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    timestamp: datetime
    user: User
    class Config():
        orm_mode = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str