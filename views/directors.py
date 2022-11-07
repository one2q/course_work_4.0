from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema
from decorators import auth_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
@director_ns.doc(params={'id': 'director_id', 'name': "director_name"})
class DirectorsView(Resource):
	@auth_required
	def get(self):
		director = director_service.get_all()
		result = DirectorSchema(many=True).dump(director)
		return result, 200

	# @admin_required
	def post(self):
		data = request.json
		director_service.create(data)
		return 'Ok', 201


@director_ns.route('/<int:pk>/')
class DirectorView(Resource):
	@auth_required
	def get(self, pk: int):
		director = director_service.get_one(pk)
		result = DirectorSchema().dump(director)
		return result, 200

	# @admin_required
	def put(self, pk: int):
		data = request.json
		if "id" not in data:
			data["id"] = pk
		director_service.update(data)
		return "", 204

	# @admin_required
	def delete(self, pk: int):
		director_service.delete(pk)
		return '', 204