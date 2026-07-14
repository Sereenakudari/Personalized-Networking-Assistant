from fastapi import FastAPI, Body
from pydantic import BaseModel

# Required modules
#from backend.event_analyzer import analyze_event
#from backend.topic_generator import generate_conversation
from backend.fact_checker import fact_check
from backend.history_logger import (
    save_history,
    load_history
)
from backend.feedback_logger import (
    save_feedback,
    load_feedback
)

# Keep your advanced features
from backend.services import (
    generate_event_plan,
    networking_coach,
    summarize_history,
    summarize_feedback
)

app = FastAPI(
    title="Personalized Networking Assistant",
    version="2.0.0"
)


# -------------------------------------------------
# Home
# -------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Personalized Networking Assistant API"
    }


# -------------------------------------------------
# Request Models
# -------------------------------------------------

class ConversationRequest(BaseModel):
    event_description: str


class EventPrompt(BaseModel):
    prompt: str

"""
# =========================================================
# REQUIRED API
# POST /analyze-event
# =========================================================

@app.post("/analyze-event")
def analyze(data: ConversationRequest):

    return analyze_event(data.event_description)
"""
"""
# =========================================================
# REQUIRED API
# POST /generate-conversation
# =========================================================

@app.post("/generate-conversation")
def generate(data: ConversationRequest):

    analysis = analyze_event(
        data.event_description
    )

    response = generate_conversation(
        data.event_description,
        analysis["themes"]
    )

    save_history(
        data.event_description,
        response
    )

    return {
        "themes": analysis["themes"],
        "conversation": response
    }
"""

# =========================================================
# REQUIRED API
# GET /fact-check
# =========================================================

@app.get("/fact-check")
def verify(query: str):

    return fact_check(query)


# =========================================================
# REQUIRED API
# GET /history
# =========================================================
# =========================================================
# Conversation History
# =========================================================

@app.get("/history")
def history():

    return load_history()


# =========================================================
# Save Feedback
# =========================================================

@app.post("/feedback")
def feedback(data: dict = Body(...)):

    save_feedback(
        data["response"],
        data["feedback"]
    )

    return {
        "message": "Feedback saved successfully."
    }


# =========================================================
# Get Feedback
# =========================================================

@app.get("/feedback")
def feedback_history():

    return load_feedback()



# =========================================================
# REQUIRED API
# Feedback
# =========================================================

@app.get("/history-summary")
def history_summary():

    return {
        "summary": summarize_history()
    }


@app.get("/feedback-summary")
def feedback_summary():

    return {
        "summary": summarize_feedback()
    }


# =========================================================
# EXTRA FEATURE
# AI Event Copilot
# =========================================================

@app.post("/event-copilot")
def event_copilot(data: EventPrompt):

    result = generate_event_plan(data.prompt)

    save_history(
        data.prompt,
        result
    )

    return {
        "response": result
    }

# =========================================================
# EXTRA FEATURE
# AI Networking Coach
# =========================================================

@app.get("/networking-coach")
def coach(question: str):

    answer = networking_coach(question)

    return {
        "advice": answer
    }