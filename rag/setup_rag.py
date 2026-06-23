from pathlib import Path

from rag.loader import load_pdf
from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import create_faiss_index


def initialize_rag():

    all_chunks = []

    pdf_folder = Path(
        "data/documents"
    )

    for pdf_file in pdf_folder.glob(
        "*.pdf"
    ):

        text = load_pdf(
            str(pdf_file)
        )

        chunks = chunk_text(text)

        all_chunks.extend(chunks)

    embeddings = create_embeddings(
        all_chunks
    )

    index = create_faiss_index(
        embeddings
    )

    return index, all_chunks