from ast import alias
from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Path, Body
from pydantic import BaseModel

router = APIRouter(
    tags=["blog"],
    prefix="/blog"
)

class Image(BaseModel):
    url: str
    alias: str

class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]
    nb_comments: int
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[Image] = None

@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
        }


@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogModel, id: int, 
            comment_title: int = Query(None,
                title="Title of the comment",
                description="Id description for comment_title",
                alias="commentTitle",
                deprecated=True),
            
            content: str = Body(...,
                    min_length=10,
                    max_length=12,
                    regex='^[a-z\s]*$'),
            
            v: Optional[List[str]] = Query(['1','2','3']),
            comment_id: int = Path(None, gt=5, le=10)

    ):

    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v,
        'comment_title': comment_title
        }

def required_functionality():
    return {'meassage': 'Learning FAstAPI'}