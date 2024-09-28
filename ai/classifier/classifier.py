from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnablePassthrough

from ai.classifier.prompt import classifier_prompt
from ai.common.chat_model import chat
from ai.common.faq_retriever import retriever


def format_classifier_docs(docs):
    return "\n\n".join(
        f"Q: {doc.page_content}\nA: "
        f"{doc.metadata['classifier1']},{doc.metadata['classifier2']}"
        for doc in docs
    )


classifier_chain = (
    {"context": retriever | format_classifier_docs, "input": RunnablePassthrough()}
    | classifier_prompt
    | chat
    | JsonOutputParser()
)
