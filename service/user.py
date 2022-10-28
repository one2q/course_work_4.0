import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
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
		return self.dao.create(data)

	def get_by_email(self, email: str):
		return self.dao.get_by_email(email)

	def update(self, user_data: dict):
		return self.dao.update(user_data)

	def get_hash(self, password: str):
		result = hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),  # Convert the password to bytes
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
			)
		return base64.b64encode(result)

	# Compare decode and encode passwords
	def compare_passwords(self, password_hash: bytes | str, password: str) -> bool:
		# Check is password a string and transform it to bytes
		if isinstance(password_hash, str):
			password_hash = password_hash.encode('utf-8')

		decode_password = base64.b64decode(password_hash)
		new_password = base64.b64decode(self.get_hash(password))

		return hmac.compare_digest(decode_password, new_password)



