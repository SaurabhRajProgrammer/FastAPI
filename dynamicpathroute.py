from fastapi import FastAPI
#fastapi is library and FastAPI is class inside it
app=FastAPI()
#app is object which derived properties of FastAPI class
@app.get("/user/{user_id}")
def get_user(user_id:str):
    return{"user_id":user_id}
