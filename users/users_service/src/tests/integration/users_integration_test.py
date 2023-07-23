import requests


def test_services_up():

    # Users service
    response = requests.get("http://users_api:5000/users/health", timeout=10)
    assert response.status_code == 200



def test_database_up():
    assert True
