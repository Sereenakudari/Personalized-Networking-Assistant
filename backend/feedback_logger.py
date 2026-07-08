import json
import os

FEEDBACK_FILE = "feedback.json"


def save_feedback(response, feedback):
    """
    Save user feedback into feedback.json
    """

    feedback_data = []

    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r") as f:
                feedback_data = json.load(f)
        except json.JSONDecodeError:
            feedback_data = []

    feedback_data.append({
        "response": response,
        "feedback": feedback
    })

    with open(FEEDBACK_FILE, "w") as f:
        json.dump(feedback_data, f, indent=4)


def load_feedback():
    """
    Load all feedback from feedback.json
    """

    if not os.path.exists(FEEDBACK_FILE):
        return []

    try:
        with open(FEEDBACK_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []