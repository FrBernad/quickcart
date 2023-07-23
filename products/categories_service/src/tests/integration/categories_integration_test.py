import requests


def _test_api_health(service_name, path):
    response = requests.get(f"http://{service_name}:5000/{path}/health", timeout=5)
    assert response.status_code == 200
    assert response.json()["status"] == "OK"


def test_categories_api_health():
    _test_api_health("categories_api", "categories")
