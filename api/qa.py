import requests

url = "https://reqres.in/api/users/1"

response = requests.get(url, headers={"x-api-key": "reqres_167601fe554b4ed7beb6755668211cbb"}, params={"page": 2, "per_page": 3})

data = response.json()

assert response.status_code == 200

assert "id" in data["data"]
assert "email" in data["data"]

assert isinstance(data["data"]["id"], int)
assert isinstance(data["data"]["email"], str)

assert data["data"]["id"] == 1

assert response.elapsed.total_seconds() < 2.0

print("все проверки прошли")

print(response.status_code, data, "12121212", data["data"]
      )