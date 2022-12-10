from unittest.mock import MagicMock

import pytest as pytest

from config import Config
from app import create_app
from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre


@pytest.fixture
def director_dao():
	director_dao = DirectorDAO(None)

	director1 = Director(id=1, name='Иван')
	director2 = Director(id=2, name='Петр')
	director3 = Director(id=3, name='Тест')

	director_dao.get_one = MagicMock(return_value=director1)
	director_dao.get_all = MagicMock(return_value=[director1, director2, director3])
	director_dao.create = MagicMock()

	return director_dao


@pytest.fixture
def genre_dao():
	genre_dao = GenreDAO(None)

	genre1 = Genre(id=1, name='Комедия')
	genre2 = Genre(id=2, name='Ужасы')
	genre3 = Genre(id=3, name='Тест')

	genre_dao.get_one = MagicMock(return_value=genre1)
	genre_dao.get_all = MagicMock(return_value=[genre1, genre2, genre3])

	return genre_dao


#########################################

@pytest.fixture()
def app():
	app = create_app(Config())
	app.config.update({
		"TESTING": True,
	})

	# other setup can go here

	yield app

	# clean up / reset resources here


@pytest.fixture()
def client(app):
	return app.test_client()
