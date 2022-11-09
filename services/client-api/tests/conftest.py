import pytest
from starlette.testclient import TestClient

from project import create_app
from project.config import Settings, get_settings


def get_settings_override():
    return Settings(testing=1)


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
