import fastapi

router = fastapi.APIRouter()


@router.get("/random-joke")
def random_joke():
    return "So Random"


@router.get("/multiple-jokes")
def multiple_jokes():
    return "Multiple Jokes"
