from dao.model.favorite_movie import FavoriteMovies


class FavoriteMoviesDAO:
	"""
		This class is work with db and provide CRUD
	"""

	def __init__(self, session):
		self.session = session

	def create(self, data):
		favorite = FavoriteMovies(**data)
		self.session.add(favorite)
		self.session.commit()
		return favorite

	def delete(self, data):
		user_id = data.get("user_id")
		movie_id = data.get("movie_id")

		favorite = self.session.query(FavoriteMovies).filter(FavoriteMovies.user_id == user_id and
		                                                     FavoriteMovies.movie_id == movie_id).first()
		self.session.delete(favorite)
		self.session.commit()