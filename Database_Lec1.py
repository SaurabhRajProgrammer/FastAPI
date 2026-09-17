from fastapi import FastAPI, Depends

app=FastAPI()

def common_logic():
    return {
        "message":"Common Logic Executed"
    }

@app.get("/")
def home(data = Depends(common_logic)):
    return data

#Reusable Logic Across Multiple Routes

def get_current_user():
    return { "user":"Saurabh Raj"}

@app.get("/profile")
def profile(data=Depends(get_current_user)):
    return data

@app.get("/profile2")
def profile(var=Depends(get_current_user)):
    return var
    