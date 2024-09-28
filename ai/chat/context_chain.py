from langchain_core.runnables import RunnablePassthrough

from ai.common.faq_retriever.retriever import retriever


def format_docs(docs):
    return "\n\n".join(
        f"Q: {doc.page_content}\nA: {doc.metadata['answer']}" for doc in docs
    )


context_chain = RunnablePassthrough.assign(context=(retriever | format_docs))
