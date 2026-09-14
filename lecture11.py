from fastapi import FastAPI,status,HTTPException

app=FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_users():
    return {
        "message":"Users Created"
    }
@app.get("/user")
def get_user():
    return {
        "status":"success",
        "message":"User fetched",
        "data":{
            "name":"Saurabh",
            "age":21
        }

    }
@app.get("/users/{user_id}")
def get_user(user_id:int):
    if user_id !=1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id":1,
        "name":"Saurabh"
    }

