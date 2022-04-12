import httpx
import pytest
from src.joke_services import JokeAPI


async def test_get_random_joke_twopart(mock_twopart_async):
    result = await JokeAPI.get_random_joke()

    assert result == "Testing Setup -> Testing delivery"


async def test_get_random_joke_single(mock_single_async):

    joke = await JokeAPI.get_random_joke()

    assert joke == "Testing 1 joke"


async def test_multiple_jokes_with_input(mock_single_async):

    jokes = await JokeAPI.multiple_jokes(3)

    assert len(jokes) == 3


async def test_multiple_jokes_with_bad_input(mock_single_async):

    not_valid_count = 11

    with pytest.raises(Exception) as ex:
        jokes = await JokeAPI.multiple_jokes(not_valid_count)

    assert "Joke count must be between 1 and 10!" == str(ex.value)


async def test_get(mock_random_joke_non_200_resp):

    url = "https://v2.jokeapi.dev/joke/"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    assert response.status_code == 501


async def test_random_joke_get(mock_random_joke_non_200_resp):

    joke = await JokeAPI.get_random_joke()

    assert joke == "Error response 501 while requesting url."
