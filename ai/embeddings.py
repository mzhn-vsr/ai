import constants

from langchain_huggingface import (
    HuggingFaceEmbeddings
)

embeddings = HuggingFaceEmbeddings(
    model_name=constants.EMBEDDING_MODEL
)
