import pytest
import json
import os
url = "https://reqres.in/api/users"


with open(os.path.join(os.path.dirname(__file__), "test_data.json")) as f:
    data = json.load(f)

users = [(u["id"], u["email"]) for u in data["users"]]

@pytest.mark.parametrize("user_id, expected_status", [
    (1, 200),
    (2, 200),
    (9999, 404),
])
def test_user_status(api_fixture, user_id, expected_status):
    response = api_fixture.get(f"{url}/{user_id}")
    assert response.status_code == expected_status

@pytest.mark.parametrize("user_id, email", users)
def test_json(api_fixture, user_id, email):
    response = api_fixture.get(f"{url}/{user_id}")
    assert response.json()["data"]["email"] == email
    assert response.json()["data"]["id"] == user_id


@pytest.mark.smoke
def test_user_created(api_fixture):
    response = api_fixture.get(f"{url}/1")
    assert response.status_code == 200

@pytest.mark.regression
def test_user_status_regression(api_fixture):
    response = api_fixture.get(f"{url}/9999")
    assert response.status_code == 404

@pytest.mark.skip(reason="счастье разрушил сам")
def test_qq(api_fixture):
    pass

@pytest.mark.xfail()
@pytest.mark.parametrize("user_id, expected_status", [
    (1, 404),
    (2, 999)
])
def test_failed(api_fixture, user_id, expected_status):
    response = api_fixture.get(f"{url}/{user_id}")
    assert response.status_code == expected_status