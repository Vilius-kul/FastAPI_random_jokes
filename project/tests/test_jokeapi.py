from clients.jokeapi import JokeAPI


async def test_get_random_joke_twopart(mock_twopart_async):

    joke = await JokeAPI.get_random_joke()

    assert joke == {"Testing Setup": "Testing delivery"}


async def test_get_random_joke_single(mock_single_async):

    joke = await JokeAPI.get_random_joke()

    assert joke == {"Random joke": "Testing 1 joke"}
