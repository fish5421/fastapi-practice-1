from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import Response
import os
from random import randint
import uuid
from sqlalchemy.orm.session import Session
import shutil


router = APIRouter(
    prefix='/file',
    tags=['file']
)

# @router.post('/file')
# def get_file(file: bytes = File(...)):
#     content = file.decode('utf-8')


@router.post("/images/")
async def create_upload_file(image: UploadFile = File(...)):

    image.filename = f"{uuid.uuid4()}.jpg"
    # contents = await image.read()  # <-- Important!
    path = f'images/{image.filename}'

    with open(path, 'w+b') as buffer:
        await shutil.copyfileobj(image.file, buffer)

    return {"filename": path}



