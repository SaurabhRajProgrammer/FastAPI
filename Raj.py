from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def saurabh():
    return{"message":"successfully"}
#about Route
@app.get("/about")
def hello():
    # a=10
    # b=20
    return{"message":"This is about Route"}

@app.get("/user")
def suman():
    # a=10
    # b=20
    return{"message":"This is user Route"}