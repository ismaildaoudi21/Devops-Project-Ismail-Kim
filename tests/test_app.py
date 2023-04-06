import pytest
import app
from app import redis_store
import json


@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client


def test_welcome(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to this API"}


def test_get_all_users(client):
    # Insert some test data
    test_users = {
        1: "John Doe",
        2: "Jane Doe"
    }
    for user_id, name in test_users.items():
        redis_store.hset('users', user_id, name)

    response = client.get('/users')
    assert response.status_code == 200
    assert response.json == {str(user_id): name for user_id, name in test_users.items()}

    # Clean up the test data
    for user_id in test_users.keys():
        redis_store.hdel('users', user_id)


def test_healthcheck(client):
    response = client.get('/healthcheck')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}


def test_create_user(client):
    user = {"id": 1, "name": "John Doe"}
    response = client.post('/users', data=json.dumps(user), content_type='application/json')
    assert response.status_code == 201
    assert response.json == {"status": "User created"}


def test_get_user(client):
    user_id = 1
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json == {"id": user_id, "name": "John Doe"}


def test_update_user(client):
    user_id = 1
    updated_data = {"name": "Jane Doe"}
    response = client.put(f'/users/{user_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 200
    assert response.json == {"status": "User updated"}


def test_delete_user(client):
    user_id = 1
    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json == {"status": "User deleted"}


def test_create_user_invalid_data(client):
    user = {"name": "John Doe"}
    response = client.post('/users', data=json.dumps(user), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data"}


def test_get_user_not_found(client):
    user_id = 2
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}


def test_update_user_invalid_data(client):
    user_id = 1
    updated_data = {"invalid_key": "Invalid data"}
    response = client.put(f'/users/{user_id}', data=json.dumps(updated_data), content_type='application/json')
    assert response.status_code == 400
    assert response.json == {"error": "Invalid data or user not found"}


def test_delete_user_not_found(client):
    user_id = 100
    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}
