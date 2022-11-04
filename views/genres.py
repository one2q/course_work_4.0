from flask_restx import Resource, Namespace
from flask import request, abort

from dao.model.genre import GenreSchema
from implemented import genre_service
from decorators import auth_required
genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
	# @auth_required
	def get(self):
		genre = genre_service.get_all()
		result = GenreSchema(many=True).dump(genre)
		return result, 200

	# @admin_required
	def post(self):
		data = request.json
		genre_service.create(data)
		return 'Ok', 201


@genre_ns.route('/<int:pk>/')
class GenreView(Resource):
	@auth_required
	def get(self, pk):
		genre = genre_service.get_one(pk)
		if not genre:
			abort(404)
		result = GenreSchema().dump(genre)
		return result, 200

	# @admin_required
	def put(self, pk: int):
		data = request.json
		if "id" not in data:
			data["id"] = pk
		genre_service.update(data)
		return "", 204

	# @admin_required
	def delete(self, pk: int):
		genre_service.delete(pk)
		return '', 204
