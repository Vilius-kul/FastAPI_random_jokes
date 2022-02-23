from pydantic import BaseModel


class UserInput(BaseModel):
    joke_count: int
