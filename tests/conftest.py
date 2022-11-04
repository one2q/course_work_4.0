from unittest.mock import MagicMock

import pytest as pytest

from dao.director import DirectorDAO
from dao.model.director import Director


@pytest.fixture
def director_dao():
	director_dao = DirectorDAO(None)

	director1 = Director(id=1, name='Иван')
	director2 = Director(id=2, name='Петр')
	director3 = Director(id=3, name='Тест')

	director_dao.get_one = MagicMock(return_value=director1)
	director_dao.get_all = MagicMock(return_value=[director1, director2, director3])

	return director_dao
