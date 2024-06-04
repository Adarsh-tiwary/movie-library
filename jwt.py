# utils/jwt.py
import jwt
from datetime import datetime, timedelta
from config import Config

def generate_jwt(email):
    payload = {
        'email': email,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['email']
    except jwt.ExpiredSignatureError:
        raise Exception('Token has expired')
    except jwt.InvalidTokenError:
        raise Exception('Invalid token')


