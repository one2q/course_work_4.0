from dao.model.director import Director


class DirectorDAO:
	"""
		This class is work with db and provide CRUD
	"""
	def __init__(self, session):
		self.session = session

	def get_one(self, pk: int):
		return self.session.query(Director).get(pk)

	def get_all(self):
		return self.session.query(Director).all()

	# def create(self, director_data):
	# 	director = Director(**director_data)
	# 	self.session.add(director)
	# 	self.session.commit()
	# 	return director
	#
	# def delete(self, pk):
	# 	director = self.get_one(pk)
	# 	self.session.delete(director)
	# 	self.session.commit()
	#
	# def update(self, director_data):
	# 	pk = director_data.get("id")
	# 	self.session.query(Director).filte(Director.id == pk).update(director_data)
	# 	self.session.commit()
