from store import faiss_index

retriever = faiss_index.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 3}
)