from flask import request
from flask_restx import Resource, Namespace

from decorators import auth_required
from implemented import favorite_movies_service

favorite_ns = Namespace('favorites')


@favorite_ns.route('/movies/')
class FavoritesView(Resource):
	@auth_required
	def post(self):
		data = request.json
		filter = {
			"user_id": data.get("user_id"),
			"movie_id": data.get("movie_id")
		}
		favorite_movies_service.create(filter)
		return '', 201

	@auth_required
	def delete(self):
		data = request.json
		filter = {
			"user_id": data.get("user_id"),
			"movie_id": data.get("movie_id")
		}
		favorite_movies_service.delete(filter)
		return '', 200
