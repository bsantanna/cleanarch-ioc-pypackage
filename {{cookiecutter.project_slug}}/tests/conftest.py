import os
import pytest

@pytest.fixture(scope="session", autouse=True)
def mock_redis_url():
    os.environ["REDIS_URL"] = "redis://localhost:6379/0"
