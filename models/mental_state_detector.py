from models.llm import generate_response


def detect_mental_state(text):

    prompt = f"""
You are a mental health classifier.

Classify the user's mental state into exactly one category:

- anxious
- stressed
- sad
- overwhelmed
- positive
- neutral

User message:
{text}

Return ONLY one word.
"""

    response = generate_response(prompt)

    state = response.strip().lower()

    allowed = [
        "anxious",
        "stressed",
        "sad",
        "overwhelmed",
        "positive",
        "neutral"
    ]

    if state not in allowed:
        return "neutral"

    return state