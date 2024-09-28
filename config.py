import os

# Endpoint содержащий базу знаний (RESTDocStore)
DOCUMENT_ENDPOINT = os.getenv("DOCUMENT_ENDPOINT")

# Путь хранения FAISS
FAISS_PATH = os.getenv("FAISS_PATH", "faiss_index")

# Путь к классам для классификации
CLASSES_PATH = os.getenv("CLASSES_PATH", "classes.csv")
