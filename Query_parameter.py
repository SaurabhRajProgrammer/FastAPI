from fastapi import FastAPI

app=FastAPI()
@app.get("/users")
def get_users(name:str=None):
    return {"Name":name}

@app.get("/product")
def get_users(product_name:str=None):
    return {"product_Name":product_name}

@app.get("/product_limit")
def get_users(limit:int=20):
    return {"limit":limit}

@app.get("/product_limit")
def get_users(limit:int=20):
    return {"limit":limit}

@app.get("/product_limit")
def get_users(limit:int=20):
    return {"limit":limit}

@app.get("/items")
def get_users(name:str=None,price: int=0):
    return {
        "name":name,
        "price":price
    }
