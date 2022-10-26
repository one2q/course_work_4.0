from flask import request, abort
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
	# Get user by email
	def get(self):
		email = request.args.get('email')
		if email:
			return users_schema.dump(user_service.get_by_email(email))
		abort(404)

	def patch(self):
		data = request.json
		password = data.get("password")
		if password:
			return "No no no", 403

		user = user_service.update(data)
		if not user:
			return abort(404)
		return user_schema.dump(user)


	def put(self):
		pass
		# user = user_service.get_by_email(email)


# @user_ns.route('/<int:pk>')
# class UserView(Resource):
# 	def get(self, pk):
# 		return user_schema.dump(user_service.get_one(pk))
