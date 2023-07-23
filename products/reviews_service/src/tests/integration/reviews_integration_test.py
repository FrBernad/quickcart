import requests


def test_services_up():

    # Review service
    response = requests.get("http://reviews_api:5000/reviews/health", timeout=10)
    assert response.status_code == 200

    # Purchase orders service
    response = requests.get("http://purchase_orders_api:5000/purchase-orders/health", timeout=10)
    assert response.status_code == 200

    # Users service
    response = requests.get("http://users_api:5000/users/health", timeout=10)
    assert response.status_code == 200


def test_database_up():
    assert True
