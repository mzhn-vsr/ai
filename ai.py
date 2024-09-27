from operator import itemgetter
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories.in_memory import (
    ChatMessageHistory,
)
from langchain_core.runnables import RunnablePassthrough
from store import faiss_index
from langchain_core.messages.ai import AIMessage

from embeddings import embeddings

from langchain_ollama import ChatOllama

chat = ChatOllama(
    model="krith/qwen2.5-14b-instruct:IQ4_XS",
    temperature = 0.8,
    num_predict = 256,
)

def qwen_fix(message: AIMessage) -> AIMessage:
    message.content = message.content.split("<|im_start|>assistant\n")[-1]
    return message

chat = chat | qwen_fix


#############################################
condense_question_system_template = (
"""
As an assistant, your task is to act as a question reformulation expert. 
Given a conversation history and the user's most recent question, 
your role is to rephrase or restate the latest question into a standalone 
version that can be fully understood without any reference to the 
prior conversation. Do not answer the question or provide additional 
explanations, simply focus on transforming it into a clear, self-contained query.

<context>
{chat_history}
</context>
"""
)

contextualize_q_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", condense_question_system_template),
        ("human", "{input}"),
    ]
)

demo = ChatMessageHistory()

def get_session_history(session_id: str):
    return demo

SYSTEM_TEMPLATE = """
You are a high-class support chatbot for RUTUBE.
Your task is to provide an accurate answer to the user's question, but only if it is related to the RUTUBE platform. Use only the context provided, following these rules:

- Answer questions **only** about the RUTUBE platform.
- Do not alter any text in quotation marks.
- **Do not generate information** that is not present in the <context></context> tags.
- If the answer is not in the provided context, say "Я не знаю ответа на ваш вопрос".
- Always limit responses to 3-5 sentences.

ONLY ANSWER RUTUBE QUESTIONS.

<context>
{context}
</context>
"""

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system", 
            SYSTEM_TEMPLATE
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
    ]
)

def format_docs(docs):
    return "\n\n".join(f"Q: {doc.page_content}\nA:{doc.metadata['answer']}" for doc in docs)

retriever = faiss_index.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 2}
)

def get_content(obj):
    return obj.content

context_chain = RunnablePassthrough.assign(
    context=(
        contextualize_q_prompt 
        | chat 
        | get_content
        | retriever 
        | format_docs
    )
)

from langchain_core.output_parsers.string import StrOutputParser

chain =  context_chain | prompt | chat | StrOutputParser()

main_chat_pipeline = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)