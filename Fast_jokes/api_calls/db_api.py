import fastapi
from jokes_piccoloapp.tables import JokesEnglish

router = fastapi.APIRouter()


@router.get("/jokes-history")
async def joke_history():
    return await JokesEnglish.select()
