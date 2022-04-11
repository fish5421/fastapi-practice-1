from auth.oauth2 import get_current_user
from fastapi import APIRouter, Depends, HTTPException, status, File
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from router.schemas import PostBase, PostDisplay
from db.database import get_db
from db import db_files
from typing import List
from fastapi.datastructures import UploadFile
from random import randint
import uuid
from fastapi.responses import FileResponse
import os
import shutil
from router.schemas import UserAuth


router = APIRouter(
    prefix='/post',
    tags=['post']
)

image_url_types = ['absolute', 'relative']

@router.post('', response_model=PostDisplay, status_code=status.HTTP_201_CREATED)
def create(request: PostBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                    detail='Parameter image_url_type can only take values absolute or relative')
    return db_files.create(db, request)

@router.get('/all', response_model=List[PostDisplay])
def posts(db: Session = Depends(get_db)):
    return db_files.get_all(db)

@router.post('/image')
async def upload_image(image: UploadFile = File(...), current_user: UserAuth = Depends(get_current_user)):
    filename = f"{uuid.uuid4()}.jpg"
    path = f'images/{filename}'
    contents = await image.read()  # <-- Important!

    with open(path, 'w+b') as buffer:
        buffer.write(contents)
    
    return{'filename': path}

@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
    return db_files.delete(db, id, current_user.id)

