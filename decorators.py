import jwt as jwt
from flask import request, abort

from constants import JWT_ALGORITHM, JWT_SECRET


def auth_required(func):
	"""
	This decorator check is it authorized user or not
	"""
	def inner(*args, **kwargs):
		if "Authorization" not in request.headers:
			abort(401)
		data = request.headers["Authorization"]
		token = data.split("Bearer ")[-1]
		try:
			jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
			return func(*args, **kwargs)
		except:
			abort(401)
	return inner

# def admin_required(func):
# 	"""
# 	This decorator check role of user and if it is not admin
# 	access is denied
# 	"""
# 	def inner(*args, **kwargs):
# 		if "Authorization" not in request.headers:
# 			abort(401)
# 		data = request.headers["Authorization"]
# 		token = data.split("Bearer ")[-1]
# 		try:
# 			decoded_data = jwt.decode(token, JWT_SECRET, JWT_ALGORITHM)
# 			role = decoded_data.get('role')
# 		except:
# 			abort(401)
# 		if role != 'admin':
# 			abort(403)
# 		return func(*args, **kwargs)
# 	return inner
