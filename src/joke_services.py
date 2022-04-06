from urllib.parse import urljoin

import httpx

from models.jokes import Joke
from models.validation_error import ValidationError


class JokeAPI:

    base_url = "https://v2.jokeapi.dev/joke/"
    # base_url = "https://v2.belekas.dev"

    @classmethod
    async def get_random_joke(cls):
        endpoint = "Any?blacklistFlags=nsfw,racist,sexist,explicit"
        url = urljoin(cls.base_url, endpoint)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        data = response.json()
        joke = Joke(**data)

        if joke.type == "single":
            return joke.joke
        else:
            return f"{joke.setup} -> {joke.delivery}"

    @classmethod
    async def multiple_jokes(cls, user_input):
        validated = cls.validate_userinput(user_input)
        jokes = [await cls.get_random_joke() for joke in range(validated)]
        return jokes

    @staticmethod
    def validate_userinput(user_input: int):
        if user_input <= 10 and user_input > 0:
            return user_input
        raise ValidationError(
            status_code=400, error_msg="Joke count must be between 1 and 10!"
        )
