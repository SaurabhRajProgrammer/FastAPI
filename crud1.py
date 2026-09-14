from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
todos=[]
class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/TodoGame")
def create_users(inserttodo:Todo):
    todos.append(inserttodo)
    return {
        "message":"Add the  TodoData",
        "Data":inserttodo
    } 
@app.get("/TodoGame")
def create_users():
    return todos
        # "message":"Get API called successfully",
        # "Data":todos
    # }  