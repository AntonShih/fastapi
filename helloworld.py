# uvicorn helloworld:app --reload
from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI() #FastAPI物件

class Gender(str, Enum):
    male  = 'male' 
    female = 'female'

@app.get("/")
async def hello_world():
    return {'message' : "Hello,2"}
    # return {"x":3 , 'y':4}

@app.get("/helloworld")
async def hello_world():
    return {'message' : "Hello,FastAPI"}
    # return {"x":3 , 'y':4}

@app.get("/users/current")
async def get_user():
    return {"user_id": f"this is a current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": f"this is a user for {user_id}"}

@app.get("/students/{gender}")
async def get_user(gender: Gender):
    return {"user_id": f"this is a {gender.value} student"}


# @app.get("/users")
# async def get_user(page_index: int, page_size: int):
#     return {
#         "page info": f"index: {page_index} size: {page_size}"
#     }


@app.get("/users")
async def get_user(page_index: int, page_size: Optional[int] = 10):
    return {
        "page info": f"index: {page_index} size: {page_size}"
    }

@app.get("/users/{user_id}/friends")
async def get_user_friends(page_index: int, user_id: int, page_size: Optional[int] = 10):
    return {
        "user friends": f"user id: {user_id}, index: {page_index}, size: {page_size}"
    }