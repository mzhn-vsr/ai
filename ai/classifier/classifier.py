from ai.common.chat_model import chat
from ai.common.faq_retriever import retriever
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser

from ai.classifier.prompt import classifier_prompt

def format_classifier_docs(docs):
    return "\n\n".join(
        f"Q: {doc.page_content}\nA: {doc.metadata['classifier1']},{doc.metadata['classifier2']}" 
        for doc in docs
    )

classifier_chain = (
    {
        "context": retriever | format_classifier_docs, 
        "input": RunnablePassthrough() 
    }
    | classifier_prompt 
    | chat
    | JsonOutputParser()
)