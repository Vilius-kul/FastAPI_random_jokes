from jokes.tables import JokesEnglish


async def get_db_jokes():
    all_jokes = await JokesEnglish.select()
    return all_jokes


async def add_jokes_to_db(joke: str):
    await JokesEnglish.insert(JokesEnglish(joke=joke))
