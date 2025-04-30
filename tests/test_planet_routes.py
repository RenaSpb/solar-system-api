def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_returns_expected_data(client, two_saved_planets):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "Closest to the Sun",
        "size": "small"
    }

def test_get_one_planet_no_data_returns_404(client):
    response = client.get("/planets/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert response_body["message"] == "planet 1 not found"

def test_get_all_planets_returns_all(client, two_saved_planets):
    response = client.get("/planets")
    response_body = response.get_json()

    assert response.status_code == 200
    assert len(response_body) == 2
    expected_response = [
        {
            "id": 1,
            "name": "Mercury",
            "description": "Closest to the Sun",
            "size": "small"
        },
        {
            "id": 2,
            "name": "Venus",
            "description": "Thick toxic atmosphere",
            "size": "medium"
        }
    ]

    assert response_body == expected_response

def test_post_planet_creates_new_planet(client):
    request_data = {
        "name": "Earth",
        "description": "Home to humans",
        "size": "medium"
    }

    response = client.post("/planets", json=request_data)
    response_body = response.get_json()

    expected_response = {
            "id": 1,
            "name": "Earth",
            "description": "Home to humans",
            "size": "medium"
        }

    assert response_body == expected_response