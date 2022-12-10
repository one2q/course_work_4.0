from flask_restx import Resource, Namespace
from flask import request, abort

from dao.model.genre import GenreSchema
from implemented import genre_service
from decorators import auth_required
genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
	@auth_required
	def get(self):
		"""
		Get all genres
		"""
		try:
			genre = genre_service.get_all()
			result = GenreSchema(many=True).dump(genre)
			return result, 200
		except Exception as e:
			print(e)


@genre_ns.route('/<int:pk>/')
class GenreView(Resource):
	@auth_required
	def get(self, pk: int):
		"""
		Get one genre by id
		"""
		try:
			genre = genre_service.get_one(pk)
			result = GenreSchema().dump(genre)
			return result, 200
		except Exception as e:
			print(e)

