KEYWORDS = [
    "exam",
    "sleep",
    "stress",
    "anxiety",
    "presentation",
    "family",
    "relationship"
]


def should_store_memory(text):

    text = text.lower()

    return any(
        keyword in text
        for keyword in KEYWORDS
    )