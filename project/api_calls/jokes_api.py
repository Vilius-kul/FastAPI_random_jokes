import fastapi
from clients.jokeapi import JokeAPI
from fastapi import Depends
from models.userinput import UserInput

router = fastapi.APIRouter()


@router.get("/random-joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    return joke


@router.get("/multi-jokes")
async def multi_joke(count: UserInput = Depends()):
    try:
        return await JokeAPI.multiple_jokes(count.joke_count)
    except ValueError as ve:
        return fastapi.responses.JSONResponse(
            content={"error": str(ve)}, status_code=400
        )


# alternative validation using fastapi.Path(*params)
# @router.get("/multiple-jokes/{count}")
# async def multiple_jokes(
#     count: int = Path(
#         ..., description="Joke count must be in range 1 to 10!", ge=1, le=10
#     )
# ):
#     return await JokeAPI.multiple_jokes(count)
