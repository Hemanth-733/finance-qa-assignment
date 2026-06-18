import requests

BASE_URL = "https://reqres.in/api"

def test_get_user():
    response = requests.get(f"{BASE_URL}/users/2")
    assert response.status_code == 200

    data = response.json()
    assert data["data"]["id"] == 2


def test_login_failure():
    payload = {
        "email": "peter@klaven"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=payload
    )

    assert response.status_code == 400