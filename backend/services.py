from backend.database import conn, cursor
import wikipedia
import os
from dotenv import load_dotenv
import google.generativeai as genai

# ----------------------------
# Load Environment Variables
# ----------------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


# ==========================================================
# AI EVENT COPILOT
# ==========================================================

def generate_event_plan(user_prompt):

    prompt = f"""
You are an AI Event Copilot.

The user said:

{user_prompt}

Generate a detailed networking guide.

Use Markdown.

Include:

# 📌 Event Overview

# 🎯 Networking Objectives

# ✅ Before the Event

# 🤝 During the Event

# 💬 Conversation Ideas

# ❓ Smart Questions

# 👥 People to Connect With

# 🚫 Common Mistakes

# 📧 Follow-up Message

# ⭐ Personalized Advice

Be detailed.
"""

    response = model.generate_content(prompt)

    cursor.execute(
        """
        INSERT INTO history(
            bio,
            event,
            interests,
            response
        )
        VALUES(?,?,?,?)
        """,
        (
            "-",
            user_prompt,
            "-",
            response.text
        )
    )

    conn.commit()

    return response.text


# ==========================================================
# AI NETWORKING COACH
# ==========================================================

def networking_coach(question):

    prompt = f"""
You are an AI Networking Coach.

Answer ONLY networking-related questions.

Question:

{question}

Give practical advice.

Use Markdown.

Use bullet points.
"""

    response = model.generate_content(prompt)

    return response.text


# ==========================================================
# FACT CHECKER
# ==========================================================

def fact_check(query):

    try:

        page = wikipedia.page(query)

        summary = wikipedia.summary(
            query,
            sentences=3
        )

        return {
            "summary": summary,
            "url": page.url
        }

    except Exception as e:

        return {
            "summary": str(e),
            "url": ""
        }


# ==========================================================
# HISTORY
# ==========================================================

def get_history():

    cursor.execute("""
        SELECT
        bio,
        event,
        interests,
        response
        FROM history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    history = []

    for row in rows:

        history.append({

            "bio": row["bio"],

            "event": row["event"],

            "interests": row["interests"],

            "response": row["response"]

        })

    return history


# ==========================================================
# History
# ==========================================================

def summarize_history():

    cursor.execute("""
        SELECT event, response
        FROM history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    if len(rows) == 0:
        return "No conversation history available."

    history_text = ""

    for event, response in rows:

        history_text += f"""
Event:
{event}

Response:
{response}

"""

    prompt = f"""
You are an AI Networking Assistant.

Below is the user's conversation history.

{history_text}

Analyze the user's networking activities.

Provide:

1. Overall networking interests
2. Frequently discussed topics
3. Networking strengths
4. Areas for improvement
5. Personalized recommendations

Format the response using Markdown.
"""

    response = model.generate_content(prompt)

    return response.text

# ==========================================================
# FEEDBACK
# ==========================================================

def summarize_feedback():

    cursor.execute("""
        SELECT feedback
        FROM feedback
    """)

    rows = cursor.fetchall()

    if len(rows) == 0:
        return "No feedback available."

    feedback_text = "\n".join(
        row[0] for row in rows
    )

    prompt = f"""
You are an AI Analyst.

User Feedback:

{feedback_text}

Analyze the feedback.

Provide:

1. Overall sentiment
2. Positive observations
3. Negative observations
4. Suggestions for improvement
5. Final summary

Format the response using Markdown.
"""

    response = model.generate_content(prompt)

    return response.text
