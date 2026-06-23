from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import create_faiss_index
from rag.retriever import retrieve_chunks

text = load_pdf(
    "data/documents/exam_stress.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(
    chunks
)

index = create_faiss_index(
    embeddings
)

results = retrieve_chunks(
    "How can I reduce exam anxiety?",
    index,
    chunks
)

for chunk in results:
    print("\n-----------------\n")
    print(chunk)