from typing import List
from fastapi import APIRouter, Depends
from router.schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Create user
@router.post("/", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read user
@router.get("/", response_model=List[UserDisplay])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)

# Read one user
@router.get("/{user_id}", response_model=UserDisplay)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, user_id)



# Update user
@router.put("/{user_id}/update")
def update_user(user_id: int, request: UserBase, db: Session = Depends(get_db)):
    return db_user.update_user(db, user_id, request)

# Delete user
@router.delete("/{user_id}/delete")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, user_id)