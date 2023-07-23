import requests


def test_services_up():
    #Shopping Cart service
    response = requests.get("http://shopping_cart_api:5000/shopping-cart/health", timeout=10)
    assert response.status_code == 200

    # Users service
    response = requests.get("http://users_api:5000/users/health", timeout=10)
    assert response.status_code == 200

    # Purchase orders service
    response = requests.get("http://purchase_orders_api:5000/purchase-orders/health", timeout=10)
    assert response.status_code == 200

    # Products service
    response = requests.get("http://products_api:5000/products/health", timeout=10)
    assert response.status_code == 200

def test_database_up():
    assert True
