import wikipediaapi

wiki = wikipediaapi.Wikipedia(
    language="en",
    user_agent="PersonalizedNetworkingAssistant/1.0 (student project)"
)

def fact_check(query):
    page = wiki.page(query)

    if page.exists():
        return {
            "summary": page.summary[:500],
            "url": page.fullurl
        }

    return {
        "summary": "No Wikipedia article found.",
        "url": ""
    }