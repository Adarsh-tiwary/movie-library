# middleware/auth.py
from functools import wraps
from flask import request, jsonify
from models import User
from utils.jwt import decode_jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-auth-token')
        if not token:
            return jsonify({'msg': 'Token is missing'}), 401
        try:
            user_email = decode_jwt(token)
            current_user = User.find_by_email(user_email)
        except:
            return jsonify({'msg': 'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated


