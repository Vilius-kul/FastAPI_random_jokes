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

        if data["type"] == "twopart":
            return {data["setup"]: data["delivery"]}
        else:
            return {"Random joke": data["joke"]}
