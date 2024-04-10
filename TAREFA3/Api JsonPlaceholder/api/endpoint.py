from fastapi import APIRouter
from utils.request import make_request

router = APIRouter()

@router.get("/posts")
async def get_posts():
    response = make_request("https://jsonplaceholder.typicode.com/posts")
    return response.json()

