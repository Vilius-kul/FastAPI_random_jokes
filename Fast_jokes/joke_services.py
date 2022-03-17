from urllib.parse import urljoin

import httpx

from models.jokes import PydanticJoke


class JokeAPI:

    base_url = "https://v2.jokeapi.dev/joke/"

    @classmethod
    async def get_random_joke(cls):
        endpoint = "Any?blacklistFlags=nsfw,racist,sexist,explicit"
        url = urljoin(cls.base_url, endpoint)
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        data = response.json()
        joke = PydanticJoke(**data)

        if joke.type == "single":
            return joke.joke
        else:
            return f"{joke.setup} -> {joke.delivery}"

    @classmethod
    async def multiple_jokes(cls, user_input):
        jokes = [await cls.get_random_joke() for joke in range(user_input)]
        return jokes
