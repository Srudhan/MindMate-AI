def build_rag_prompt(
    query,
    retrieved_chunks,
    emotion,
    memories
):

    context = "\n\n".join(
        retrieved_chunks
    )

    memory_context = "\n".join(
        memories
    )

    prompt = f"""
You are MindMate AI, an empathetic mental wellness assistant.

Detected Mental State:
{emotion}

Relevant User Memories:
{memory_context}

Knowledge Base Context:
{context}

Instructions:
- Be empathetic and supportive.
- Keep responses under 120 words.
- Avoid long essays.
- Avoid too many bullet points.
- Do not overwhelm the user with too many techniques.
- If appropriate, mention relevant memories.
- Ask one follow-up question if it feels natural.

User:
{query}

Assistant:
"""

    return prompt