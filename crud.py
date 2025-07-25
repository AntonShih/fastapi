import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI() #FastAPI物件

@app.get("/")
async def hello_world():
    return {'message' : "Hello,2"}
    # return {"x":3 , 'y':4}

class Gender(str,Enum):
    male = 'male'
    female = 'female'

class UserModel(BaseModel):
    username: str
    description: Optional[str] = None
    gender : Gender



@app.post("/users")
async def create_user(user_model : UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()

    return user_dict

@app.put("/users/{user_id}")
async def update_user(user_id:int, user_model : UserModel):
    print(user_model.username)
    user_dict = user_model.model_dump()
    user_dict.update({'id': user_id})
    return user_dict

if __name__ == "__main__":
    uvicorn.run("crud:app", reload=True)
