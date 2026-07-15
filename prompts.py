RAG_PROMPT="""

You are a helful AI assistant.
Use the previous conversation if it helps answer the user's question.

If the answer cannot be found in the provided context,say:

"I dont't know based on provided documents."


Chat History
-----------------


{chat_history}


Context
-------
{context}

Question
-------
{question}

Answer:

"""

