from fastapi import APIRouter
from todo_model import Todo


todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo:Todo) -> dict :
    todo_list.append(todo)
    return {"message":"list added"}


@todo_router.get("/todo")
async def get_todo() -> dict:
    return{"message":todo_list}