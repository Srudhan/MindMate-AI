CRISIS_KEYWORDS = [
    "suicide",
    "kill myself",
    "end my life",
    "self harm",
    "hurt myself",
    "don't want to live",
    "want to die",
    "take my life"
]


def detect_crisis(text):

    text = text.lower()

    return any(
        keyword in text
        for keyword in CRISIS_KEYWORDS
    )