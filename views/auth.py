from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import auth_service, user_service

auth_ns = Namespace('auth')
user_schema = UserSchema()


@auth_ns.route('/register/')
class AuthViews(Resource):
	# Register new user
	def post(self):
		"""
		Register a new user. {"email": str, "password": str}
		"""
		data = request.json
		email = data.get("email", None)
		password = data.get("password", None)
		if None in (email, password):
			return 'Enter email and password', 400
		try:
			user = user_service.create(data)
			return user_schema.dump(user), 201
		except Exception as e:
			return 'Unable to create this user, try another email', 400


# User authentication
@auth_ns.route('/login/')
class AuthViews(Resource):
	# Get tokens
	def post(self):
		"""
		Identification {"email": str, "password": str}
		"""
		data = request.json

		email = data.get("email", None)
		password = data.get("password", None)

		if email is None or password is None:
			return 'Enter email and password', 400
		if user_service.compare_passwords(email, password):
			tokens = auth_service.generate_tokens(email)
			return tokens, 201
		return 'Password is not correct, try again', 403

	# Refresh tokens
	def put(self):
		"""
		Authentication {"access_token": str, "refresh_token": str}
		"""
		data = request.json
		token = data.get('refresh_token')

		tokens = auth_service.refresh_token(token)

		return tokens, 201
