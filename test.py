from fastapi import fastapiRec
app=fastapiRec()
@app.get("/")
def hello():
    return{
        "message":"create the home route",
        "name":"Saurabh"
    }