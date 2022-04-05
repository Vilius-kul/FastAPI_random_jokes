from fastapi import APIRouter, BackgroundTasks, Depends

from data.tables import JokesEnglish
from joke_services import JokeAPI
from models.userinput import UserInput

router = APIRouter()


@router.get("/random_joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    await JokesEnglish.insert(JokesEnglish(joke=joke))
    return joke


@router.get("/multi_jokes")
async def multi_joke(count: UserInput = Depends()):
    jokes = await JokeAPI.multiple_jokes(count.joke_count)
    for joke in jokes:
        await JokesEnglish.insert(JokesEnglish(joke=joke))
    return jokes


@router.get("/jokes_history")
async def joke_history():
    return await JokesEnglish.select()
