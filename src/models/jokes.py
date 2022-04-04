from typing import Optional

from pydantic import BaseModel


class Joke(BaseModel):
    setup: Optional[str]
    delivery: Optional[str]
    joke: Optional[str]
    type: str
