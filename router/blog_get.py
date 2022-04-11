from fastapi import APIRouter
from typing import Optional
from fastapi import status, Response
from enum import Enum

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get("/type/{blog_type}", tags=["blog"])
def get_blog_type(blog_type: BlogType):
    return {"blog_type": blog_type}


@router.get("/")
def index():
    return {"message": "Hello World"}

# @app.get("/blog/all")
# def get_all_blogs():
#     return {"message": "All blogs"}

@router.get("/all",
        summary='Get all blogs',
        description='This api call simulates retieving or querying all blogs',
        response_description='The list of all available blogs')
def get_all_blogs(page, page_size):
    return {"message": f"All {page_size} blogs on page {page}"}



@router.get("/{id}/comments/{comment_id}",
         tags=['comment'])
def get_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """
    Similates retrieving comments for a blog

    - **id**: blog id mandatory path parameter
    - **comment_id**: comment id mandatory path parameter
    - **valid**: valid flag optional query parameter
    - **username**: username optional query parameter
    
    """


    
    return {"message": f"Comment {comment_id} for blog {id} is valid: {valid} and username: {username}"} 
    
    

@router.get("/{id}", status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return{'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {f"Blog with id {id}"}
