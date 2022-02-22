import fastapi
from clients.jokeapi import JokeAPI
from fastapi import Path

router = fastapi.APIRouter()


@router.get("/random-joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    return joke


@router.get("/multiple-jokes/{count}")
async def multiple_jokes(
    count: int = Path(
        ..., description="Joke count must be in range 1 to 10!", ge=1, le=10
    )
):
    return await JokeAPI.multiple_jokes(count)
