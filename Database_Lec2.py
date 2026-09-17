from fastapi import FastAPI, Depends,HTTPException,Header

app=FastAPI()

def verify_token(token:str = Header(None)):
    if token !="my_secret_token":
        raise HTTPException(status_code=401,detail="unauthorized")
    return "user authorized"

@app.get("/secure-data")
def secure_data(user =Depends(verify_token)):
    return {"message":user}
