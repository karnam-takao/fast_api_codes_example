from fastapi import FastAPI

from api import todo_router
from student_api import student_router

app  = FastAPI()


@app.get("/")
async def read_root() -> dict:
    return {"Hello": "World"}

app.include_router(todo_router)
app.include_router(student_router,prefix="/student")


#dynamic filtering the result while sending 

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# class Student(BaseModel):
#     student_id: int
#     student_name: str
#     age: int
#     grade: str
#     section: str

# # Sample data
# student_list = [
#     Student(student_id=1, student_name="John", age=16, grade="10th", section="A"),
#     Student(student_id=2, student_name="Jane", age=17, grade="11th", section="B")
# ]

# # Only return student_name dynamically
# @app.get("/students/names", response_model=List[Student], response_model_include={"student_name"})
# async def get_only_names():
#     return student_list
