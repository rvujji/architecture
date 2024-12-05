import pytest
from fastapi import HTTPException
from fastapi.testclient import TestClient
from pymongo.errors import BulkWriteError
from mongomock import MongoClient as MockMongoClient, database

# Import your main application
from app import app

@pytest.fixture
def sample_data():
    return {
        "rec_id": "rec123",
        "material_name": "Copper Wire",
        "items": [
            {"item_name": "Wire", "quantity": 10, "unit": "kg"},
            {"item_name": "Insulation Material", "quantity": 5, "unit": "kg"}
        ],
        "category": "Metal",
        "seller_info": {"name": "John Doe", "contact": "9876543210"}
    }

# Mock MongoClient and database for testing
client = MockMongoClient()
#db = database.Database(client, "scrapit")
#collection = db["item"]
collection = client["Scrapit"]["item"]

# Replace the real MongoDB client with the mock
#app.dependency_overrides[MongoClient] = lambda: MockMongoClient()

# Test Client for sending requests
client = TestClient(app)

# Patch the real MongoClient with our mock
# @pytest.fixture(autouse=True)
# def mock_mongo(monkeypatch):
#     monkeypatch.setattr(MockMongoClient, "return_value", client)


def test_service_msg():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 201
    assert response.json() == {"message": "CRUD root"}

def test_create(sample_data):
    """Test creating a new rec."""
    response = client.post("/record", json=sample_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["message"] == "rec created successfully"

def test_create_duplicate(sample_data):
    """Test creating a duplicate rec."""
    client.post("/record", json=sample_data)  # Create first
    response = client.post("/record", json=sample_data)  # Create duplicate
    assert response.status_code == 400
    assert response.json()["detail"] == "rec with this ID already exists."

def test_get_all(sample_data):
    """Test retrieving all recs."""
    client.post("/record", json=sample_data)  # Create a rec
    response = client.get("/record")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["rec_id"] == sample_data["rec_id"]

def test_get_by_id(sample_data):
    """Test retrieving a rec by ID."""
    client.post("/record", json=sample_data)  # Create a rec
    response = client.get(f"/record/{sample_data['rec_id']}")
    assert response.status_code == 200
    assert response.json()["rec_id"] == sample_data["rec_id"]

def test_get_rec_not_found():
    """Test retrieving a non-existing rec."""
    response = client.get("/record/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "rec not found."

def test_update(sample_data):
    """Test updating a rec."""
    client.post("/record", json=sample_data)  # Create a rec
    updates = {"name": "Updated Name"}
    response = client.put(f"/record/{sample_data['rec_id']}", json=updates)
    assert response.status_code == 200
    assert response.json()["message"] == "rec updated successfully."

def test_update_not_found():
    """Test updating a non-existing rec."""
    updates = {"name": "Updated Name"}
    response = client.put("/record/nonexistent", json=updates)
    assert response.status_code == 404
    assert response.json()["detail"] == "rec not found."

def test_delete(sample_data):
    """Test deleting a rec."""
    client.post("/record", json=sample_data)  # Create a rec
    response = client.delete(f"/record/{sample_data['rec_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "rec deleted successfully."

def test_delete_not_found():
    """Test deleting a non-existing rec."""
    response = client.delete("/record/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "rec not found."