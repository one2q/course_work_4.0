from flask_restx import Resource, Namespace, fields
from flask import request

from dao.model.director import DirectorSchema
from decorators import auth_required
from implemented import director_service

director_ns = Namespace('directors')


director_model = director_ns.model(
	'Director',
	{
		'id': fields.Integer(),
		'name': fields.String()
	}
)


@director_ns.route('/')
class DirectorsView(Resource):
	# @director_ns.marshal_list_with(director_model)
	@director_ns.expect(director_model)
	@auth_required
	def get(self):
		"""
		Get all directors
		"""
		try:
			director = director_service.get_all()
			result = DirectorSchema(many=True).dump(director)
			return result, 200
		except Exception as e:
			print(e)

	# def post(self):
	# 	"""
	# 	Create a new director
	# 	"""
	# 	data = request.json
	# 	director_service.create(data)
	# 	return 'Ok', 201


@director_ns.route('/<int:pk>/')
class DirectorView(Resource):
	@director_ns.expect(director_model)
	@auth_required
	def get(self, pk: int):
		"""
		Get one director
		"""
		try:
			director = director_service.get_one(pk)
			result = DirectorSchema().dump(director)
			return result, 200

		except Exception as e:
			print(e)

	# def put(self, pk: int):
	# 	data = request.json
	# 	if "id" not in data:
	# 		data["id"] = pk
	# 	director_service.update(data)
	# 	return "", 204
	#
	#
	# def delete(self, pk: int):
	# 	director_service.delete(pk)
	# 	return '', 204
