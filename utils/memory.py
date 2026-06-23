def build_conversation(messages, emotion):

    conversation = f"""
You are MindMate AI.

The user's detected emotion is:
{emotion}

Respond supportively and empathetically.

Conversation:
"""

    for msg in messages:
        conversation += (
            f"{msg['role']}: {msg['content']}\n"
        )

    return conversation