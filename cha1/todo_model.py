from pydantic import BaseModel

class PacktBook(BaseModel):
    id:int
    name:str
    publishers:str
    isbn:str
    
class Item(BaseModel):
    id:int
    status:bool   

class Todo(BaseModel):
    id:int
    item:str
    