# controllers/auth_controller.py
from flask import request, jsonify
from models import User
from utils.jwt import generate_jwt

def register():
    data = request.get_json()
    user = User(data['username'], data['email'], data['password'])
    user.save()
    token = generate_jwt(user.email)
    return jsonify({'token': token})

def login():
    data = request.get_json()
    user = User.find_by_email(data['email'])
    if user and User.check_password(user['password'], data['password']):
        token = generate_jwt(user['email'])
        return jsonify({'token': token})
    return jsonify({'msg': 'Invalid credentials'}), 401

