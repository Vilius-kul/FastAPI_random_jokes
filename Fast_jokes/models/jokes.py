from pydantic import BaseModel


class PydanticJoke(BaseModel):
    setup: None | str
    delivery: None | str
    joke: None | str
    type: str
