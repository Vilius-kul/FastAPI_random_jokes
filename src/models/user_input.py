from pydantic import BaseModel, validator


class UserInput(BaseModel):
    joke_count: int

    # @validator("joke_count")
    # def limit_count(cls, v):
    #     if v <= 10 and v > 0:
    #         return v
    #     raise ValueError("Out of range! Try 1 to 10.")
