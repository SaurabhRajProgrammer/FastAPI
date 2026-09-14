from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    name:str
    age:int
    email:str
@app.post("/create_user")
def create_user(user:User):
    return{
        "message":"user created",
        "data":user
    }  
class Address(BaseModel):    # nested JSON
    city:str
    pin_code:int
class Users(BaseModel):
    name1:str
    age1:int
    address:Address
@app.post("/create_users2")
def create_users(user1:Users):
    return user1          