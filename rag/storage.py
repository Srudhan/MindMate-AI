import faiss
import pickle


def save_index(index, chunks):

    faiss.write_index(
        index,
        "data/faiss.index"
    )

    with open(
        "data/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )