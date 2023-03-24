from flask import jsonify, request
from app import app, redis_store

@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Welcome to this API"}), 200

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json.get('id')
    name = request.json.get('name')
    if user_id and name:
        redis_store.hset('users', user_id, name)
        return jsonify({"status": "User created"}), 201
    return jsonify({"error": "Invalid data"}), 400

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = redis_store.hget('users', user_id)
    if user:
        return jsonify({"id": user_id, "name": user.decode('utf-8')}), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['GET'])
def get_all_users():
    users = redis_store.hgetall('users')
    users_dict = {int(user_id): name.decode('utf-8') for user_id, name in users.items()}
    return jsonify(users_dict), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    name = request.json.get('name')
    if redis_store.hexists('users', user_id) and name:
        redis_store.hset('users', user_id, name)
        return jsonify({"status": "User updated"}), 200
    return jsonify({"error": "Invalid data or user not found"}), 400

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if redis_store.hexists('users', user_id):
        redis_store.hdel('users', user_id)
        return jsonify({"status": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404