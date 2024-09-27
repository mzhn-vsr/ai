import os
from langchain_community.vectorstores import FAISS
import faiss
from rest_docstore import RESTDocstore

from embeddings import embeddings

docstore = RESTDocstore()
index_to_docstore_id = {}

faiss_index = FAISS(
    index=faiss.IndexFlatL2(len(embeddings.embed_query("hello world"))),
    embedding_function=embeddings,
    docstore=docstore,
    index_to_docstore_id=index_to_docstore_id
)

faiss_index_path = 'faiss_index'

if os.path.exists(faiss_index_path):
    faiss_index.load_local(
        faiss_index_path, 
        embeddings,
        allow_dangerous_deserialization = True
    )
