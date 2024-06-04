# models.py
from werkzeug.security import generate_password_hash, check_password_hash
from flask_pymongo import ObjectId
from utils.db import mongo

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def save(self):
        return mongo.db.users.insert_one(self.__dict__)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def check_password(hashed_password, password):
        return check_password_hash(hashed_password, password)

class MovieList:
    def __init__(self, user_id, name, movies, is_public):
        self.user_id = user_id
        self.name = name
        self.movies = movies
        self.is_public = is_public

    def save(self):
        return mongo.db.movie_lists.insert_one(self.__dict__)

    @staticmethod
    def find_by_user(user_id):
        return mongo.db.movie_lists.find({'user_id': user_id})

    @staticmethod
    def find_public_by_id(list_id):
        return mongo.db.movie_lists.find_one({'_id': ObjectId(list_id), 'is_public': True})


