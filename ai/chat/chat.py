
from ai.chat.prompt import main_prompt
from ai.common.faq_retriever.retriever import retriever
from ai.common.chat_model import chat
from langchain_core.runnables import RunnablePassthrough

def format_docs(docs):
    return "\n\n".join(f"Q: {doc.page_content}\nA: {doc.metadata['answer']}" for doc in docs)

chat_chain = (
    {
        "context": retriever | format_docs, 
        "input": RunnablePassthrough() 
    }
    | main_prompt 
    | chat
)