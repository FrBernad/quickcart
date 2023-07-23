import requests


def _test_api_health(service_name, path):
    response = requests.get(f"http://{service_name}:5000/{path}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_purchase_orders_api_health():
    _test_api_health("purchase_orders_api", "purchase-orders")


def test_shopping_cart_api_health():
    _test_api_health("shopping_cart_api", "shopping-cart")


def test_users_api_health():
    _test_api_health("users_api", "users")


def test_products_api_health():
    _test_api_health("products_api", "products")
