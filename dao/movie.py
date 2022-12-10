from dao.model.movie import Movie


class MovieDAO:
	"""
	This class is work with db and provide CRUD
	"""
	def __init__(self, session):
		self.session = session

	def get_one(self, pk: int):
		return self.session.query(Movie).get(pk)

	def get_all(self, sort: bool = False, page=False):
		"""
		This method give us a list of movies depend on a requested parameters
		:param sort: if need sort movie by year set True
		:param page: if need paginate, set page True
		:return: movies sorted by parameters
		"""
		if page and sort:
			movies = self.session.query(Movie).order_by(Movie.year.desc()).paginate(page=int(page), per_page=12).items
		elif sort:
			movies = self.session.query(Movie).order_by(Movie.year.desc()).all()
		elif page:
			movies = self.session.query(Movie).paginate(page=int(page), per_page=12).items
		else:
			movies = self.session.query(Movie).all()
		return movies

	# def create(self, movie_data: dict):
	# 	movie = Movie(**movie_data)
	# 	self.session.add(movie)
	# 	self.session.commit()
	# 	return movie
	#
	# def delete(self, pk: int):
	# 	movie = self.get_one(pk)
	# 	self.session.delete(movie)
	# 	self.session.commit()
	#
	# def update(self, movie_data: dict):
	# 	pk = movie_data.get("id")
	# 	self.session.query(Movie).filter(Movie.id == pk).update(movie_data)
	# 	self.session.commit()
	# 	return self.get_one(pk)
