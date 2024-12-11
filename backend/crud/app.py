from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from typing import List
from bson import ObjectId
from db_manager import DatabaseManager
import os
import logging
import logging_config

# MongoDB Connection, Initialize Database Manager
db_manager = DatabaseManager(
    connection_string = os.environ.get("DBCONNECTIONSTRING"),
    db_name = os.environ.get("DBNAME"),
    collection_name = os.environ.get("DBCOLLECTION")
)

# FastAPI App
app = FastAPI()

logger = logging.getLogger(__name__)

# Helper Function to Convert BSON ObjectId
def to_dict(item):
    item["_id"] = str(item["_id"])
    return item

# Endpoints
@app.get("/", status_code=201)
def service_msg():
    return {"message": "CRUD root"}


@app.post("/record", status_code=201)
def create(rec: dict):
    """Create a new rec."""
    try: 
        logger.info("post rec_id = " + rec["rec_id"])
        if "rec_id" not in rec:
            raise HTTPException(status_code=400, detail="rec must include 'rec_id'.")
        if db_manager.find_by_id(rec["rec_id"]):
            raise HTTPException(status_code=400, detail="rec with this ID already exists.")
        result = db_manager.insert(rec)
        logger.info("saved rec_id = " + rec["rec_id"])
        return {"message": "rec created successfully", "id": str(result.inserted_id)}
    except HTTPException as http_exc:
        logger.error(f"HTTP Exception: {http_exc.detail}")
    except Exception as exc:
        logger.error(f"An error occurred: {str(exc)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")    

@app.get("/record", response_model=List[dict])
def get_all():
    """Get all recs."""
    return [db_manager.to_dict(rec) for rec in db_manager.find_all()]

@app.get("/record/{rec_id}", response_model=dict)
def get_by_id(rec_id: str):
    """Get a rec by ID."""
    logger.info("get red_id = " + rec_id)
    rec = db_manager.find_by_id(rec_id)
    if not rec:
        raise HTTPException(status_code=404, detail="rec not found.")
    return db_manager.to_dict(rec)

@app.put("/record/{rec_id}")
def update(rec_id: str, updates: dict):
    """Update an existing rec."""
    result = db_manager.update(rec_id, updates)
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="rec not found.")
    return {"message": "rec updated successfully."}

@app.delete("/record/{rec_id}")
def delete(rec_id: str):
    """Delete a rec by ID."""
    result = db_manager.delete(rec_id)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="rec not found.")
    return {"message": "rec deleted successfully."}