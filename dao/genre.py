from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, pk: int):
        return self.session.query(Genre).get(pk)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_data):
        genre = Genre(**genre_data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, pk: int):
        genre = self.get_one(pk)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_data):
        pk = genre_data.get("id")
        self.session.query(Genre).filter(Genre.id == pk).update(genre_data)
        self.session.commit()
