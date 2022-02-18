import fastapi
from clients.jokeapi import JokeAPI

router = fastapi.APIRouter()


@router.get("/random-joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    return joke


@router.get("/multiple-jokes")
def multiple_jokes():
    return "Multiple Jokes"
