import math


def test_prediction(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={
            "median_income_in_block": 8.3252,
            "median_house_age_in_block": 41,
            "average_rooms": 6,
            "average_bedrooms": 1,
            "population_per_block": 322,
            "average_house_occupancy": 2.55,
            "block_latitude": 37.88,
            "block_longitude": -122.23,
        },
    )
    assert response.status_code == 200
    assert "median_house_value" in response.json()
    assert "currency" in response.json()
    assert math.isclose(response.json().get("median_house_value"), 422005, rel_tol=1.0)


def test_prediction_nopayload(test_client) -> None:
    response = test_client.post(
        "/api/model/predict",
        json={},
    )
    assert response.status_code == 422
