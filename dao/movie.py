from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk: int):
        return self.session.query(Movie).get(pk)

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_director_id(self, pk: int):
        return self.session.query(Movie).filter(Movie.director_id == pk).all()

    def get_by_genre_id(self, pk: int):
        return self.session.query(Movie).filter(Movie.genre_id == pk).all()

    def get_by_year(self, year: int):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def create(self, movie_data):
        movie = Movie(**movie_data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, pk: int):
        movie = self.get_one(pk)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        pk = movie_data.get("id")
        self.session.query(Movie).filter(Movie.id == pk).update(movie_data)
        self.session.commit()
        return self.get_one(pk)

        #TODO do not forget to delete this vvvvvvvv

        # movie.title = movie_d.get("title")
        # movie.description = movie_d.get("description")
        # movie.trailer = movie_d.get("trailer")
        # movie.year = movie_d.get("year")
        # movie.rating = movie_d.get("rating")
        # movie.genre_id = movie_d.get("genre_id")
        # movie.director_id = movie_d.get("director_id")
        # self.session.add(movie)
        # self.session.commit()
