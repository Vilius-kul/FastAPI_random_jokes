from fastapi import APIRouter, Depends, Response

from data.tables import JokesEnglish
from joke_services import JokeAPI
from models.userinput import UserInput
from models.validation_error import ValidationError

router = APIRouter()


@router.get("/random_joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    try:
        await JokesEnglish.insert(JokesEnglish(joke=joke))
    except Exception as e:
        print(e)
    return joke


@router.get("/multi_jokes")
async def multi_joke(count: UserInput = Depends()):
    try:
        jokes = await JokeAPI.multiple_jokes(count.joke_count)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as x:
        return Response(content=str(x), status_code=500)
    for joke in jokes:
        await JokesEnglish.insert(JokesEnglish(joke=joke))
    return jokes


@router.get("/jokes_history")
async def joke_history():
    return await JokesEnglish.select()


# return jokes_in_english table from by id
@router.get("/jokes_history/{id}")
async def get_joke_by_id(id: int):
    return await JokesEnglish.select().where(JokesEnglish.id == id)  # type: ignore
