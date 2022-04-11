from django.template import Engine
from fastapi import FastAPI
from router import blog_get, blog_post, users, file, post
from db import models
from db.database import engine
from fastapi.staticfiles import StaticFiles
from auth import authentication


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(users.router)
app.include_router(file.router)
app.include_router(post.router)
app.include_router(authentication.router)

@app.get("/hello")
def index():
    return {"message": "Hello World"}

models.Base.metadata.create_all(engine)

app.mount('/images', StaticFiles(directory='images'), name='images')