import os

import faiss
import requests
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

import config
from ai.embeddings import embeddings
from rest_docstore import RESTDocstore

docstore = RESTDocstore()

faiss_index_path = "faiss_index"

if os.path.exists(faiss_index_path):
    faiss_index = FAISS.load_local(
        faiss_index_path, embeddings, allow_dangerous_deserialization=True
    )
else:
    faiss_index = FAISS(
        index=faiss.IndexFlatL2(len(embeddings.embed_query("hello world"))),
        embedding_function=embeddings,
        docstore=docstore,
        index_to_docstore_id={},
    )

index_to_docstore_id = faiss_index.index_to_docstore_id


def load_data():
    url = config.DOCUMENT_ENDPOINT
    limit = 100
    offset = 0

    items_from_api = []

    while True:
        try:
            response = requests.get(f"{url}?limit={limit}&offset={offset}")
            data = response.json()
        except Exception:
            print(f"Cannot reach {url} for update FAQ")
            return

        if not data or len(data["items"]) == 0:
            break

        items_from_api.extend([doc["id"] for doc in data["items"]])

        total = data["total"]
        items = data["items"]

        needed_items = [
            doc for doc in items if doc["id"] not in index_to_docstore_id.values()
        ]

        if len(needed_items) != 0:
            documents = [Document(page_content=doc["question"]) for doc in needed_items]
            ids = [doc["id"] for doc in needed_items]

            faiss_index.add_documents(documents=documents, ids=ids)

        offset += limit
        if offset >= total:
            break

    redurant_items = [
        doc_id for doc_id in index_to_docstore_id.values() if doc_id not in items_from_api
    ]

    faiss_index.delete(redurant_items)


load_data()

faiss_index.save_local("faiss_index")
