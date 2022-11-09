def test_alive(test_app):
    response = test_app.get("/alive")
    assert response.status_code == 200
    assert response.json() == {"message": "alive"}
