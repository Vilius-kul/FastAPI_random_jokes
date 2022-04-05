from fastapi import APIRouter, BackgroundTasks, Depends

from data.tables import JokesEnglish
from joke_services import JokeAPI
from models.userinput import UserInput

router = APIRouter()

############### background tasks #########


async def insert_jokes_to_db(jokes: list[str]):
    for joke in jokes:
        await JokesEnglish.insert(JokesEnglish(joke=joke))


##########################################


@router.get("/random_joke")
async def random_joke(background_tasks: BackgroundTasks):
    joke = await JokeAPI.get_random_joke()
    # TODO: do something if api returns empty or some other non string stuff...
    background_tasks.add_task(insert_jokes_to_db, [joke])
    return joke


@router.get("/multi_jokes")
async def multi_joke(background_tasks: BackgroundTasks, count: UserInput = Depends()):
    jokes = await JokeAPI.multiple_jokes(count.joke_count)
    background_tasks.add_task(insert_jokes_to_db, jokes)
    return jokes


@router.get("/jokes_history")
async def joke_history():
    return await JokesEnglish.select()
