import requests
url = "https://reqres.in/api/users"
header = {"x-api-key": "reqres_167601fe554b4ed7beb6755668211cbb"}

def test_response_code_check(api_fixture):
    response = requests.get(f"{url}/1", headers=header, timeout=10)
    assert response.status_code == 200

def test_user_email(api_fixture):
    response = api_fixture.get(f"{url}/2")
    assert "email" in response.json()["data"]

def test_user_id_correct(api_fixture):
    response = api_fixture.get(f"{url}/2")
    assert response.json()["data"]["id"] == 2

def test_incorrect_user(api_fixture):
    response = api_fixture.get(f"{url}/2")
    assert response.status_code == 200

def test_post_query(created_user):
    assert created_user["name"] == "xxasdxc"
    assert created_user["job"] == "qa-engineer"
    assert "id" in created_user
    assert isinstance(created_user["id"], str)

def test_delete_user(api_fixture):
    response = api_fixture.delete(f"{url}/2")
    assert response.status_code == 204
    assert response.text == ""

