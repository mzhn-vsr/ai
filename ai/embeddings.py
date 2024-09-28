from langchain_huggingface import HuggingFaceEmbeddings

import constants

embeddings = HuggingFaceEmbeddings(model_name=constants.EMBEDDING_MODEL)
