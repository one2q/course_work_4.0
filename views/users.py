import jwt
from flask import request, abort
from flask_restx import Resource, Namespace

from constants import JWT_SECRET, JWT_ALGORITHM
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
		user_data = request.headers["Authorization"]
		token = user_data.split("Bearer ")[-1]
		decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
		email = decoded_data.get('email')

		if email:
			return user_schema.dump(user_service.get_by_email(email))
		abort(404)

	@auth_required
	def patch(self):
		data = request.json
		password = data.get("password")
		# Check if where any password
		if password:
			return "No no no", 403

		# Get email from token
		user_data = request.headers["Authorization"]
		token = user_data.split("Bearer ")[-1]
		decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
		email = decoded_data.get('email')
		data["email"] = email

		# Update users data
		user = user_service.update(data)
		if not user:
			return abort(404)
		return user_schema.dump(user)


@user_ns.route('/password/')
class UsersView(Resource):

	@auth_required
	def put(self):
		data = request.json
		password = data.get("password")

		# Get email from token
		user_data = request.headers["Authorization"]
		token = user_data.split("Bearer ")[-1]
		decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
		email = decoded_data.get('email')
		data["email"] = email

		user = user_service.update(data)
		if not user:
			return abort(404)
		return user_schema.dump(user)
