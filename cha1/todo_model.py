from pydantic import BaseModel
from typing import List


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
    

class TodoItems(BaseModel):
    todos:List[TodoItem]
    
    class Config : 
        schema_extra ={
            "example":{
                "todos":[
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    },
                    {
                        "item": "Example schema 3!"
                    },
                ]
                
            }
        }
            
   
class Student(BaseModel):
    student_id:int
    student_name:str
    age:int
    grade:str
    section:str
    
    class Config:
        schema_extra = {
            "student_id": 1,
            "Student_name": "John Doe",
            "age": 16,
            "grade": "10th",
            "section": "A"
        }
        
        
        
    
class Student_list(BaseModel):
    students : List[Student]
    
    class Config:
        schema_extra = {
            "example": {
                "students": [
                    {
                        "student_id": 1,
                        "Student_name": "John Doe",
                        "age": 16,
                        "grade": "10th",
                        "section": "A"
                    },
                    {
                        "student_id": 2,
                        "Student_name": "Jane Smith",
                        "age": 15,
                        "grade": "9th",
                        "section": "B"
                    }
                ]
            }
        }
        

class Student_name(BaseModel):
    student_name: str
    

    
    # class Config:
    #     schema_extra = {
    #         "example":{
                
            
    #             "students":[
    #                 {
    #                     "student":"student obj1"
    #                 },
                    
    #                 {
    #                     "student":"student obj 2"
    #                 },
    #         ]
            
    #     }
    # }
    



            
      

