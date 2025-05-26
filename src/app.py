"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pymongo import MongoClient
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent, "static")), name="static")

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["mergington"]
activities_col = db["activities"]



# Pre-populate MongoDB if empty
if activities_col.count_documents({}) == 0:
    for name, details in hardcoded_activities.items():
        doc = {"_id": name, **details}
        activities_col.insert_one(doc)

@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")

@app.get("/activities")
def get_activities():
    activities = {}
    for doc in activities_col.find():
        name = doc["_id"]
        details = doc.copy()
        del details["_id"]
        activities[name] = details
    return activities

@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    activity = activities_col.find_one({"_id": activity_name})
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")
    activities_col.update_one(
        {"_id": activity_name},
        {"$push": {"participants": email}}
    )
    return {"message": f"Signed up {email} for {activity_name}"}

@app.post("/activities/{activity_name}/unregister")
def unregister_from_activity(activity_name: str, email: str):
    activity = activities_col.find_one({"_id": activity_name})
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    if email not in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is not registered for this activity")
    activities_col.update_one(
        {"_id": activity_name},
        {"$pull": {"participants": email}}
    )
    return {"message": f"Unregistered {email} from {activity_name}"}