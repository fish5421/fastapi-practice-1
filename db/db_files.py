from fastapi import HTTPException, status
from router.schemas import PostBase
from sqlalchemy.orm.session import Session
from db.models import DBImageFiles
import datetime



def create(db: Session, request: PostBase):
    new_post = DBImageFiles(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        timestamp = datetime.datetime.now(),
        user_id = request.creator_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_all(db: Session):
    return db.query(DBImageFiles).all()

def delete(db: Session, id: int, user_id: int):
    post = db.query(DBImageFiles).filter(DBImageFiles.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Post with id {id} not found")
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
            detail=f"You are not the creator of this post")

    db.delete(post)
    db.commit()
    return 'ok'

