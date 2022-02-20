import pytest
from clients.jokeapi import JokeAPI


@pytest.mark.parametrize("anyio_backend", ["asyncio"])
async def test_jokeapi_random_joke(anyio_backend):

    response = await JokeAPI.get_random_joke()

    assert response == ""
