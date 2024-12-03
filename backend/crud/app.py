from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List
from bson import ObjectId
from db_manager import DatabaseManager

# MongoDB Connection, Initialize Database Manager
db_manager = DatabaseManager(
    connection_string="mongodb://mongodb:27017/",
    db_name="Scrapit",
    collection_name="item"
)

# FastAPI App
app = FastAPI()

# Helper Function to Convert BSON ObjectId
def to_dict(item):
    item["_id"] = str(item["_id"])
    return item

# Endpoints
@app.get("/", status_code=201)
def service_msg():
    return {"message": "CRUD root"}


@app.post("/boms", status_code=201)
def create(bom: dict):
    """Create a new BoM."""
    if "bom_id" not in bom:
        raise HTTPException(status_code=400, detail="BoM must include 'bom_id'.")
    if db_manager.find_by_id(bom["bom_id"]):
        raise HTTPException(status_code=400, detail="BoM with this ID already exists.")
    result = db_manager.insert(bom)
    return {"message": "BoM created successfully", "id": str(result.inserted_id)}

@app.get("/boms", response_model=List[dict])
def get_all():
    """Get all BoMs."""
    return [db_manager.to_dict(bom) for bom in db_manager.find_all()]

@app.get("/boms/{bom_id}", response_model=dict)
def get_by_id(bom_id: str):
    """Get a BoM by ID."""
    bom = db_manager.find_by_id(bom_id)
    if not bom:
        raise HTTPException(status_code=404, detail="BoM not found.")
    return db_manager.to_dict(bom)

@app.put("/boms/{bom_id}")
def update(bom_id: str, updates: dict):
    """Update an existing BoM."""
    result = db_manager.update(bom_id, updates)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="BoM not found.")
    return {"message": "BoM updated successfully."}

@app.delete("/boms/{bom_id}")
def delete(bom_id: str):
    """Delete a BoM by ID."""
    result = db_manager.delete(bom_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="BoM not found.")
    return {"message": "BoM deleted successfully."}