from dao.favorite_movies import FavoriteMoviesDAO


class FavoriteMoviesService:
	def __init__(self, dao: FavoriteMoviesDAO):
		self.dao = dao

	def create(self, data):
		favorite = self.dao.create(data)
		return favorite

	def delete(self, data):
		self.dao.delete(data)