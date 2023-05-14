from fastapi import FastAPI
import uvicorn
from connect import connect
import os

app = FastAPI()


@app.get("/")
async def root():
    res = None
    res = connect()
    if not res:
        res = "debug"
    return {"message": "Hello World\n" + res}


if __name__ == "__main__":
    FASTAPI_HOST = os.environ.get('FASTAPI_HOST', "127.0.0.1")
    FASTAPI_PORT = int(os.environ.get('FASTAPI_PORT', 8000))
    uvicorn.run("app:app", reload=True, host=FASTAPI_HOST, port=FASTAPI_PORT)
