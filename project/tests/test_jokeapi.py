from clients.jokeapi import JokeAPI


def test_get_random_joke():
    # Arrange

    # Act
    joke = JokeAPI.get_random_joke()
    # Assert
    assert joke == "string"
