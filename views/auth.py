from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service, user_service

auth_ns = Namespace('auth')


# Register new user
@auth_ns.route('/register')
class AuthViews(Resource):
	def post(self):
		data = request.json
		email = data.get("email", None)
		password = data.get("password", None)
		if email is None or password is None:
			return '', 400
		user_service.create(data)
		return '', 201


# User authentication
@auth_ns.route('/login')
class AuthViews(Resource):
	def post(self):
		data = request.json

		email = data.get("email", None)
		password = data.get("password", None)

		if email is None or password is None:
			return '', 400
		tokens = auth_service.generate_tokens(email, password)
		return tokens, 201

	def put(self):
		data = request.json
		token = data.get('refresh_token')

		tokens = auth_service.refresh_token(token)

		return tokens, 201
