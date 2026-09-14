from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users =[]

# show otput look
#put /users/104?notify=true
# {
    # "name":"Saurabh",
    # "age":24
# }
class User(BaseModel):
    name:str
    age:int
@app.post("/users")
def create_api(var:User):
    users.append(var)    
    return {
        "message":"create the users",
        "data":var
    }
@app.put("/users/{user_id}")
def update_api(user_id:int,var:User,notify:bool = False):
    if user_id < len(users):
        users[user_id]=User

