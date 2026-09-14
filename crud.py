from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todos(insertTodo:Todo):
    todos.append(insertTodo)

    return {
        "message": "TODOS added",
        "data": todos
    }

# Both the Route Paths for POST & GET methods is same name here, python interpreter understands only the 
# Methods instaed of it's Route Path Name.
@app.get("/todos")
def get_todo():
    return {
        "message": "GET API Called Successfully",
        "data": todos
    }
