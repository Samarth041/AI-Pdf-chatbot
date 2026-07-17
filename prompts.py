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

DOCUMENT_GRADER_PROMPT="""
You are an exper documnet relevance grader.
Question
{question}

Document:
{document}

Answer ONLY with 

yes or no. Do not explain
"""

