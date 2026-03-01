import pytest
import requests

url = "https://reqres.in/api/users"
header = {"x-api-key": "reqres_167601fe554b4ed7beb6755668211cbb"}

@pytest.fixture(scope="session")
def api_fixture():
    session = requests.Session()
    session.headers.update(header)
    yield session
    session.close()

@pytest.fixture(scope='function')
def created_user(api_fixture):
    response = api_fixture.post(url, json={"name": "xxasdxc", "job": "qa-engineer"})
    user = response.json()
    yield user
    api_fixture.delete(f"{url}/{user['id']}")
