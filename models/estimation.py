from db import db
from bson.objectid import ObjectId

collection = db.estimations  # collection name

def insert_estimation(data):
    """Insert a new estimation document."""
    result = collection.insert_one(data)
    return str(result.inserted_id)

def find_estimation_by_id(id):
    """Find estimation by ObjectId."""
    return collection.find_one({"_id": ObjectId(id)})

def update_estimation(id, update_data):
    """Update estimation document."""
    result = collection.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    return result.modified_count

def delete_estimation(id):
    """Delete estimation document."""
    result = collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count


def get_estimations():
    estimations_cursor = collection.find()
    estimations = []
    for est in estimations_cursor:
        est["_id"] = str(est["_id"])  # Convert ObjectId to string for JSON
        estimations.append(est)
    return estimations