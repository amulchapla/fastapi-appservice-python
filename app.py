# Run `uvicorn main:app`
# OR Run `uvicorn app:app`
# Open browser and go to `"http://localhost:8000"` and you should get a "Hello World FastAPI" message back.
# You can also get to API swagger doc at `"http://localhost:8000/docs"`

import os
from fastapi import FastAPI, Request

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()


@app.get("/")
async def root():
    db_server = os.environ['DATABASE_SERVER']
    hello_msg = db_server + " Hello FastAPI"
    filestore_path = os.getenv('FILESTORE_PATH')
    #return {"message": "Hello World FastAPI"}
    return {"message": hello_msg, "filestorepath": filestore_path}

@app.get("/get")
async def get_name(name:str):
    return {"nameOut": name+" FastAPI rocks!"}

