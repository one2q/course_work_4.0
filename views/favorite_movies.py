from flask import request
from flask_restx import Resource, Namespace

from implemented import favorite_movies_service

favorite_ns = Namespace('/favorites/movies/')


@favorite_ns.route('/<int:pk>')
class FavoritesView(Resource):
	def post(self, pk):
		data = request.json
		filter = {
			"user_id": data.get("user_id"),
			"movie_id": data.get("movie_id")
		}
		favorite_movies_service.create(filter)
		return '', 201

	def delete(self, data):
		data = request.json
		filter = {
			"user_id": data.get("user_id"),
			"movie_id": data.get("movie_id")
		}
		favorite_movies_service.delete(filter)
		return '', 200
