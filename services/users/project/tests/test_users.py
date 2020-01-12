def test_users_ping(test_app):
    """Ensure users /ping route behaves correctly"""
    client = test_app.test_client()
    resp = client.get("/users/ping")
    data = resp.json
    assert resp.status_code == 200
    assert data["status"] == "success"
    assert data["message"] == "pong!"
