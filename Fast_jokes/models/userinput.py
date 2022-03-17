from pydantic import BaseModel, Field, ValidationError, validator


class UserInput(BaseModel):
    joke_count: int = Field(gt=0, lt=11, description="Must be between 1 and 10")


# couldn't make it work properly
# class UserInput(BaseModel):
#     joke_count: int

#     @validator("joke_count")
#     def limit_count(cls, v):
#         if v not in range(1, 11):
#             raise ValueError("Out of range! Try 1 to 10.")
#         return v
