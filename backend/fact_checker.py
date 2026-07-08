import wikipedia


def fact_check(query):

    try:

        page = wikipedia.page(query)

        return {
            "summary": wikipedia.summary(query, sentences=2),
            "url": page.url
        }

    except Exception as e:

        return {
            "summary": str(e),
            "url": ""
        }