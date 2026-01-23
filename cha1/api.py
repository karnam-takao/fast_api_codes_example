from fastapi import APIRouter,Path
from todo_model import Todo , TodoItem


todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo:Todo) -> dict :
    todo_list.append(todo)
    return {"message":"list added"}



    
@todo_router.put("/todo/{todo_id}")
async def update_todo(todo_data : TodoItem, todo_id: int = Path(...,title="id to updating the todo"))-> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
        return {
            "message":"sucess"
        }
        
    return{
        "message":"fail"
    }


@todo_router.get("/todo")
async def get_todo() -> dict:
    return{"message":todo_list}


@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id:int = Path(...,title="dlete todo id"))-> dict:
    
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return{
                "message":"done"
            }
    
    return{
        "message":"failed no id"
    }
        



@todo_router.get("/todo/{todo_id}")

async def get_single_todo(todo_id: int = Path(...,title="The ID of the Todo to retrive."))-> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return{
                "todo":todo
            }
    
    return {
        "message":"Todo id does not exist!!!"
    }



    