import os

import uvicorn
from fastapi import FastAPI

import api
from views import home

os.environ["PICCOLO_CONF"] = "piccolo_conf"

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.include_router(home.router)
    app.include_router(api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run("main:app")
else:
    configure()
