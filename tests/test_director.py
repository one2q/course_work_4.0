import json

test_result = {
	"id": 1,
	"name": "Тейлор Шеридан"
}


# Before test do not forget to comment auth decorator


def test_request_example(client):
	response = client.get("/directors/1/", json={
		"id": 1,
		"name": "Тейлор Шеридан"
	})
	assert test_result == response.json, "Ошибка получения одного директора"
