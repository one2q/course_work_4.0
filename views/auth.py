from flask import request
from flask_restx import Resource, Namespace

from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthViews(Resource):
	def post(self):
		data = request.json
		username = data.get("username", None)
		password = data.get("password", None)
		if username is None or password is None:
			return '', 400
		tokens = auth_service.generate_tokens(username, password)
		return tokens, 201

	def put(self):
		data = request.json
		token = data.get('refresh_token')

		tokens = auth_service.refresh_token(token)

		return tokens, 201
