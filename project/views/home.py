import fastapi

router = fastapi.APIRouter()


@router.get("/")
async def read_root():
    return "This is a home page!"
