import os

import pytest
from fastapi.testclient import TestClient
from testcontainers.core.waiting_utils import wait_for_logs
from testcontainers.redis import RedisContainer

os.environ["REDIS_URL"] = "redis://localhost:6379"
redis = RedisContainer("redis:latest").with_exposed_ports(6379)


@pytest.fixture(scope="module", autouse=True)
def setup(request):
    redis.start()

    def remove_container():
        redis.stop()

    request.addfinalizer(remove_container)
    wait_for_logs(redis, "Ready to accept connections")


from app.main import app  # noqa:E402

client = TestClient(app)


def test_health_check():
    response = client.get("/actuator/health")
    assert response.status_code == 200
    assert response.json() == {"msg": "success"}

def test_metrics():
    response = client.get("/actuator/metrics")
    assert response.status_code == 200, "The /metrics endpoint should return 200"
    data = response.json()

    assert "application" in data, "The response should contain the 'application' key"
    assert "uptime_seconds" in data["application"], "It should contain 'uptime_seconds'"
    assert "startup_time" in data["application"], "It should contain 'startup_time'"

    assert "system" in data, "The response should contain the 'system' key"
    assert "cpu_usage_percent" in data["system"], "It should contain 'cpu_usage_percent'"
    assert "memory" in data["system"], "It should contain memory information"
    assert "disk" in data["system"], "It should contain disk information"

    assert "threads" in data, "The response should contain the 'threads' key"
    assert "active_count" in data["threads"], "It should contain 'active_count'"


