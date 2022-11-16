import calendar
import datetime

import jwt
from flask_restx import abort

from constants import JWT_SECRET, JWT_ALGORITHM
from service.user import UserService


class AuthService:
	def __init__(self, service: UserService):
		self.user_service = service

	def generate_tokens(self, email: str) -> dict:
		"""
		This function is generate access and refresh tokens
		"""
		user = self.user_service.get_by_email(email)
		# Check if where is a user
		if user is None:
			raise abort(404)

		data = {
			"email": user.email
		}
		# 30 min token
		min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
		data["exp"] = calendar.timegm(min30.timetuple())
		access_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

		# 130 day token
		day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
		data["exp"] = calendar.timegm(day130.timetuple())
		refresh_token = jwt.encode(payload=data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

		tokens = {
			"access_token": access_token,
			"refresh_token": refresh_token
		}

		return tokens

	# Generate new access token
	def refresh_token(self, refresh_token):
		data = jwt.decode(refresh_token, JWT_SECRET, JWT_ALGORITHM)
		email = data.get("email")
		return self.generate_tokens(email)
