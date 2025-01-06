import os
import pytest

os.environ["TESTING"] = "1"

@pytest.fixture(scope="session", autouse=True)
def test_config():
    yield
