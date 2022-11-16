import base64
import hashlib
import hmac

import jwt

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, JWT_SECRET, JWT_ALGORITHM
from dao.user import UserDAO


class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_all(self):
		return self.dao.get_all()

	def get_one(self, pk: int):
		return self.dao.get_one(pk)

	def create(self, data: dict):
		data["password"] = self.get_hash(data["password"])
		return self.dao.create(data) # создать свою ошибку

	def get_by_email(self, email: str):
		return self.dao.get_by_email(email)

	def update(self, user_data: dict):
		return self.dao.update(user_data)

	@staticmethod
	def get_hash(password: str):
		result = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
			)
		return base64.b64encode(result)

	@staticmethod
	def get_email_from_token(user_token) -> str:
		token = user_token.split("Bearer ")[-1]
		decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
		email = decoded_data.get('email')

		return email

	def compare_passwords(self, email, old_password):
		user = self.get_by_email(email)
		user_password = user.password
		hash_old_password = self.get_hash(old_password)
		return user_password == hash_old_password


