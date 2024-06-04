
# app.py
from flask import Flask
from flask_cors import CORS
from utils.db import init_db
from routes.auth_routes import auth_bp
from routes.movie_list_routes import movie_list_bp

app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)

init_db(app)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(movie_list_bp, url_prefix='/api/movielist')

if __name__ == '__main__':
    app.run(debug=True)
