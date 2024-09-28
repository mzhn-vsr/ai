import os
from langchain_community.vectorstores import FAISS
import faiss
from rest_docstore import RESTDocstore

from ai.embeddings import embeddings

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
        index_to_docstore_id={}
    )

index_to_docstore_id = faiss_index.index_to_docstore_id

from langchain_core.documents import Document

import requests
import config 

def load_data():
    url = config.DOCUMENT_ENDPOINT
    limit = 100 
    offset = 0 
    while True:
        response = requests.get(
            f'{url}?limit={limit}&offset={offset}'
        )
        data = response.json()
    
        if not data or len(data['items']) == 0:
            break
    
        total = data['total']
        items = data['items']

        needed_items = [doc for doc in items if doc['id'] not in index_to_docstore_id.values() ]

        if len(needed_items) != 0:
            documents=[
                Document(page_content=doc['question'])
                for doc in needed_items
            ]
            ids=[doc['id'] for doc in needed_items]
        
            faiss_index.add_documents(
                documents=documents,
                ids=ids
            )
    
        offset += limit
        if offset >= total:
            break

load_data()

faiss_index.save_local("faiss_index")