import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from app.config.app import create_app


@pytest.fixture(scope="session", autouse=True)
async def initialize_tests():
    await initializer(["app.repository.models"], db_url="sqlite://:memory:")
    yield
    await finalizer()


@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)


def test_create_hanzi_without_relationships(client):
    hanzi_data = {
        "hanzi_text": "你",
        "pinyin": "nǐ",
        "meaning": "you",
        "hsk_level": 1
    }
    
    response = client.post("/api/hanzi/", json=hanzi_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["hanzi_text"] == "你"
    assert data["pinyin"] == "nǐ"
    assert data["meaning"] == "you"
    assert data["hsk_level"] == 1
    assert data["image_file"] is None
    assert data["category"] is None


def test_create_hanzi_with_category(client):
    category_data = {
        "name": "Basic Pronouns",
        "hsk_level": 1
    }
    category_response = client.post("/api/categories/", json=category_data)
    category_id = category_response.json()["id"]
    
    hanzi_data = {
        "hanzi_text": "我",
        "pinyin": "wǒ",
        "meaning": "I, me",
        "hsk_level": 1,
        "category_id": category_id
    }
    
    response = client.post("/api/hanzi/", json=hanzi_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    assert response.status_code == 200
    data = response.json()
    assert data["hanzi_text"] == "我"
    assert data["category"]["id"] == category_id
    assert data["category"]["name"] == "Basic Pronouns"