import fastapi

router = fastapi.APIRouter()


@router.get("/")
async def read_root():
    return fastapi.responses.HTMLResponse(
        "<h1>Welcome to Fast JokeAPI</h1>\
        <h2>To try it out, go to:</h2>\
        <ul>\
        <li><a href='http://127.0.0.1:8000/random-joke'> Random joke! </li>\
        <li><a href='http://127.0.0.1:8000/multi-jokes?joke_count=2'> Multiple jokes/{joke_count}</li>\
        </ul>"
    )
