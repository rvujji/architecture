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
        "bom_id": "BOM123",
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
    """Test creating a new BoM."""
    response = client.post("/boms", json=sample_data)
    assert response.status_code == 201
    assert "id" in response.json()
    assert response.json()["message"] == "BoM created successfully"

def test_create_duplicate(sample_data):
    """Test creating a duplicate BoM."""
    client.post("/boms", json=sample_data)  # Create first
    response = client.post("/boms", json=sample_data)  # Create duplicate
    assert response.status_code == 400
    assert response.json()["detail"] == "BoM with this ID already exists."

def test_get_all(sample_data):
    """Test retrieving all BoMs."""
    client.post("/boms", json=sample_data)  # Create a BoM
    response = client.get("/boms")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["bom_id"] == sample_data["bom_id"]

def test_get_by_id(sample_data):
    """Test retrieving a BoM by ID."""
    client.post("/boms", json=sample_data)  # Create a BoM
    response = client.get(f"/boms/{sample_data['bom_id']}")
    assert response.status_code == 200
    assert response.json()["bom_id"] == sample_data["bom_id"]

def test_get_bom_not_found():
    """Test retrieving a non-existing BoM."""
    response = client.get("/boms/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "BoM not found."

def test_update(sample_data):
    """Test updating a BoM."""
    client.post("/boms", json=sample_data)  # Create a BoM
    updates = {"name": "Updated Name"}
    response = client.put(f"/boms/{sample_data['bom_id']}", json=updates)
    assert response.status_code == 200
    assert response.json()["message"] == "BoM updated successfully."

def test_update_not_found():
    """Test updating a non-existing BoM."""
    updates = {"name": "Updated Name"}
    response = client.put("/boms/nonexistent", json=updates)
    assert response.status_code == 404
    assert response.json()["detail"] == "BoM not found."

def test_delete(sample_data):
    """Test deleting a BoM."""
    client.post("/boms", json=sample_data)  # Create a BoM
    response = client.delete(f"/boms/{sample_data['bom_id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "BoM deleted successfully."

def test_delete_not_found():
    """Test deleting a non-existing BoM."""
    response = client.delete("/boms/nonexistent")
    assert response.status_code == 404
    assert response.json()["detail"] == "BoM not found."