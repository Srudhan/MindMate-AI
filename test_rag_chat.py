from rag.setup_rag import initialize_rag
from rag.rag_pipeline import rag_response


index, chunks = initialize_rag()

answer = rag_response(
    query="How can I reduce exam anxiety?",
    emotion="fear",
    index=index,
    chunks=chunks
)

print("\nANSWER:")
print(answer)