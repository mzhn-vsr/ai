from typing import List
from fastapi import APIRouter
from pydantic import BaseModel

from langchain_core.documents import Document
from pydantic import BaseModel
from store import faiss_index

router = APIRouter()

class DocumentInput(BaseModel):
    id: str
    question: str
    answer: str

@router.put("/add")
def add_to_faiss(documents: List[DocumentInput]):
    faiss_index.add_documents(
        documents=[
            Document(
                page_content=doc.question, 
                metadata={
                    "answer": data["answer"],
                    "classifier1": data["classifier1"] or "ОТСУТСТВУЕТ",
                    "classifier2": data["classifier2"] or "Отсутствует",
                }
            )
            for doc in documents
        ],
        ids=[doc.id for doc in documents],
    )
    faiss_index.save_local("faiss_index")
    return {"message": "OK"}


@router.delete("/delete")
def delete_from_faiss(ids: List[str]):
    common_ids = set(ids).intersection(faiss_index.index_to_docstore_id.values())
    if not common_ids:
        return {"message": "OK"}

    faiss_index.delete(common_ids)
    faiss_index.save_local("faiss_index")
    return {"message": "OK"}