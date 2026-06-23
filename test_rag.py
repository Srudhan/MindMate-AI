from rag.loader import load_pdf
from rag.chunker import chunk_text

text = load_pdf(
    "data/documents/exam_stress.pdf"
)

print("Characters:", len(text))

chunks = chunk_text(text)

print("Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])