from dao.model.user import User


class UserDAO:
	"""
	This class is get necessary data from db
	"""
	def __init__(self, session):
		self.session = session

	# Create new object in table user
	def create(self, data):

		user = User(**data)
		self.session.add(user)
		self.session.commit()
		return user

	# Return all users
	def get_all(self):
		return self.session.query(User).all()

	# Return user by username
	def get_by_username(self, username):
		return self.session.query(User).filter(User.username == username).first()

	# Return user by id
	def get_one(self, pk: int):
		return self.session.query(User).get(pk)

	# Delete user by id
	def delete(self, pk):
		user = self.get_one(pk)
		self.session.delete(user)
		self.session.commit()

