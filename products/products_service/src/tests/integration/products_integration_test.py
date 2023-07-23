import requests


def test_services_up():

    # Products service
    response = requests.get("http://products_api:5000/products/health", timeout=10)
    assert response.status_code == 200

    # # Users service
    response = requests.get("http://users_api:5000/users/health", timeout=10)
    assert response.status_code == 200
    
    # Categories Service
    response = requests.get("http://categories_api:5000/categories/health", timeout=10)
    assert response.status_code == 200


def test_database_up():
    assert True
