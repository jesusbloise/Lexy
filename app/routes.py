import requests
from app import app
from flask import jsonify

BASE_URL = "https://jsonplaceholder.typicode.com"  

@app.route('/posts', methods=['GET'])
def get_posts():
    try:
        response = requests.get(f"{BASE_URL}/posts")
        response.raise_for_status()  
        return jsonify(response.json())  
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/comments', methods=['GET'])
def get_comments():
    try:
        response = requests.get(f"{BASE_URL}/comments")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/albums', methods=['GET'])
def get_albums():
    try:
        response = requests.get(f"{BASE_URL}/albums")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/photos', methods=['GET'])
def get_photos():
    try:
        response = requests.get(f"{BASE_URL}/photos")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/todos', methods=['GET'])
def get_todos():
    try:
        response = requests.get(f"{BASE_URL}/todos")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    try:
        response = requests.get(f"{BASE_URL}/users")
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
