from fastapi import APIRouter,Path,HTTPException,status
from todo_model import Student,Student_list,Student_name
from typing import List


student_router  = APIRouter()
student_list = []


#display all the students
@student_router.get("/",response_model=Student_list)
async def get_student( )-> dict :
    if len(student_list) <1 : 
        return{
            "message":"no data!!"
        }
    
    return{
        "students":student_list
    }
    

@student_router.post("/")
async def add_student(student:Student) -> dict:
    student_list.append(student)
    
    return{
        "message":"student added!!"
    }
    
    

@student_router.put("/{student_id}")
async def update_student(student:Student,student_id:int = Path(...,title="updating student!!"))-> dict:
    print(student)
    print(f"id:${student_id} ")
    return{
        "message":"okay"
    }
    

@student_router.delete("/{student_id}")
async def delete_student(student_id:int= Path(...,title="deleteing the  student")) -> dict:
    print(student_id)
     
    return{
        "message":"okay"
    }
    
@student_router.get("/names",response_model=List[Student_name])
async def get_only_names():
    return student_list
