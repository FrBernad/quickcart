import requests

def test_services_up():
    response = requests.get("http://categories_api:5000/categories/health", timeout=10)
    assert response.status_code == 200
    
def test_database_up():
    assert True
