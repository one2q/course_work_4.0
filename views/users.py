from flask import request, abort
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
	# Get user by email
	@auth_required
	def get(self):
		user_token = request.headers["Authorization"]
		email = user_service.get_email_from_token(user_token)

		if email:
			return user_schema.dump(user_service.get_by_email(email))
		abort(404)
	# Update user's information
	@auth_required
	def patch(self):
		data = request.json
		password = data.get("password")
		# Check if where any password
		if password:
			return "No no no", 403

		# Get email from token
		user_token = request.headers["Authorization"]
		email = user_service.get_email_from_token(user_token)

		data["email"] = email

		# Update users data
		user = user_service.update(data)
		if not user:
			return abort(404)
		return user_schema.dump(user)


@user_ns.route('/password/')
class UsersView(Resource):
	# Update user's password
	@auth_required
	def put(self):
		data = request.json
		password = data.get("password")

		# Get email from token
		user_token = request.headers["Authorization"]
		email = user_service.get_email_from_token(user_token)

		data["email"] = email

		user = user_service.update(data)
		if not user:
			return abort(404)
		return user_schema.dump(user)
