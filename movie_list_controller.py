# controllers/movie_list_controller.py
from flask import request, jsonify
from models import MovieList
from middleware.auth import token_required

@token_required
def create_list(current_user):
    data = request.get_json()
    movie_list = MovieList(current_user['_id'], data['name'], data['movies'], data['is_public'])
    movie_list.save()
    return jsonify({'msg': 'Movie list created'})

@token_required
def get_lists(current_user):
    lists = MovieList.find_by_user(current_user['_id'])
    return jsonify([list for list in lists])

def get_public_list(list_id):
    movie_list = MovieList.find_public_by_id(list_id)
    if movie_list:
        return jsonify(movie_list)
    return jsonify({'msg': 'List not found'}), 404


