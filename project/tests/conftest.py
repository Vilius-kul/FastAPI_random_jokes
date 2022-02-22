import httpx
import pytest
from pytest_httpx import HTTPXMock


@pytest.fixture(params=["asyncio"])
def anyio_backend(request):
    return request.param


@pytest.fixture
async def mock_twopart_async(httpx_mock: HTTPXMock, anyio_backend):
    httpx_mock.add_response(
        json={
            "type": "twopart",
            "setup": "Testing Setup",
            "delivery": "Testing delivery",
        },
    )

    async with httpx.AsyncClient() as client:
        response = await client.get("https://v2.jokeapi.dev/joke/")


@pytest.fixture
async def mock_single_async(httpx_mock: HTTPXMock, anyio_backend):
    httpx_mock.add_response(
        json={"type": "single", "joke": "Testing 1 joke"},
    )

    async with httpx.AsyncClient() as client:
        response = await client.get("https://v2.jokeapi.dev/joke/")
