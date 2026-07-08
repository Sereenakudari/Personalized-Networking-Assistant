import json
import os

HISTORY_FILE = "history.json"


def save_history(event_description, response):

    history = load_history()

    history.append({
        "bio": "-",
        "event": event_description,
        "interests": "-",
        "response": response
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r") as f:
        return json.load(f)