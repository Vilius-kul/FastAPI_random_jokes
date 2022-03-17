from fastapi import APIRouter, BackgroundTasks, Depends

from joke_services import JokeAPI
from jokes_piccoloapp.tables import JokesEnglish
from models.userinput import UserInput

router = APIRouter()

############### background tasks #########
async def insert_joke_to_db(joke: str):
    await JokesEnglish.insert(JokesEnglish(joke=joke))


async def insert_jokes_to_db(jokes: list[str]):
    for joke in jokes:
        await JokesEnglish.insert(JokesEnglish(joke=joke))


##########################################


@router.get("/random-joke")
async def random_joke(background_tasks: BackgroundTasks):
    joke = await JokeAPI.get_random_joke()
    # TODO: do something if api returns empty or some other non string stuff...
    background_tasks.add_task(insert_joke_to_db, joke)
    return joke


@router.get("/multi-jokes")
async def multi_joke(background_tasks: BackgroundTasks, count: UserInput = Depends()):
    jokes = await JokeAPI.multiple_jokes(count.joke_count)
    background_tasks.add_task(insert_jokes_to_db, jokes)
    return jokes


@router.get("/jokes-history")
async def joke_history():
    return await JokesEnglish.select()
