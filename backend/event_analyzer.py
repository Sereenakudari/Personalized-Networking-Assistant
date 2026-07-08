from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_event(event_description):

    result = classifier(event_description)

    label = result[0]["label"]
    score = result[0]["score"]

    themes = []

    text = event_description.lower()

    if "ai" in text or "artificial intelligence" in text:
        themes.append("Artificial Intelligence")

    if "cyber" in text:
        themes.append("Cybersecurity")

    if "cloud" in text:
        themes.append("Cloud Computing")

    if "hackathon" in text:
        themes.append("Hackathon")

    if "conference" in text:
        themes.append("Conference")

    if "startup" in text:
        themes.append("Startup")

    if len(themes) == 0:
        themes.append("Networking")

    return {
        "themes": themes,
        "sentiment": label,
        "confidence": score
    }