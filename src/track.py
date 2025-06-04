# type: ignore
import json
import os

TRACK_FILE = "track.json"
DAILY_TRACK_FILE = "daily_track.json"


# Load or initialize tracking data
def load_tracker():
    if os.path.exists(TRACK_FILE):
        with open(TRACK_FILE, "r") as file:
            return json.load(file)
    return {"last_index": -1}


def load_daily_tracker():
    if os.path.exists(DAILY_TRACK_FILE):
        with open(DAILY_TRACK_FILE, "r") as file:
            return json.load(file)
    return {"daily_count": 0}


# Save current index to tracker
def update_tracker(index):
    with open(TRACK_FILE, "w") as file:
        json.dump({"last_index": index}, file)


def update_daily_tracker(index):
    with open(DAILY_TRACK_FILE, "w") as file:
        json.dump({"daily_count": index}, file)


# Get last completed index
def get_last_completed_index():
    tracker = load_tracker()
    return tracker.get("last_index", -1)


def get_last_completed_daily_index():
    daily_tracker = load_daily_tracker()
    return daily_tracker.get("daily_count", 0)
