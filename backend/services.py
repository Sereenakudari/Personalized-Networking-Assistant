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
# FEEDBACK
# ==========================================================

def save_feedback(response, feedback):

    cursor.execute(
        """
        INSERT INTO feedback(
            response,
            feedback
        )
        VALUES(?,?)
        """,
        (
            response,
            feedback
        )
    )

    conn.commit()


def get_feedback():

    cursor.execute("""
        SELECT
        response,
        feedback
        FROM feedback
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    result = []

    for row in rows:

        result.append({

            "response": row["response"],

            "feedback": row["feedback"]

        })

    return result