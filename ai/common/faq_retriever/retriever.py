from store import faiss_index

retriever = faiss_index.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k": 5,
        "fetch_k": 30,
        "score_threshold": 0.6,
    },
)
