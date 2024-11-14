import pytest
from ..app import app  # Asegúrate de que esta importación esté correcta
from flask import jsonify

# Usamos el cliente de prueba de Flask para simular solicitudes
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Prueba para la ruta '/posts'
def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    assert isinstance(response.json, list)  # Verifica que la respuesta sea una lista

# Prueba para la ruta '/comments'
def test_get_comments(client):
    response = client.get('/comments')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Prueba para la ruta '/albums'
def test_get_albums(client):
    response = client.get('/albums')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Prueba para la ruta '/photos'
def test_get_photos(client):
    response = client.get('/photos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Prueba para la ruta '/todos'
def test_get_todos(client):
    response = client.get('/todos')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Prueba para la ruta '/users'
def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert isinstance(response.json, list)
