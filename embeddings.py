from langchain_ollama import (
    OllamaEmbeddings
)

embeddings = OllamaEmbeddings(
    model="jeffh/intfloat-multilingual-e5-large:f16"
)