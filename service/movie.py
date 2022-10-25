from dao.movie import MovieDAO


class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_one(self, bid):
		return self.dao.get_one(bid)

	def get_all(self, filters):
		sort, page = False, False
		if filters.get("status") is not None:
			sort = True
		if filters.get("page") is not None:
			page = filters.get("page")
		movies = self.dao.get_all(sort, page)

		return movies

	def create(self, movie_data):
		return self.dao.create(movie_data)

	def update(self, movie_data):
		self.dao.update(movie_data)
		return self.dao

	def delete(self, pk: int):
		self.dao.delete(pk)
