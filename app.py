from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS

from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.favorite_movies import favorite_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object: Config) -> Flask:
	app = Flask(__name__)
	app.config.from_object(config_object)
	register_extensions(app)
	return app


def register_extensions(app: Flask) -> None:
	db.init_app(app)
	api = Api(app, doc='/', title='API')
	api.add_namespace(director_ns)
	api.add_namespace(genre_ns)
	api.add_namespace(movie_ns)
	api.add_namespace(user_ns)
	api.add_namespace(auth_ns)
	api.add_namespace(favorite_ns)


app = create_app(Config())
CORS(app)
migrate = Migrate(app, db, render_as_batch=True)

# with app.app_context():
# 	db.create_all()

if __name__ == '__main__':
	app.run(port=5000)
