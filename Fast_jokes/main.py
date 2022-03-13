import os

import uvicorn
from fastapi import FastAPI

from api_calls import db_api, jokes_api
from jokes.tables import JokesEnglish
from views import home

os.environ["PICCOLO_CONF"] = "piccolo_conf"

app = FastAPI()


def configure():
    configure_routing()


def configure_routing():
    app.include_router(home.router)
    app.include_router(jokes_api.router)
    app.include_router(db_api.router)


if __name__ == "__main__":
    configure()
    uvicorn.run("main:app")
else:
    configure()
