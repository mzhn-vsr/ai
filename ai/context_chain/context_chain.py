from langchain_core.runnables import RunnablePassthrough
from ai.chat import chat
from ai.context_chain.summarize import contextualize_q_prompt
from ai.context_chain.retriever import retriever

def format_docs(docs):
    return "\n\n".join(f"Q: {doc.page_content}\nA:{doc.metadata['answer']}" for doc in docs)

def get_content(obj):
    return obj.content

context_chain = RunnablePassthrough.assign(
    context=(
        #contextualize_q_prompt 
        #| chat 
        #| get_content
        retriever 
        | format_docs
    )
)