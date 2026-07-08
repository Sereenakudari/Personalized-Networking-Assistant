from backend.services import model


def generate_conversation(event_description, themes):

    prompt = f"""
You are an AI Networking Assistant.

Event Description:
{event_description}

Networking Themes:
{", ".join(themes)}

Generate 5 professional networking conversation starters.

Requirements:
- Friendly
- Professional
- Suitable for conferences
- Natural
- Use bullet points only.
"""

    response = model.generate_content(prompt)

    return response.text
