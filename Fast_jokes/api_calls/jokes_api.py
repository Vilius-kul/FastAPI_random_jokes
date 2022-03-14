import fastapi
from clients.jokeapi import JokeAPI
from db_services.jokes_db_servoces import add_jokes_to_db
from fastapi import Depends
from models.userinput import UserInput

router = fastapi.APIRouter()


@router.get("/random-joke")
async def random_joke():
    return await JokeAPI.get_random_joke()


@router.get("/multi-jokes")
async def multi_joke(count: UserInput = Depends()):
    return await JokeAPI.multiple_jokes(count.joke_count)
