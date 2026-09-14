from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getSome():
    return {"Status": "Something Return!!!!"}
