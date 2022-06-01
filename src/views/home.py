import fastapi

router = fastapi.APIRouter()


@router.get("/")
async def read_root():
    return fastapi.responses.HTMLResponse(
        "<h1>Welcome to Fast JokeAPI</h1>\
        <h2>To try it out, go to:</h2>\
        <ul>\
        <li><a href='/random_joke'> Random joke! </li>\
        <li><a href='/multi_jokes?joke_count=2'> Multiple jokes/{joke_count}</li>\
        <li><a href='/jokes_history'> Jokes history </li>\
        </ul>"
    )
