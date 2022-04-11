from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from db.database import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship

class DBUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    items = relationship('DBImageFiles', back_populates='user')

class DBImageFiles(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image_url = Column(String(200), nullable=False)
    image_url_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('DBUser', back_populates='items')
    book_spine = relationship("DBdetectedSpines")


class DBdetectedSpines(Base):
    __tablename__ = 'detected_spines'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    image = Column(String(200), nullable=False)
    bookshelf_id = Column(Integer, ForeignKey('images.id'), nullable=False)


