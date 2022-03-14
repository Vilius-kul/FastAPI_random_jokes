import fastapi
from clients.jokeapi import JokeAPI
from fastapi import Depends
from jokes_piccoloapp.tables import JokesEnglish
from models.userinput import UserInput

router = fastapi.APIRouter()


@router.get("/random-joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    await JokesEnglish.insert(
        JokesEnglish(joke=joke)
    )  # inserts jokes into db, JokesEnglish table
    return joke


@router.get("/multi-jokes")
async def multi_joke(count: UserInput = Depends()):
    # TODO: add db insert function
    return await JokeAPI.multiple_jokes(count.joke_count)
