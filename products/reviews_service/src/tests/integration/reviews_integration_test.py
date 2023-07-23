import requests


def _test_api_health(service_name, path):
    response = requests.get(f"http://{service_name}:5000/{path}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_reviews_api_health():
    _test_api_health("reviews_api", "reviews")


def test_purchase_orders_api_health():
    _test_api_health("purchase_orders_api", "purchase-orders")


def test_users_api_health():
    _test_api_health("users_api", "users")
