from langchain_core.prompts import ChatPromptTemplate

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
