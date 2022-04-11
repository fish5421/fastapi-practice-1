from sqlalchemy.orm.session import Session
from router.schemas import UserBase
from db.models import DBUser
from db.hash import Hash
from fastapi import HTTPException, status


def create_user(db: Session, request: UserBase):
    new_user = DBUser(
        username=request.username,
        email=request.email,
        password=Hash.becrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db: Session):
    return db.query(DBUser).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(DBUser).filter(DBUser.id == user_id).first()

def update_user(db:Session, user_id: int, request: UserBase):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if user:
        user.username = request.username
        user.email = request.email
        user.password = Hash.becrypt(request.password)
        db.commit()
        db.refresh(user)
        return 'ok'
    return 'nope'

def delete_user(db: Session, user_id: int):
    user = db.query(DBUser).filter(DBUser.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return 'ok'
    return 'nope'
    
def get_user_by_username(db: Session, username: str):
    user = db.query(DBUser).filter(DBUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"User not, {username} found")
    return user
        

