# routes/movie_list_routes.py
from flask import Blueprint
from controllers.movie_list_controller import create_list, get_lists, get_public_list

movie_list_bp = Blueprint('movie_list', __name__)

movie_list_bp.route('/', methods=['POST'])(create_list)
movie_list_bp.route('/', methods=['GET'])(get_lists)
movie_list_bp.route('/<list_id>', methods=['GET'])(get_public_list)

