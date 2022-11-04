from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from decorators import auth_required

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):

	@auth_required
	def get(self):
		status = request.args.get("status")
		page = request.args.get("page")

		filters = {
			"status": status,
			"page": page,
		}
		all_movies = movie_service.get_all(filters)
		result = movies_schema.dump(all_movies)
		return result, 200

	# @admin_required
	def post(self):
		req_json = request.json
		try:
			movie = movie_service.create(req_json)
			return "", 201, {"location": f"/movies/{movie.id}"}
		except Exception as e:
			return e


@movie_ns.route('/<int:pk>')
class MovieView(Resource):
	@auth_required
	def get(self, pk: int):
		try:
			movie = movie_service.get_one(pk)
			result = movie_schema.dump(movie)
			return result, 200
		except Exception as e:
			return e

	# @admin_required
	def put(self, pk: int):
		req_json = request.json
		if "id" not in req_json:
			req_json["id"] = pk
		movie_service.update(req_json)
		return "", 204

	# @admin_required
	def delete(self, pk: int):
		movie_service.delete(pk)
		return "", 204
