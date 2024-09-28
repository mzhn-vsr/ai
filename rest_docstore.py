from typing import Dict, List, Union

import requests
from langchain_community.docstore.base import AddableMixin, Docstore
from langchain_core.documents import Document

from config import DOCUMENT_ENDPOINT


class RESTDocstore(Docstore, AddableMixin):
    """
    RESTDocsotre - реализация Langchain docstore.
    """

    def __init__(self):
        self.base_url = DOCUMENT_ENDPOINT
        pass

    def search(self, search: str) -> Union[str, Document]:
        response = requests.get(f"{self.base_url}/{search}")

        if response.status_code == 200:
            data = response.json()

            return Document(
                page_content=data["question"],
                metadata={
                    "answer": data["answer"],
                    "classifier1": data["classifier1"] or "ОТСУТСТВУЕТ",
                    "classifier2": data["classifier2"] or "Отсутствует",
                },
            )
        else:
            return f"ID {search} not found."

    def add(self, texts: Dict[str, Document]) -> None:
        pass

    def delete(self, ids: List) -> None:
        pass
