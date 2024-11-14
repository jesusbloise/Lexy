import pytest
from app import app  
from flask import jsonify


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)  


def test_get_comments(client):
    response = client.get('/comments')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_albums(client):
    response = client.get('/albums')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_photos(client):
    response = client.get('/photos')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)
