from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Users(BaseModel):
    name:str
    age:int
    password:str

class UsersResponse(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=UsersResponse)
def get_user():
    return{
        "name":"Nayra",
        "age":4,
        "password":"154017"
    }