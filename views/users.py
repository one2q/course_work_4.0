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


	@auth_required
	def patch(self):
		data = request.json
		password = data.get("password", None)
		email = data.get("email", None)

		if password or email:
			return "To change email or password use another service", 403

		# Get email from token
		user_token = request.headers["Authorization"]
		email = user_service.get_email_from_token(user_token)

		data["email"] = email

		# Update users data
		user = user_service.update(data)

		updated_data = {"password": user_service.get_hash(new_password), "email": email}

		user = user_service.update(updated_data)
		if not user:
			return abort(404)
		return user_schema.dump(user)


@user_ns.route('/password/')
class UsersView(Resource):
	"""
		Change users password, enter json {"old_password": "test"  and "new_password": "test1"}
	"""

	# @auth_required
	def put(self):
		data = request.json
		old_password = data.get("old_password")
		new_password = data.get("new_password")

		# Get email from token
		user_token = request.headers["Authorization"]
		email = user_service.get_email_from_token(user_token)

		data["email"] = email

		# Check if user enter correct password
		if not user_service.compare_passwords(email, old_password):
			return 'Enter correct password', 400

		updated_data = {"password": user_service.get_hash(new_password), "email": email}

		user = user_service.update(updated_data)
		if not user:
			return abort(404)
		return user_schema.dump(user)
