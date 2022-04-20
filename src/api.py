from fastapi import APIRouter, Depends, Response

from data.tables import JokesEnglish
from joke_services import JokeAPI
from models.user_input import UserInput
from models.validation_error import ValidationError

router = APIRouter()


@router.get("/random_joke")
async def random_joke():
    joke = await JokeAPI.get_random_joke()
    try:
        await JokesEnglish.insert(JokesEnglish(joke=joke))
    except ConnectionError as ce:
        return ce.args
    return await JokesEnglish.select().order_by(JokesEnglish.id, ascending=False).first()  # type: ignore


@router.get("/multi_jokes")
async def multi_joke(count: UserInput = Depends()):
    try:
        jokes = await JokeAPI.multiple_jokes(count.joke_count)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)

    except Exception as x:
        return Response(content=str(x), status_code=400)
    try:
        for joke in jokes:
            await JokesEnglish.insert(JokesEnglish(joke=joke))
    except ConnectionError as ce:
        return ce.args

    return (
        await JokesEnglish.select()
        .order_by(JokesEnglish.id, ascending=False)  # type: ignore
        .limit(count.joke_count)
    )


@router.get("/jokes_history")
async def joke_history():
    return await JokesEnglish.select()
