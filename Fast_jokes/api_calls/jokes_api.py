from clients.jokeapi import JokeAPI
from fastapi import APIRouter, BackgroundTasks, Depends
from jokes_piccoloapp.tables import JokesEnglish
from models.userinput import UserInput

router = APIRouter()


async def to_database_single(joke: str):
    await JokesEnglish.insert(JokesEnglish(joke=joke))


async def to_database_multi(jokes: list[str]):
    for joke in jokes:
        await JokesEnglish.insert(JokesEnglish(joke=joke))


@router.get("/random-joke")
async def random_joke(background_tasks: BackgroundTasks):
    joke = await JokeAPI.get_random_joke()
    # TODO: do something if api returns empty or some other non string stuff...
    background_tasks.add_task(
        to_database_single, joke
    )  # inserts jokes into db, JokesEnglish table
    return joke


@router.get("/multi-jokes")
async def multi_joke(background_tasks: BackgroundTasks, count: UserInput = Depends()):
    jokes = await JokeAPI.multiple_jokes(count.joke_count)
    background_tasks.add_task(
        to_database_multi, jokes
    )  # inserts jokes into db, JokesEnglish table
    return jokes
