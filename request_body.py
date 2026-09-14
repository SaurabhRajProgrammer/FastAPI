from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Users(BaseModel):
    name:str
    age: float
# @app.post("/create-users")
# def create_users(name:str,age:int):
#     return{
#         "name":name,
#         "age":age
#     }
# @app.post("/create-users1")      
# def create_users(users:dict):
    # return{                            
        # "message":"users Created",
        # "data":users
    # }
@app.post("/created-users2")
def create_user(user:Users):
    return{
        "message":"Users created",            #create pydantic 
        "data":user.name
    }    
