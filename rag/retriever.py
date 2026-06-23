from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)


def retrieve_chunks(
    query,
    index,
    chunks,
    top_k=2
):

    query_vector = model.encode(
        [query]
    )

    distances, indices = index.search(
        query_vector,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(
            chunks[idx]
        )

    return results