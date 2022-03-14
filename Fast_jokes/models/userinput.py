from pydantic import BaseModel, Field, ValidationError, validator


class UserInput(BaseModel):
    joke_count: int = Field(gt=0, lt=11, description="Must be between 1 and 10")
