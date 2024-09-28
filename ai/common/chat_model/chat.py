from langchain_ollama import ChatOllama

import constants

chat = ChatOllama(
    model=constants.CHAT_MODEL,
    temperature=0.05,
    num_predict=256,
)

chat = chat
