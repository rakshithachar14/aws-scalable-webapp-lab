from app import app

def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_homepage():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Welcome!"

def test_how_are_you():
    client = app.test_client()
    response = client.get("/how-are-you")

    assert response.status_code == 200
    assert response.get_data(as_text=True) == "I am good, how about you?"
