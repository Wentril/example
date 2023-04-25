from fastapi import FastAPI
import uvicorn
from connect import connect

app = FastAPI()


@app.get("/")
async def root():
    res = None
    res = connect()
    if not res:
        res = "debug"
    return {"message": "Hello World\n" + res}


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True, host="localhost", port=10000)
