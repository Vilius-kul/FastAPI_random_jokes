import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "Fast!"}


if __name__ == "__main__":
    uvicorn.run("main:app")
