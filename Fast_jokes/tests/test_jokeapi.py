from clients.jokeapi import JokeAPI


async def test_get_random_joke_twopart(mock_twopart_async):

    result = await JokeAPI.get_random_joke()

    assert result == "Testing Setup -> Testing delivery"


async def test_get_random_joke_single(mock_single_async):

    joke = await JokeAPI.get_random_joke()

    assert joke == "Testing 1 joke"


async def test_multiple_jokes_with_input(mock_single_async):

    jokes = await JokeAPI.multiple_jokes(3)

    assert len(jokes) == 3
