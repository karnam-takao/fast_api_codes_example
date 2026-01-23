from pydantic import BaseModel

class PacktBook(BaseModel):
    id:int
    name:str
    publishers:str
    isbn:str
    
class TodoItem(BaseModel):
    item:str
    
    class Config:
        schema_extra = {
            "example": {
                "item":"read the next few lines"
            }
        }  

class Todo(BaseModel):
    id:int
    item:str
    