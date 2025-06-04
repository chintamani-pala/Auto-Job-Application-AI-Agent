# type: ignore
import json
import os

TRACK_FILE = "track.json"


# Load or initialize tracking data
def load_tracker():
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as file:
            return json.load(file)
    return {"last_index": -1}


# Save current index to tracker
def update_tracker(index):
    with open(TRACK_FILE, "w") as file:
        json.dump({"last_index": index}, file)


# Get last completed index
def get_last_completed_index():
    tracker = load_tracker()
    return tracker.get("last_index", -1)
