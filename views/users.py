from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):

	def get(self):
		username = request.args.get('username')
		if username:
			return users_schema.dump(user_service.get_by_username(username))

		return users_schema.dump(user_service.get_all())

	def post(self):
		data = request.json
		user_service.create(data)
		return '', 201


@user_ns.route('/<int:pk>')
class UserView(Resource):
	def get(self, pk):
		return user_schema.dump(user_service.get_one(pk))
