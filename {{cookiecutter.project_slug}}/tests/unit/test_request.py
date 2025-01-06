import os
import pytest
from fastapi import Request
from unittest.mock import MagicMock

from testcontainers.redis import RedisContainer

from app.core.container import get_request_id, settings


@pytest.fixture(scope="module", autouse=True)
def mock_redis_container():
    with RedisContainer("redis:latest") as redis:
        redis_host = redis.get_container_host_ip()
        redis_port = redis.get_exposed_port(6379)
        redis_url = f"redis://{redis_host}:{redis_port}"

        os.environ["REDIS_URL"] = redis_url
        settings.REDIS_URL = redis_url

        yield redis


def test_get_request_id():
    mock_request = MagicMock(spec=Request)

    mock_request.headers = {"X-Request-ID": "12345"}
    request_id = get_request_id(mock_request)
    assert request_id == "12345", "It should return the value of the 'X-Request-ID' header"

    mock_request.headers = {}
    request_id = get_request_id(mock_request)
    assert request_id is None, "It should return None if the 'X-Request-ID' header is not present"

