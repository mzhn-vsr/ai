from langchain_core.output_parsers.string import StrOutputParser
from ai.context_chain import context_chain, format_docs, retriever
from ai.main_prompt import main_prompt
from ai.chat import chat, debug
from langchain_core.runnables import RunnablePassthrough
# from ai.classifier_chain.classifier_chain import classifier_chain

chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough() }
    | main_prompt 
    | chat
#    | StrOutputParser()
)