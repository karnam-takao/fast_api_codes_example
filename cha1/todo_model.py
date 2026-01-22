from pydantic import BaseModel

class PacktBook(BaseModel):
    id:int
    name:str
    publishers:str
    isbn:str
    
    

class Todo(BaseModel):
    id:int
    item:str
    