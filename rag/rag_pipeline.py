from rag.retriever import retrieve_chunks
from database.memory import get_memories

from utils.prompts import (
    build_rag_prompt
)

from models.llm import (
    generate_response
)


def rag_response(
    query,
    emotion,
    index,
    chunks
):

    retrieved_chunks = retrieve_chunks(
        query,
        index,
        chunks
    )

    print("\n=== RETRIEVED CHUNKS ===")
    print(len(retrieved_chunks))

    memories = get_memories()

    prompt = build_rag_prompt(
        query,
        retrieved_chunks,
        emotion,
        memories
    )

    print("\n=== PROMPT ===")
    print(prompt[:1000])

    answer = generate_response(
        prompt
    )

    print("\n=== ANSWER ===")
    print(repr(answer))

    return answer, retrieved_chunks