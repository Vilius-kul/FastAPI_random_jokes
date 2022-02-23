from urllib.parse import urljoin

import httpx


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

        joke = {}

        if data["type"] == "twopart":
            joke = {data["setup"]: data["delivery"]}
        else:
            joke = {"Random joke": data["joke"]}
        return joke

    @classmethod
    async def multiple_jokes(cls, user_input):
        if user_input not in range(1, 11):
            raise ValueError("Joke_count must be between 1 and 11!")

        jokes = {joke: await cls.get_random_joke() for joke in range(user_input)}
        return jokes
