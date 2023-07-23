import requests


def _test_api_health(path):
    response = requests.get(f"http://api_gateway:80/{path}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_categories_api_health():
    _test_api_health("categories")


def test_products_api_health():
    _test_api_health("products")


def test_reviews_api_health():
    _test_api_health("reviews")


def test_purchase_orders_api_health():
    _test_api_health("purchase-orders")


def test_shopping_cart_api_health():
    _test_api_health("shopping-cart")


def test_users_api_health():
    _test_api_health("users")
