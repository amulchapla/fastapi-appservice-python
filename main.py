from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World FastAPI"}

@app.get("/get")
async def get_name(name:str):
    return {"nameOut": name+" FastAPI rocks!"}

