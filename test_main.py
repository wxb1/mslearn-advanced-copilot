from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_for_country():
    # Portugal has two entries in the sample data
    response = client.get("/countries/Portugal/cities")
    assert response.status_code == 200
    assert sorted(response.json()) == ["Lisbon", "Porto"]


def test_cities_for_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert response.json() == ["Seville"]


def test_cities_unknown_country():
    response = client.get("/countries/Narnia/cities")
    assert response.status_code == 404
    assert response.json()["detail"] == "Country not found"