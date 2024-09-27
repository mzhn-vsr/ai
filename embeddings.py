import constants

from langchain_ollama import (
    OllamaEmbeddings
)

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

embeddings = HuggingFaceEmbeddings(
    model_name=constants.EMBEDDING_MODEL
)
