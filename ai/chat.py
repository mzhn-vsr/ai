import constants

from langchain_ollama import ChatOllama
from langchain_core.messages.ai import AIMessage

chat = ChatOllama(
    model=constants.CHAT_MODEL,
    temperature = 0.05,
    num_predict = 256,
)

def qwen_fix(message: AIMessage) -> AIMessage:
    message.content = message.content.split("<|im_start|>assistant\n")[-1]
    return message

def debug(obj):
    print(obj)
    return obj

chat = chat #| qwen_fix