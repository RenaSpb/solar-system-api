def test_get_all_planets_returns_empty_list(client):
    response = client.get("/planets")
    assert response.status_code == 200
    assert response.get_json() == []

def test_create_planet_success(client):
    print("🚀 [TEST] 开始创建星球 Nibiru")

    planet_data = {
        "name": "Nibiru",
        "description": "A mysterious wandering planet",
        "size": "unknown"
    }

    response = client.post("/planets", json=planet_data)
    print("📡 [TEST] 收到响应")

    response_data = response.get_json()
    print("🔍 [TEST] 响应数据:", response_data)

    assert response.status_code == 201
    assert "id" in response_data
    assert response_data["message"] == "Planet Nibiru created"



def test_create_planet_missing_field(client):
    incomplete_data = {
        "name": "IncompletePlanet",
        "size": "small"
        # description is missing
    }

    response = client.post("/planets", json=incomplete_data)
    response_data = response.get_json()

    assert response.status_code == 400
    assert "error" in response_data

def test_create_planet_empty_request(client):
    response = client.post("/planets", data="")  # No JSON
    assert response.status_code == 400

