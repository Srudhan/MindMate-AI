from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import create_embeddings

text = load_pdf(
    "data/documents/exam_stress.pdf"
)

chunks = chunk_text(text)

embeddings = create_embeddings(
    chunks
)

print(embeddings.shape)